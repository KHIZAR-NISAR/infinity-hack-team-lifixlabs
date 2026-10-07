# NovaWorks AI CRM - Meeting to Project Automation

## Team
- Team name: LiFixLabs
- Members and responsibilities: 
  - Khizar Nisar (Backend, DB, DevOps)
  - Ahmad Bilal (Frontend, UI Integration, AI Prompts)
  - (Add remaining team members if any)
- Repository: https://github.com/KHIZAR-NISAR/infinity-hack-team-lifixlabs

## What Works
- **Authentication & Roles:** Secure login system with Admin, Manager, and Agent roles securely managed via Flask sessions.
- **Seeded Login Data:** Database automatically seeds 10 required dummy users with their respective roles on the first startup.
- **Admin Dashboard:** Admin can view overview and initiate project creation from meeting transcripts. (Note: Transcript-to-Project extraction logic is pending full integration).
- **Manager View:** Mapped templates for Manager to view assigned projects.
- **Agent View:** Mapped templates for Agents to view individual tasks.
- **Environment & Security Protocols:** Strict `.env` usage. No API keys or passwords are hardcoded in the codebase. Production uses Railway environment variables. GitHub Push protection rules are respected by keeping `.env` completely out of git history.

## Technology Stack
- Frontend: HTML5, TailwindCSS (via CDN), Jinja2 Templates
- Backend: Flask 3.1.3 (Python)
- Database: PostgreSQL (Supabase Connection Pooler) + SQLAlchemy ORM + psycopg2
- AI: Google Gemini (API Keys managed via environment variables)
- Authentication/session approach: Server-side secure HTTP-only sessions via Flask `session` object.

## Links
- Live application: https://infinity-hack-team-lifixlabs-production.up.railway.app
- Demo video: Not Required (App is successfully deployed live).

## Requirements
- Python 3.10+
- `pip` (Python package manager)
- PostgreSQL Database
- Valid AI API Key

## Run Locally
1. Clone this repository and enter its directory:
   ```sh
   git clone https://github.com/KHIZAR-NISAR/infinity-hack-team-lifixlabs.git
   cd infinity-hack-team-lifixlabs
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Copy the provided `.env.example` to `.env`.
   ```sh
   cp .env.example .env
   ```
5. Set environment variables in the `.env` file using your local/private values (Database URL, AI API Key, etc.).
6. The app is configured to automatically create the database schema on startup via SQLAlchemy `db.create_all()`.
7. The app automatically seeds all ten demo users via `seed_demo_users()` when the app contexts loads.
8. Start backend and frontend:
   ```sh
   python app.py
   ```
   Open your browser and navigate to `http://127.0.0.1:5000`.

## Environment Variables
| Variable | Purpose | Where configured |
| --- | --- | --- |
| `DATABASE_URL` | PostgreSQL Database connection string | Backend (`.env` or Railway Variables) |
| `AI_API_KEY` | AI provider credential for parsing transcripts | Backend (`.env` or Railway Variables) |
| `SECRET_KEY` | Flask Session signing secret | Backend (`.env` or Railway Variables) |
| `PORT` | Defines the port to bind (default 8000 on Railway) | Deployment (Railway Variables) |

**Security Note:** All API Keys and connection strings are strictly managed via environment variables and are completely excluded from source control (`.gitignore` protects `.env`).

## Demo Login Accounts
These emails are fictional identifiers, not mailboxes. Signup, email verification, and forgot password are unnecessary.

| Role | Name | Demo email | Password |
| --- | --- | --- | --- |
| Admin | Admin | admin@novaworks.example | Demo123! |
| Manager | Ayesha Khan | ayesha@novaworks.example | Demo123! |
| Manager | Bilal Ahmed | bilal@novaworks.example | Demo123! |
| Manager | Hina Malik | hina@novaworks.example | Demo123! |
| Agent | Ali Raza | ali@novaworks.example | Demo123! |
| Agent | Hamza Shah | hamza@novaworks.example | Demo123! |
| Agent | Sara Noor | sara@novaworks.example | Demo123! |
| Agent | Usman Tariq | usman@novaworks.example | Demo123! |
| Agent | Zain Abbas | zain@novaworks.example | Demo123! |
| Agent | Maryam Asif | maryam@novaworks.example | Demo123! |

## How Judges Can Test
1. Access the deployed application at the Live Link provided above.
2. The initial screen is the Login UI.
3. Use the demo credentials from the table above to test Authentication (e.g., `admin@novaworks.example` / `Demo123!`).
4. Incorrect passwords or emails will trigger a validation error gracefully.
5. Successful login directs the user to the personalized Dashboard.
6. The database is hosted securely via Supabase, ensuring persistent data across sessions.

## Deployment Details
- Deployment status: Live
- Frontend host: Railway (served natively by Flask)
- Backend host: Railway (Gunicorn WSGI)
- Database: Supabase PostgreSQL (IPv4 Transaction Pooler enabled with SSL)
- Deployed branch/commit: `main`

### How We Deployed
1. Deployed directly via GitHub Repository connection on Railway.
2. Uses standard `Procfile` specifying `web: gunicorn app:app --bind 0.0.0.0:$PORT` for production deployment.
3. Database provisioned on Supabase. Connection string uses Transaction Pooler for IPv4 compatibility and sets `sslmode=require`.
4. Environment variables (`DATABASE_URL`, `AI_API_KEY`, `SECRET_KEY`, `PORT`) configured securely in Railway App Settings without quotes.
5. Schema and seed commands execute safely at startup using a `try-except` guard in the app context.

## Known Limitations
- The integration for passing the meeting transcript directly to the AI model and saving the AI output to the Project/Task tables is under development.
- UI mapping for individual Task interaction and Agent feedback is pending.

## Submission Summary
- Source repository: https://github.com/KHIZAR-NISAR/infinity-hack-team-lifixlabs
- Live link: https://infinity-hack-team-lifixlabs-production.up.railway.app
- Setup and seed commands: Automated on app startup.
- Demo login accounts: Confirmed working securely with password verification.
- Features completed: Full Auth System, DB Schema, Secure Deployment (Railway + Supabase), Secret Protocols Followed, UI Template mapping started.