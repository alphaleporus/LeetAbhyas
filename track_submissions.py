# track_submissions.py
import os, json, requests
from dotenv import load_dotenv

load_dotenv()
SESSION = os.getenv("LEETCODE_SESSION")
CSRF    = os.getenv("CSRF_TOKEN")
USER    = os.getenv("LEETCODE_USERNAME")  # e.g. "Alphaleporus"

HEADERS = {
    "Cookie":       f"LEETCODE_SESSION={SESSION}; csrftoken={CSRF}",
    "X-CSRFToken":  CSRF,
    "Referer":      "https://leetcode.com",
    "Content-Type": "application/json",
    "User-Agent":   "Mozilla/5.0",
}
GQL = "https://leetcode.com/graphql"

RECENT_QUERY = """
query recentAcSubmissions($username: String!) {
  recentAcSubmissionList(username: $username) {
    id
    title
    titleSlug
    timestamp
    lang
    statusDisplay
  }
}
"""

def fetch_log():
    resp = requests.post(
        GQL,
        json={"query": RECENT_QUERY, "variables": {"username": USER}},
        headers=HEADERS
    )
    resp.raise_for_status()
    lod = resp.json()["data"]["recentAcSubmissionList"]
    # keep only id, slug, title, timestamp
    return [
        {"id": sub["id"],
         "slug": sub["titleSlug"],
         "title": sub["title"],
         "ts": int(sub["timestamp"])}
        for sub in lod
    ]

def load_old(filepath="submissions_log.json"):
    if not os.path.exists(filepath):
        return []
    return json.load(open(filepath))

def merge(old, new):
    # Use id as key, preserve all new if not seen
    d = {p["id"]: p for p in old}
    for p in new:
        d[p["id"]] = p
    return sorted(d.values(), key=lambda x: x["ts"])

if __name__ == "__main__":
    log = merge(load_old(), fetch_log())
    with open("submissions_log.json", "w") as f:
        json.dump(log, f, indent=2)
    print(f"🔍 submissions_log.json updated with {len(log)} entries")
