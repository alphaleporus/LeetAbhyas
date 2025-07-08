# spaced_reminder.py (fixed 'title' KeyError and improved formatting)
import os, json, smtplib
from datetime import datetime, timedelta, timezone
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()
SMTP_USER = os.getenv("EMAIL_USER")       # Gmail address
SMTP_PASS = os.getenv("EMAIL_APP_PASS")   # Gmail App Password
TO_EMAIL  = os.getenv("TO_EMAIL")         # Your email

# Intervals in days
REVIEW_INTERVALS = [7, 15, 30, 60, 90]
LOG_PATH = "submissions_log.json"

def load_submissions():
    return json.load(open(LOG_PATH))

def due_reviews(subs):
    today = datetime.now(timezone.utc).date()
    global today_str
    today_str = today.strftime("%B %d, %Y")
    due = []
    for sub in subs:
        dt = datetime.fromtimestamp(sub["ts"], tz=timezone.utc).date()
        for d in REVIEW_INTERVALS:
            if today == dt + timedelta(days=d):
                due.append(sub)
                break
    return due

def send_email(subject, html_body):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = TO_EMAIL
    msg.set_content("This email requires an HTML-compatible email client.")
    msg.add_alternative(html_body, subtype='html')

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SMTP_USER, SMTP_PASS)
        smtp.send_message(msg)

if __name__ == "__main__":
    submissions = load_submissions()
    due = due_reviews(submissions)

    if not due:
        print("✅ No reviews due today.")
        exit(0)

    problem_lines = "\n".join(
        f'<div class="problem">{i+1}. '
        f'<a href="https://leetcode.com/problems/{p["slug"]}/">{p.get("title", p["slug"])}</a> '
        f'— solved on {datetime.fromtimestamp(p["ts"], tz=timezone.utc).strftime("%B %d, %Y")}</div>'
        for i, p in enumerate(due)
    )

    html_body = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <style>
        body {{
          font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
          background-color: #f4f4f4;
          padding: 30px;
          color: #333;
        }}
        .container {{
          background-color: white;
          padding: 24px 32px;
          border-radius: 10px;
          max-width: 600px;
          margin: auto;
          box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}
        .title {{
          font-size: 24px;
          color: #2c3e50;
          margin-bottom: 10px;
        }}
        .subtitle {{
          font-size: 16px;
          color: #555;
          margin-bottom: 20px;
        }}
        .problem {{
          margin-bottom: 12px;
        }}
        .problem a {{
          text-decoration: none;
          color: #1e90ff;
          font-weight: 600;
        }}
        .footer {{
          margin-top: 30px;
          font-size: 13px;
          color: #999;
          text-align: center;
        }}
      </style>
    </head>
    <body>
      <div class="container">
        <div class="title">🧠 LeetCode Spaced Repetition Review</div>
        <div class="subtitle">You're scheduled for review today ({today_str}) 🎯</div>
        {problem_lines}
        <div class="footer">Keep Grinding 💪</div>
      </div>
    </body>
    </html>
    """

    send_email(
        subject=f"⏰ LeetCode Review Reminder ({len(due)} problem(s))",
        html_body=html_body
    )
    print(f"📬 Sent review reminder for {len(due)} problems.")
