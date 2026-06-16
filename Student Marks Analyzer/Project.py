import openpyxl
import pandas as pd
import matplotlib.pyplot as plt

# Create Excel Workbook
wb = openpyxl.Workbook()

ws = wb.active
ws.title = "student"

# Add Student Data
ws.append(["Name", "Math", "Science", "English", "Computer"])
ws.append(["Rahul", 85, 98, 78, 92])
ws.append(["Priya", 90, 85, 88, 95])
ws.append(["Rohan", 60, 55, 70, 65])
ws.append(["Sneha", 78, 82, 85, 80])
ws.append(["Amit", 45, 50, 55, 48])
ws.append(["Pooja", 92, 88, 90, 94])
ws.append(["Vikas", 35, 48, 38, 47])
ws.append(["Neha", 88, 92, 85, 90])

# Save Excel File
wb.save("students.xlsx")

print("Excel file created successfully!")

# Read Excel File
df = pd.read_excel("students.xlsx")

print("\nData Loaded Successfully:")
print(df)

# Calculate Average Marks
df["Average"] = df[["Math", "Science", "English", "Computer"]].mean(axis=1)

print("\nAverage Marks:")
print(df[["Name", "Average"]])

# Pass / Fail
df["Result"] = df["Average"].apply(
    lambda x: "Pass" if x >= 60 else "Fail"
)

print("\nResults:")
print(df[["Name", "Average", "Result"]])

# Topper and Lowest Scorer
topper = df.loc[df["Average"].idxmax()]
lowest = df.loc[df["Average"].idxmin()]

print(f"\nTopper: {topper['Name']} - {topper['Average']:.2f}")
print(f"Lowest: {lowest['Name']} - {lowest['Average']:.2f}")

# Class Average
print(f"Class Average: {df['Average'].mean():.2f}")

# Bar Chart
plt.figure(figsize=(10, 6))
plt.bar(df["Name"], df["Average"], color="skyblue")
plt.title("Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.axhline(y=60, color="red", linestyle="--", label="Pass Marks (60)")
plt.legend()
plt.show()

# Save Results to New Excel File
df.to_excel("results.xlsx", index=False)

print("\nResults saved successfully in 'results.xlsx'")