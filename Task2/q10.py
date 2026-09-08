import pandas as pd
df=pd.read_csv('matches.csv')
pom_c=df.groupby('player_of_match')['id'].count().sort_values(ascending=False)
print(pom_c.head(3))