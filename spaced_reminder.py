# spaced_reminder.py (updated to fix deprecation warnings and a bug in logic)
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
    due = []
    for sub in subs:
        dt = datetime.fromtimestamp(sub["ts"], tz=timezone.utc).date()
        for d in REVIEW_INTERVALS:
            if today == dt + timedelta(days=d):
                due.append(sub)
                break
    return due

def send_email(subject, body):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = TO_EMAIL
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SMTP_USER, SMTP_PASS)
        smtp.send_message(msg)

if __name__ == "__main__":
    submissions = load_submissions()
    due = due_reviews(submissions)

    if not due:
        print("✅ No reviews due today.")
        exit(0)

    lines = ["You have the following LeetCode problems due for review:\n"]
    for p in due:
        reviewed_on = datetime.fromtimestamp(p['ts'], tz=timezone.utc).date()
        lines.append(f"- [{p['id']} - {p['slug']}]"
                     f"(https://leetcode.com/problems/{p['slug']}/) "
                     f"solved on {reviewed_on}")
    body = "\n".join(lines)

    send_email(
        subject=f"⏰ LeetCode Review Reminder ({len(due)} problem(s))",
        body=body
    )
    print(f"📬 Sent review reminder for {len(due)} problems.")

