<div align="center">

  <h1>LeetAbhyas 🧠</h1>
  <img src="https://raw.githubusercontent.com/gaurav15042004/LeetAbhyas/output/badge.svg" alt="Submissions Badge">

  <p>LeetAbhyas is a fully automated and aesthetically organised repository that syncs all my accepted LeetCode submissions. Each problem is neatly version-controlled and browsable — automatically updated every day using GitHub Actions and a custom Python bot.</p>

  <blockquote><strong>🎯 Encouraging consistency, mastery of DSA, and long-term recall.</strong></blockquote>

</div>

---

## 🔧 Tech Stack

- 🐍 Python
- 🔁 GitHub Actions
- ⚙️ leetcode-export CLI
- ☁️ Git & GitHub
- 📚 Java for DSA

---

## 📈 Badge System

The dynamic badge above reflects the total number of accepted submissions. It updates automatically after each daily sync using a custom badge renderer.

---

## ⚙️ Automations at Work

- 🕰 **Daily Sync**: GitHub Action runs at 6 AM IST to fetch new accepted problems.
- 📁 **Structured Storage**: Problems saved by ID and slug.
- ✅ **Accepted-Only**: Filters out rejected or duplicate submissions.
- 🧠 **Spaced Repetition Reminder**: Reinforces learning through timed revision emails.

---

## 🧠 Spaced Repetition System

Maximize retention with science-backed revision intervals:

<div align="center">

| Review Day | Reminder Type      |
|------------|--------------------|
| Day 7      | First recall       |
| Day 15     | Reinforcement      |
| Day 30     | Medium-term memory |
| Day 60     | Long-term memory   |
| Day 90     | Final reinforcement|

</div>

- 📬 Emails triggered automatically using GitHub Actions.
- 🔐 Credentials like `EMAIL_USER`, `TO_EMAIL` managed with GitHub Secrets.
- 🧾 Powered by a Python script (`spaced_reminder.py`) that checks your submissions log.

---

## 🛠 Getting Started (Fork & Use)

1. **Fork this Repository**
2. Navigate to: `Settings → Secrets and Variables → Actions`
3. Add the following secrets:
   - `LEETCODE_SESSION`: your LeetCode session cookie
   - `LEETCODE_USERNAME`: your LeetCode username
   - `EMAIL_USER`: your sender email (Gmail recommended)
   - `EMAIL_APP_PASS`: your app password (not main Gmail password)
   - `TO_EMAIL`: where to receive reminders
4. Enable GitHub Actions
5. Sit back and watch the automation 🎬

---

## 🙌 About Me

<div align="center">

**Made with 💻 + ❤️ by Gaurav Sharma**

📧 gaurav15042004@gmail.com  
🎓 B.Tech Computer Engineering @ BVCOE Pune  
🔗 [@gaurav15042004 on GitHub](https://github.com/gaurav15042004)

</div>

---

<div align="center">
  “Consistency compounds.” – Naval Ravikant
</div>
