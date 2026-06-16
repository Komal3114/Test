import pandas as pd

#df = pd.read_csv("students.csv")
df = pd.read_csv(r"C:\Users\komal\OneDrive\Documents\Desktop\Technical_OutSource_Training\Python\Day_6\students.csv")

print(df.head())
print(df.info())
print(df.describe())