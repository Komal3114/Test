"""
Create a program:

1. Scrape this website:
   http://quotes.toscrape.com

2. Find quotes by 
   "Albert Einstein" only

3. Print like this:

Einstein Quotes:
-----------------
1. "The world as we have..."
2. "Any fool can know..."

# Author check karo
if author.text == "Albert Einstein":
    # print karo
"""

import requests
from bs4 import BeautifulSoup

base_url = "http://quotes.toscrape.com"
page = "/page/1/"

einstein_quotes = []
count = 1

while page:
    url = base_url + page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text

        # Author check karo
        if author == "Albert Einstein":
            einstein_quotes.append(text)

    # next page find karo
    next_btn = soup.find("li", class_="next")
    page = next_btn.a["href"] if next_btn else None

# Output format
print("Einstein Quotes:")
print("-----------------")

for i, q in enumerate(einstein_quotes, start=1):
    print(f"{i}. {q}")