import pandas as pd
df=pd.read_csv('deliveries.csv')
runs_count=df.groupby("batsman")['batsman_runs'].sum().sort_values(ascending=False)
print(runs_count.head(10))