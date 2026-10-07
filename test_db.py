from app import app
from models import db, User, seed_demo_users
from sqlalchemy import text

with app.app_context():
    try:
        # Check connection
        db.session.execute(text('SELECT 1'))
        print("Connected to DB successfully.")
        
        # Add users
        print("Seeding users...")
        seed_demo_users()
        
        # Commit
        db.session.commit()
        print("Seeding committed.")
        
        # Verify
        users = User.query.all()
        for user in users:
            print(f"{user.name} - {user.email} - {user.role}")
            
    except Exception as e:
        print(f"Error: {e}")
