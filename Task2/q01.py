import pandas as pd
df=pd.read_csv('matches.csv')
m=df[df["season"] == 2008]
print("matches conducted in 2008:",m["id"].count())