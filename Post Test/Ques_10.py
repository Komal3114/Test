"""
Q10. API Task: (5 Marks) 
• Call this API: https://jsonplaceholder.typicode.com/users 
• Check status code == 200 before processing 
• Print Name, Email, Phone of ALL users 
• Save all user data to 'users.json' 
• Print total number of users fetched 
• Handle all exceptions properly
"""

import requests
import json

try:
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)

    if response.status_code == 200:
        users = response.json()

        print("User Details:")
        print("-" * 40)

        for user in users:
            print("Name :", user["name"])
            print("Email:", user["email"])
            print("Phone:", user["phone"])
            print("-" * 40)

        
        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)

        print("Data saved to users.json")

        
        print("Total Number of Users Fetched:", len(users))

    else:
        print("Failed to fetch data.")
        print("Status Code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Request Error:", e)

except json.JSONDecodeError:
    print("Error decoding JSON data.")

except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    print("API operation completed.")