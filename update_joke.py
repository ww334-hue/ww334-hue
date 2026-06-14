import requests
import datetime

def get_tech_fact():
    try:
        url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
        response = requests.get(url)
        data = response.json()
        return data["text"]
    except:
        return "Simplicity is the soul of efficiency. — Austin Freeman"

def rebuild_readme():
    fact = get_tech_fact()
    
    # --- PART 1: TECH STACK & PROJECT STATUS PROFILE ---
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

---

💡 **Random Fact of the Day:** *{fact}*
"""
    
    # Overwrite the README.md with the brand new dashboard layout
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_readme_content)

if __name__ == "__main__":
    rebuild_readme()
