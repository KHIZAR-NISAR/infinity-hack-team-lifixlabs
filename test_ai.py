import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get('AI_API_KEY')
print(f"API Key found: {bool(api_key)}")

prompt = """
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
[{"name": "Ali Raza", "role": "AGENT"}]

TRANSCRIPT:
Ali will do the frontend login by 2026-10-10. It will take 5 hours.

OUTPUT SCHEMA: Return raw valid JSON matching this exact structure:
{
  "projects": [
    {
      "name": "Project Name",
      "clientName": "Client Name",
      "description": "Brief description",
      "managerId": "Valid ID from directory",
      "deadline": "YYYY-MM-DD",
      "tasks": [
        {
          "title": "Task Title",
          "description": "Brief task details",
          "assigneeId": "Valid ID from directory",
          "deadline": "YYYY-MM-DD",
          "estimatedHours": 12
        }
      ]
    }
  ]
}
Return ONLY JSON. No markdown formatting blocks like ```json. Just raw `{...}`.
"""

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent?key={api_key}"
payload = {
    "contents": [{"parts": [{"text": prompt}]}],
    "generationConfig": {
        "temperature": 0.0,
        "response_mime_type": "application/json"
    }
}
print("Calling AI...")
resp = requests.post(url, json=payload)
print(f"Status: {resp.status_code}")
try:
    print(json.dumps(resp.json(), indent=2))
except Exception as e:
    print("Response text:", resp.text)
