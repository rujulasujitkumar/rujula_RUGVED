import pandas as pd
df=pd.read_csv('matches.csv')
season_cnt=df.groupby("season")["id"].count()
print(season_cnt)