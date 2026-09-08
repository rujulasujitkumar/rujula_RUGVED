import pandas as pd
df1=pd.read_csv('matches.csv')
df2=pd.read_csv('deliveries.csv')

match_runs=df2.groupby('match_id')['total_runs'].sum().reset_index()
merged=match_runs.merge(df1[['id', 'venue']],left_on='match_id',right_on='id')
avg_runs=merged.groupby('venue')['total_runs'].mean()
print(avg_runs)