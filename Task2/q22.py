import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('matches.csv')
toss_win=df["toss_winner"].value_counts()
plt.bar(toss_win.index,toss_win.values,color='cyan')
plt.xlabel("Toss Winners")
plt.ylabel("No.of times toss won")
plt.title("Toss Winners")
plt.xticks(rotation=90)
plt.show()
