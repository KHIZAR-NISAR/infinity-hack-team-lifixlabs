import os
import json
import requests
from flask import Flask, render_template, request, redirect, session, url_for, flash
from models import db, User, Project, Task, seed_demo_users
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = 'super-secret-hackathon-key'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///dev.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    try:
        db.create_all()
        seed_demo_users()
    except Exception as e:
        print(f"[WARN] DB init failed: {e}")

def get_current_user():
    user_id = session.get('user_id')
    if not user_id:
        return None
    return User.query.get(user_id)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        # In a real app we check password_hash. For this hackathon, just allow if email exists and password is Demo123!
        if user and password == "Demo123!":
            session['user_id'] = user.id
            session['role'] = user.role
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials")
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
        
    projects = []
    tasks = []
    team = User.query.all()
    
    if user.role == 'ADMIN':
        projects = Project.query.all()
    elif user.role == 'MANAGER':
        projects = Project.query.filter_by(manager_id=user.id).all()
    elif user.role == 'AGENT':
        tasks = Task.query.filter_by(assignee_id=user.id).all()
        # Get distinct projects for these tasks
        project_ids = list(set([t.project_id for t in tasks]))
        projects = Project.query.filter(Project.id.in_(project_ids)).all()
        
    return render_template('dashboard.html', user=user, projects=projects, tasks=tasks, team=team)

@app.route('/project/<project_id>')
def project_detail(project_id):
    user = get_current_user()
    if not user:
        return redirect(url_for('login'))
        
    project = Project.query.get_or_404(project_id)
    
    # Access control
    if user.role == 'MANAGER' and project.manager_id != user.id:
        return "Unauthorized", 403
    if user.role == 'AGENT':
        agent_tasks = Task.query.filter_by(project_id=project.id, assignee_id=user.id).all()
        if not agent_tasks:
            return "Unauthorized", 403
            
    tasks = Task.query.filter_by(project_id=project.id).all()
    if user.role == 'AGENT':
        # Agents only see their own tasks
        tasks = [t for t in tasks if t.assignee_id == user.id]
        
    manager = User.query.get(project.manager_id)
    
    return render_template('project.html', project=project, tasks=tasks, manager=manager, user=user)

@app.route('/api/transcript', methods=['POST'])
def process_transcript():
    user = get_current_user()
    if not user or user.role != 'ADMIN':
        return {"error": "Unauthorized"}, 403
        
    transcript = request.form.get('transcript')
    if not transcript:
        return {"error": "Transcript is empty"}, 400
        
    # Build directory JSON to feed to AI
    team = User.query.all()
    directory = [{"id": u.id, "name": u.name, "role": u.role, "skills": u.skills} for u in team]
    
    api_key = os.environ.get('AI_API_KEY')
    if not api_key:
        return {"error": "AI API Key missing"}, 500
        
    prompt = f"""
    You are an expert AI Project Manager for NovaWorks Technologies.
    Read the following transcript and extract the project and task details.
    
    CRITICAL RULES (HACKATHON TRAPS TO AVOID):
    1. FINAL DECISIONS ONLY: The transcript has people suggesting dates/hours, then correcting them later. Only output the FINAL agreed dates, owners, and hours.
    2. REJECT OUT OF SCOPE: Do NOT create tasks for payments, inventory, live maps, driver tracking, or external ticketing services.
    3. KAMRAN IS NOT AN EMPLOYEE: Ignore anyone not in the directory provided below. Do not create users.
    4. TASKS MUST BE SEPARATE: Do not combine Ali's two frontend tasks. Do not combine Hamza's API tasks across projects.
    5. NO MANAGER TASKS: Only AGENTs get tasks.
    6. DATE FORMAT: YYYY-MM-DD. (Assume year is 2026).
    
    COMPANY DIRECTORY:
    {json.dumps(directory, indent=2)}
    
    TRANSCRIPT:
    {transcript}
    
    OUTPUT SCHEMA: Return raw valid JSON matching this exact structure:
    {{
      "projects": [
        {{
          "name": "Project Name",
          "clientName": "Client Name",
          "description": "Brief description",
          "managerId": "Valid ID from directory",
          "deadline": "YYYY-MM-DD",
          "tasks": [
            {{
              "title": "Task Title",
              "description": "Brief task details",
              "assigneeId": "Valid ID from directory",
              "deadline": "YYYY-MM-DD",
              "estimatedHours": 12
            }}
          ]
        }}
      ]
    }}
    Return ONLY JSON. No markdown formatting blocks like ```json. Just raw `{...}`.
    """
    
    try:
        # Call Gemini REST API directly
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "temperature": 0.0,
                "response_mime_type": "application/json"
            }
        }
        resp = requests.post(url, json=payload)
        resp_data = resp.json()
        
        if 'error' in resp_data:
            return {"error": resp_data['error']['message']}, 500
            
        ai_text = resp_data['candidates'][0]['content']['parts'][0]['text']
        ai_json = json.loads(ai_text)
        
        # Save to DB transactionally
        try:
            for p in ai_json.get('projects', []):
                project = Project(
                    name=p['name'],
                    client_name=p['clientName'],
                    description=p.get('description', ''),
                    manager_id=p['managerId'],
                    deadline=p['deadline']
                )
                db.session.add(project)
                db.session.flush() # get ID
                
                for t in p.get('tasks', []):
                    task = Task(
                        project_id=project.id,
                        title=t['title'],
                        description=t.get('description', ''),
                        assignee_id=t['assigneeId'],
                        deadline=t['deadline'],
                        estimated_hours=float(t['estimatedHours'])
                    )
                    db.session.add(task)
            db.session.commit()
            return {"success": True}
        except Exception as e:
            db.session.rollback()
            return {"error": f"Database error: {str(e)}"}, 500
            
    except Exception as e:
        return {"error": f"AI Parsing error: {str(e)}"}, 500

if __name__ == '__main__':
    app.run(debug=True, port=8000)
