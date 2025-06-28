import os
import re

README_PATH = "README.md"
SUBMISSIONS_PATH = "auto_sync_bot/submissions"

def count_problems():
    if not os.path.exists(SUBMISSIONS_PATH):
        return 0
    return len([d for d in os.listdir(SUBMISSIONS_PATH) if os.path.isdir(os.path.join(SUBMISSIONS_PATH, d))])

def update_readme(count):
    with open(README_PATH, "r") as f:
        content = f.read()

    updated = re.sub(
        r"https://img\.shields\.io/badge/Total%20Solved-\d+-blueviolet",
        f"https://img.shields.io/badge/Total%20Solved-{count}-blueviolet",
        content
    )

    with open(README_PATH, "w") as f:
        f.write(updated)

if __name__ == "__main__":
    count = count_problems()
    update_readme(count)
