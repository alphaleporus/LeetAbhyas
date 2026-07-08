import os
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

def count_solved_problems(folder_path):
    p = Path(folder_path)
    if not p.exists():
        print(f"⚠️ Folder not found: {folder_path}")
        return 0

    solved_slugs = set()
    for f in p.iterdir():
        if f.name.startswith(".") or not f.is_file():
            continue
        # "two-sum.py" -> "two-sum"
        solved_slugs.add(f.stem)

    return len(solved_slugs)

def create_badge(count):
    text = f"{count} LeetCode Problems Solved"
    fig, ax = plt.subplots(figsize=(6, 1.5))
    ax.set_xlim(0, 6); ax.set_ylim(0, 1.5); ax.axis("off")
    rect = FancyBboxPatch((0, 0), 6, 1.5, boxstyle="round,pad=0.3",
                          linewidth=2, edgecolor="#e7c8dd", facecolor="#fcefee")
    ax.add_patch(rect)
    ax.text(3, 0.75, text, fontsize=18, ha="center", va="center",
            color="#6c4675", weight="bold")
    plt.savefig("badge.svg", format="svg", bbox_inches="tight")

if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    submissions_path = os.path.join(base_dir, "submissions")
    count = count_solved_problems(submissions_path)
    print(f"✅ Counted {count} solved problems from {submissions_path}")
    create_badge(count)
