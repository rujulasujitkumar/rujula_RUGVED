import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('matches.csv')
win_=df["winner"].value_counts().head(5)
plt.bar(win_.index,win_.values,color='cyan')
plt.title("Top 5 Teams")
plt.xlabel("Teams")
plt.ylabel("Number of Wins")
plt.xticks(rotation=90)
plt.show()
