import os
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

def count_solved_problems(folder_path):
    if not os.path.exists(folder_path):
        print(f"⚠️ Folder not found: {folder_path}")
        return 0
    entries = os.listdir(folder_path)
    return sum(
        os.path.isdir(os.path.join(folder_path, entry))
        for entry in entries
        if not entry.startswith(".")
    )

def create_badge(count):
    text = f"{count} LeetCode Problems Solved"

    fig, ax = plt.subplots(figsize=(6, 1.5))
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 1.5)
    ax.axis("off")

    # Pastel colors
    background_color = "#fcefee"  # pastel pink
    border_color = "#e7c8dd"      # slightly darker pastel
    text_color = "#6c4675"        # pastel purple

    # Draw rounded rectangle background
    rect = FancyBboxPatch((0, 0), 6, 1.5,
                          boxstyle="round,pad=0.3",
                          linewidth=2,
                          edgecolor=border_color,
                          facecolor=background_color)
    ax.add_patch(rect)

    ax.text(3, 0.75, text, fontsize=18, ha='center', va='center', color=text_color, weight='bold')
    plt.savefig("badge.svg", format="svg", bbox_inches='tight')

if __name__ == "__main__":
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    submissions_path = os.path.join(base_dir, "submissions")
    count = count_solved_problems(submissions_path)
    create_badge(count)
