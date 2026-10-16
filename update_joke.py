import requests

def get_tech_fact() -> str:
    try:
        url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
        response = requests.get(url, timeout=10)
        data = response.json()
        return data.get("text", "Simplicity is the soul of efficiency. — Austin Freeman")
    except Exception:
        return "Simplicity is the soul of efficiency. — Austin Freeman"

def generate_progress_bar(completed_semesters: int, total_semesters: int = 9) -> str:
    percentage = (completed_semesters / total_semesters) * 100
    bar_length = 10
    filled_length = int(round(bar_length * completed_semesters / total_semesters))
    bar = '=' * filled_length + '-' * (bar_length - filled_length)
    return f"`[{bar}]` {percentage:.1f}%"

def rebuild_readme():
    fact = get_tech_fact()
    
    total_semesters = 9
    semesters_left = 4  # Adjust this when your semester finishes
    completed_semesters = total_semesters - semesters_left
    
    progress_display = generate_progress_bar(completed_semesters, total_semesters)
    
    new_readme_content = f"""# Hi there! 👋

Welcome to my GitHub profile. I'm an Software Engineering undergraduate student focusing on building robust software, database engineering, and automation systems.

## 🎓 Academic Journey
* 📚 **Degree Progress:** {progress_display}
* ⏳ **Timeline:** **{semesters_left} semesters remaining** (including current session) until graduation!

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

---

💡 **Random Fact of the Day:** *{fact}*
"""
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_readme_content)
    
    print("README.md successfully updated!")

if __name__ == "__main__":
    rebuild_readme()
