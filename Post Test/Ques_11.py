"""
Q11. Web Scraping Task: (5 Marks) 
• Scrape this website: http://quotes.toscrape.com 
• Get all quotes and authors 
• Print only quotes by 'Albert Einstein' 
• Save ALL quotes to 'quotes.json' 
• Print total number of quotes scraped
"""

import requests
from bs4 import BeautifulSoup
import json

try:
    url = "http://quotes.toscrape.com"

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("span", class_="text")
        authors = soup.find_all("small", class_="author")

        all_quotes = []

        print("Albert Einstein Quotes:")
        print("-" * 50)

        
        for quote, author in zip(quotes, authors):
            quote_text = quote.text
            author_name = author.text

            all_quotes.append({
                "quote": quote_text,
                "author": author_name
            })

            
            if author_name == "Albert Einstein":
                print(quote_text)

        
        with open("quotes.json", "w") as file:
            json.dump(all_quotes, file, indent=4)

        print("\nAll quotes saved to quotes.json")

        print("Total Quotes Scraped:", len(all_quotes))

    else:
        print("Failed to access website.")
        print("Status Code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Request Error:", e)

except Exception as e:
    print("Error:", e)

finally:
    print("Scraping operation completed.")