import requests
from bs4 import BeautifulSoup

url = "https://www.playstation.com/en-in"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# Title
title = soup.title.text
print(f"Title: {title}")

# H1 (safe check)
h1 = soup.find("h1")
if h1:
    print("H1:", h1.text)
else:
    print("H1 not found")

# Paragraph (safe check)
p = soup.find("p")
if p:
    print("Paragraph:", p.text)
else:
    print("Paragraph not found")

# Links
links = soup.find_all("a")

for link in links:
    print("Text:", link.text.strip())
    print("Href:", link.get("href"))