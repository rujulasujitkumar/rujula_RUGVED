import pandas as pd
df=pd.read_csv('deliveries.csv')
run_total=df.groupby("batsman")['batsman_runs'].sum()
batsman_out=df[df['player_dismissed'].notna()].groupby("player_dismissed")["player_dismissed"].count()
batting_avg=(run_total/batsman_out).dropna().sort_values(ascending=False)
print(batting_avg.head(10))