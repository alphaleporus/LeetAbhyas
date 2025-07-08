<div align="center">

  <h1 style="font-size: 3em; color: #4CAF50;">LeetAbhyas 🧠</h1>
  <img src="https://raw.githubusercontent.com/gaurav15042004/LeetAbhyas/output/badge.svg" alt="Submissions Badge" style="margin: 20px 0;">

  <p style="font-size: 1.1em; max-width: 600px;">
    <strong>LeetAbhyas</strong> is a fully automated and beautifully structured repository that tracks all my <em>accepted</em> LeetCode submissions and delivers smart, spaced repetition reminders — directly to your inbox.
  </p>

  <blockquote><strong>🎯 Designed for consistency, DSA mastery, and long-term retention.</strong></blockquote>

</div>

---

## 🌐 Tech Stack

<div align="center">

| 🧩 Stack             | 🔍 Purpose                                    |
|----------------------|-----------------------------------------------|
| 🐍 Python            | Core scripting (fetch, sync, reminder)        |
| 🔁 GitHub Actions    | Automation for syncing and email dispatch     |
| ⚙️ leetcode-export    | CLI for fetching accepted submissions         |
| ✉️ Gmail SMTP        | Sends rich HTML reminder emails               |
| 📚 Java              | Primary DSA language                          |
| ☁️ Git + GitHub      | Version control and remote hosting            |

</div>

---

## 📊 Dynamic Badge

The badge above shows the live count of accepted LeetCode submissions, auto-updated after each sync. Rendered via a custom GitHub Actions workflow.

---

## 🤖 Automation Flow

![Automation Flow](Mermaid%20AI%20Diagram%20Jul%208%202025.svg)


---

## 🧠 Spaced Repetition Logic

<div align="center">

| 📅 Review Day | 🧪 Type               |
|---------------|-----------------------|
| Day 7         | First recall          |
| Day 15        | Reinforcement         |
| Day 30        | Medium-term memory    |
| Day 60        | Long-term memory      |
| Day 90        | Final reinforcement   |

</div>

- ✅ Python script: `spaced_reminder.py`
- 🧾 Tracks from `submissions_log.json`
- 🎨 Sends polished HTML emails with direct problem links
- 🔐 Secured using Gmail App Password

---

## 🚀 Get Started (Fork & Run)

> Clone the power. Build your revision muscle.

1. **Fork the Repository**
2. Navigate to `Settings → Secrets → Actions`
3. Add the following secrets:
   - `LEETCODE_COOKIES`: Your full LeetCode cookie string
   - `LEETCODE_USERNAME`: Your LeetCode handle
   - `EMAIL_USER`: Sender Gmail address
   - `EMAIL_APP_PASS`: Gmail app-specific password
   - `TO_EMAIL`: Destination email address
4. Enable GitHub Actions
5. 💥 Done! Watch the automation work its magic

---

## ✨ Showcase Snapshot

![sample-email](https://raw.githubusercontent.com/gaurav15042004/LeetAbhyas/assets/sample-email.png)

*Above: Sample spaced repetition HTML email (auto-generated)*

---

## 👨‍💻 About the Creator

<div align="center">

**Crafted with ❤️ and caffeine by Gaurav Sharma**

📧 gaurav15042004@gmail.com  
🎓 B.Tech Computer Engineering @ BVCOE Pune  
🔗 [@gaurav15042004 on GitHub](https://github.com/gaurav15042004)

</div>

---

<div align="center">
  <em>“Consistency compounds.” – Naval Ravikant</em>
</div>
