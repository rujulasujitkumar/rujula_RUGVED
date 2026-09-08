import pandas as pd
df = pd.read_csv('matches.csv')
city_count=df.groupby("city")['id'].count()
max_no=city_count.max()
max_city=city_count.idxmax()
min_no=city_count.min()
min_city=city_count.idxmin()
print("Max matches:",max_city,":",max_no)
print("Min matches:",min_city,":",min_no)