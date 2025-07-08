# test.py
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("EMAIL_USER")
PASS = os.getenv("EMAIL_APP_PASS")

print(f"Email: {EMAIL}")
print(f"Password is None: {PASS is None}")

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL, PASS)
        print("✅ Login successful!")
except Exception as e:
    print(f"❌ Login failed: {e}")
