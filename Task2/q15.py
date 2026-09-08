import pandas as pd
df1=pd.read_csv('matches.csv')
df2=pd.read_csv('deliveries.csv')
merged=df2.merge(df1[["id","season"]],left_on='match_id',right_on='id')
total_runs=merged.groupby("season")['total_runs'].sum()
print(total_runs)