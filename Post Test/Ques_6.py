"""
Q6. List & Tuple Operations: (4 Marks) 
• Create a list of 8 city names 
• Print first 4 cities 
• Print last 4 cities 
• Add a new city at end 
• Remove the first city 
• Convert list to tuple and print
"""

cities = ["Bhopal", "Indore", "Jabalpur", "Gwalior", "Ujjain", "Sagar", "Reva", "Satna"]

print("First 4 Cities : ",cities[:4])

print("Last 4 Cities : ",cities[-4:])

cities.append("Delhi")
print("After Adding New City:", cities)

cities.pop(0)
print("After Removing First City :",cities)

city_tuple = tuple(cities)
print("Tuple : ", city_tuple)