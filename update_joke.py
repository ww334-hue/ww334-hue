import requests
import datetime
import re

def get_tech_fact():
    try:
        url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
        response = requests.get(url)
        data = response.json()
        return data["text"]
    except:
        return "Simplicity is the soul of efficiency. — Austin Freeman"

def calculate_days_left():
    # Set a target milestone date (Year, Month, Day)
    # Example: December 18, 2026
    target_date = datetime.date(2026, 12, 18)
    today = datetime.date.today()
    
    delta = target_date - today
    return max(0, delta.days)

def rebuild_readme():
    fact = get_tech_fact()
    days_remaining = calculate_days_left()
    
    # The complete dashboard structure combining both concepts
    new_readme_content = f"""# Hi there! 👋

Welcome to my GitHub profile. I'm a developer focusing on building robust software, database engineering, and automation systems.

## 🛠️ My Tech Stack
Here are the core technologies and frameworks I work with:

| Category | Technologies |
| :--- | :--- |
| **Languages** | Python, C#, VB.Net, x86 Assembly |
| **Databases** | Relational Models, SQL, Database Normalization |
| **Tools & OS** | Git, GitHub Actions, Windows Development |

## 🚀 Current Project Status
* 🔒 **System Architecture:** Integrating secure native system gatekeepers with backend data ledgers.
* 🤖 **Automation:** Building cloud-based profile metrics and scrapers via GitHub Actions.

## 🎯 Active Targets & Goals
* ⏳ **Milestone Countdown:** **{days_remaining} days** remaining until December graduation and major deployment targets!
* 📚 **Weekly Habit:** Mastering advanced database performance optimizations and indexing configurations.

---

💡 **Random Fact of the Day:** *{fact}*
"""
    
    # Overwrite the README.md file
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_readme_content)

if __name__ == "__main__":
    rebuild_readme()
