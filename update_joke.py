import requests
import re

def get_tech_fact():
    try:
        # Reliable API for short, single-line random facts
        url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
        response = requests.get(url)
        data = response.json()
        return data["text"]
    except:
        return "Simplicity is the soul of efficiency. — Austin Freeman"

def update_readme():
    fact = get_tech_fact()
    
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Wraps the single line strictly inside the hidden tags
    fact_block = f"\n\n💡 **Random Fact:** {fact}\n\n"
    
    pattern = r".*?"
    updated_content = re.sub(pattern, fact_block, content, flags=re.DOTALL)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated_content)

if __name__ == "__main__":
    update_readme()
