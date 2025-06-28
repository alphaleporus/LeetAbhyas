import os
import json
import requests
from dotenv import load_dotenv

# ─── Load .env ────────────────────────────────────────────────────────────────
load_dotenv()
LEETCODE_SESSION = os.getenv("LEETCODE_SESSION")
CSRF_TOKEN       = os.getenv("CSRF_TOKEN")
USERNAME         = "Alphaleporus"   # ← your handle

# ─── Endpoints ───────────────────────────────────────────────────────────────
GRAPHQL_URL = "https://leetcode.com/graphql"
DETAIL_API  = "https://leetcode.com/api/submissions/detail/{id}/"

# ─── Headers (with both cookies) ─────────────────────────────────────────────
HEADERS = {
    "Cookie":       f"LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={CSRF_TOKEN}",
    "X-CSRFToken":  CSRF_TOKEN,
    "Referer":      "https://leetcode.com",
    "User-Agent":   "Mozilla/5.0",
    "Accept":       "application/json",
}

# ─── Query recent AC submissions (to get IDs) ────────────────────────────────
RECENT_SUBS_QUERY = """
query recentAcSubmissions($username: String!) {
  recentAcSubmissionList(username: $username) {
    id
    title
    titleSlug
    lang
    statusDisplay
  }
}
"""

def fetch_recent_metadata():
    payload = {"query": RECENT_SUBS_QUERY, "variables": {"username": USERNAME}}
    r = requests.post(GRAPHQL_URL, json=payload, headers=HEADERS)
    r.raise_for_status()
    return r.json()["data"]["recentAcSubmissionList"]

def fetch_code_via_api(submission_id: int) -> str | None:
    url = DETAIL_API.format(id=submission_id)
    r = requests.get(url, headers=HEADERS)
    if r.status_code != 200:
        print(f"⚠️ API detail failed for {submission_id}: {r.status_code}")
        return None
    data = r.json().get("submissionDetail") or r.json()
    return data.get("code")

def fetch_and_save():
    subs = fetch_recent_metadata()
    print(f"📥 Fetched {len(subs)} submissions")

    save_dir = os.path.join("auto_sync_bot", "submissions")
    os.makedirs(save_dir, exist_ok=True)

    for sub in subs:
        sid    = sub["id"]
        title  = sub["title"]
        safe   = title.replace(" ", "_")
        lang   = sub["lang"]
        ext    = "java" if "Java" in lang else "py"
        path   = os.path.join(save_dir, f"{safe}.{ext}")

        if os.path.exists(path):
            continue

        code = fetch_code_via_api(sid)
        if not code:
            continue

        with open(path, "w", encoding="utf-8") as f:
            f.write(f"// {title} [{lang}]\n\n{code}")
        print(f"✅ Saved: {path}")

if __name__ == "__main__":
    fetch_and_save()
