import pandas as pd

players = {
    "Players" : ["Messi","Ronaldo","Sunil Chetri"],
    "Goals" : [5,7,6]
}

df = pd.DataFrame(players)

df["Players"]
print(df["Goals"].median())