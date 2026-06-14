import requests

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
    
    # We define the entire layout right here in the script
    new_readme_content = f"""# Hi there! 👋

Welcome to my GitHub profile.

## About Me
I am an IT student working on automation projects.

💡 **Random Fact:** {fact}

## My Projects
- Project 1
- Project 2
"""
    
    # This completely overwrites the old file with the clean layout
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_readme_content)

if __name__ == "__main__":
    rebuild_readme()
