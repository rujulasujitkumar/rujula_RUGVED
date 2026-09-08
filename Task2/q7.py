import pandas as pd
df=pd.read_csv("matches.csv")
max_=df.loc[df['win_by_runs'].idxmax()]
runs_=df[df['win_by_runs']>0]
min_=runs_.loc[runs_['win_by_runs'].idxmin()]
print("Team:",max_['winner'],"won by",max_['win_by_runs'])
print("Team:",min_['winner'],"won by",min_['win_by_runs'])


