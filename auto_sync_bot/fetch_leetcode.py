# fetch_leetcode.py (updated with timestamp clamp)
import os, json, requests, time
from dotenv import load_dotenv

load_dotenv()
COOKIES_HEADER = os.getenv("LEETCODE_COOKIES")
USER    = os.getenv("LEETCODE_USERNAME")  # e.g. "Alphaleporus"

HEADERS = {
    "cookie":        COOKIES_HEADER,
    "content-type":  "application/json",
    "x-requested-with": "XMLHttpRequest",
    "origin":        "https://leetcode.com",
    "referer":       "https://leetcode.com",
    "user-agent":    "Mozilla/5.0",
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
    now_ts = int(time.time())  # Clamp to current time
    return [
        {
            "id": sub["id"],
            "slug": sub["titleSlug"],
            "title": sub["title"],
            "ts": min(int(sub["timestamp"]), now_ts)
        }
        for sub in lod
    ]

def load_old(filepath="submissions_log.json"):
    if not os.path.exists(filepath):
        return []
    return json.load(open(filepath))

def merge(old, new):
    now_ts = int(time.time())
    d = {p["id"]: p for p in old}
    for p in new:
        p["ts"] = min(p["ts"], now_ts)
        d[p["id"]] = p
    return sorted(d.values(), key=lambda x: x["ts"])

if __name__ == "__main__":
    log = merge(load_old(), fetch_log())
    with open("submissions_log.json", "w") as f:
        json.dump(log, f, indent=2)
    print(f"🔍 submissions_log.json updated with {len(log)} entries")
