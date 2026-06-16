data = []
for quote, author in zip(quotes, authors):
    data.append({
        "quote": quote.text,
        "author": author.text
    })

with open("quotes.json", "w") as f:
    json.dump(data, f , index=4)

print("Data saved to quotes.json!")