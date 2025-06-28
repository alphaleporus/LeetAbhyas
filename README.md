<h1 align="center">LeetAbhyas 🧠</h1>


<p align="center">
  <img src="https://raw.githubusercontent.com/gaurav15042004/LeetAbhyas/output/badge.svg" alt="Solved Problems Badge" width="300"/>
  <br>
  <i>Automated LeetCode sync for consistent DSA mastery</i>
</p>

---

## 🚀 Overview
LeetAbhyas automates the process of fetching and storing every accepted LeetCode solution. Each day, a GitHub Actions workflow runs a Python script to retrieve your latest accepted problems (via `leetcode-export`), generates a vibrant pastel badge showing your total solved count, and commits the updates to this repository.

**Why LeetAbhyas?**
- 💡 Build a searchable, version-controlled vault of your solutions
- 🔄 Ensure disciplined daily syncing without manual overhead
- 🎯 Encourage consistent practice and spaced revision

---

## ✨ Features

- **Auto-Sync**: Fetches accepted submissions daily using GitHub Actions
- **Dynamic Badge**: Generates a pastel-themed SVG badge with your total solved count
- **Organized Storage**: Each problem saved under `auto_sync_bot/submissions/` by ID and slug
- **Custom Notes**: Markdown stubs for personal explanations or insights
- **Extensible**: Easy to fork and adapt for your own LeetCode profile

---

## 🛠️ Tech Stack

- **Python** for scripting and badge creation (`matplotlib`)
- **leetcode-export** CLI for robust submission retrieval
- **GitHub Actions** for automation (sync + badge)
- **Git & GitHub** for version control and hosting

---

## 🚀 Getting Started

1. **Fork** this repository to your GitHub account.
2. **Add Secrets** in your fork:
   - `LEETCODE_COOKIES`: Your full browser Cookie header from LeetCode
   - `LEETCODE_USERNAME`: Your LeetCode username (e.g., `Alphaleporus`)
3. **Enable Actions** and confirm workflows are active.
4. **Watch Your Repo**: Solutions and badge updates automatically each day.

---

## ⚙️ Customization

- **Adjust Schedule**: Modify `cron` in `.github/workflows/*.yml` for a different sync time.
- **Styling**: Tweak pastel colors or layout in `update_readme_badge.py`.
- **Notes Template**: Enhance Markdown stubs under `submissions/` for deeper insights.

---

## 📬 Spaced Revision (Coming Soon)
Integrate email/SMS reminders for revisiting problems at 7, 15, 30, 60, and 90 days using a Python-based notification bot.

---

## 🙌 Author

**Gaurav Sharma**  
B.Tech CSE @ BVCOE Pune  
✉️ gaurav15042004@gmail.com  
🐦 [@gaurav15042004](https://github.com/gaurav15042004)

---


