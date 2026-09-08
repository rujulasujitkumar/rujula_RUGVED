import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('matches.csv')
win_=df["winner"].value_counts()
plt.bar(win_.index,win_.values,color='cyan')
plt.title("Distribution of Winning Teams")
plt.xlabel("Teams")
plt.ylabel("Number of Wins")
plt.xticks(rotation=90)
plt.show()