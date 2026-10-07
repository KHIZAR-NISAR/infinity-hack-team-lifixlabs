import uuid
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

def generate_uuid():
    return str(uuid.uuid4())

class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False) # ADMIN, MANAGER, AGENT
    specialization = db.Column(db.String(100), nullable=True)
    skills = db.Column(db.String(255), nullable=True)

class Project(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    name = db.Column(db.String(200), nullable=False)
    client_name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    manager_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    deadline = db.Column(db.String(20), nullable=True)

class Task(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=generate_uuid)
    project_id = db.Column(db.String(36), db.ForeignKey('project.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    assignee_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    deadline = db.Column(db.String(20), nullable=True)
    estimated_hours = db.Column(db.Float, nullable=True)

def seed_demo_users():
    demo_users = [
        {"name": "Admin", "email": "admin@novaworks.example", "role": "ADMIN", "specialization": "Administrator", "skills": "Company overview, transcript creation"},
        {"name": "Ayesha Khan", "email": "ayesha@novaworks.example", "role": "MANAGER", "specialization": "Web PM", "skills": "Web projects, client coordination"},
        {"name": "Bilal Ahmed", "email": "bilal@novaworks.example", "role": "MANAGER", "specialization": "Mobile PM", "skills": "Mobile projects, delivery planning"},
        {"name": "Hina Malik", "email": "hina@novaworks.example", "role": "MANAGER", "specialization": "AI PM", "skills": "AI projects, requirement review"},
        {"name": "Ali Raza", "email": "ali@novaworks.example", "role": "AGENT", "specialization": "Full-Stack", "skills": "React, frontend integration"},
        {"name": "Hamza Shah", "email": "hamza@novaworks.example", "role": "AGENT", "specialization": "Full-Stack", "skills": "Node.js, databases, APIs"},
        {"name": "Sara Noor", "email": "sara@novaworks.example", "role": "AGENT", "specialization": "App Developer", "skills": "Flutter, mobile UI"},
        {"name": "Usman Tariq", "email": "usman@novaworks.example", "role": "AGENT", "specialization": "App Developer", "skills": "Flutter, integration, testing"},
        {"name": "Zain Abbas", "email": "zain@novaworks.example", "role": "AGENT", "specialization": "AI Developer", "skills": "LLMs, extraction, prompts"},
        {"name": "Maryam Asif", "email": "maryam@novaworks.example", "role": "AGENT", "specialization": "AI Developer", "skills": "Retrieval, document processing"}
    ]

    for u in demo_users:
        existing = User.query.filter_by(email=u["email"]).first()
        if not existing:
            new_user = User(
                name=u["name"],
                email=u["email"],
                password_hash=generate_password_hash("Demo123!"),
                role=u["role"],
                specialization=u["specialization"],
                skills=u["skills"]
            )
            db.session.add(new_user)
    db.session.commit()
