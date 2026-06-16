import matplotlib.pyplot as plt
import numpy as np

players = ["Ronaldo","Messi","Mbappe","Haaland","Neymar.jr"]
goals = [5,7,6,4,5]

plt.plot(players,goals)
plt.xlabel("Players")
plt.ylabel("Goals")
plt.show()

plt.pie([45,34,55],labels=["messi","mane","neil"])
plt.show()