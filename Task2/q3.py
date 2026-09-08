import pandas as pd
df=pd.read_csv('matches.csv')
city_wise_cnt=df.groupby('city')['id'].count()
print(city_wise_cnt)