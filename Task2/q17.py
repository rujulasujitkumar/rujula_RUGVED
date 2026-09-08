import pandas as pd
df=pd.read_csv('deliveries.csv')
nonempty_dismissal=df[df['dismissal_kind'].notna()]
wickets_count=nonempty_dismissal.groupby("bowler")['dismissal_kind'].count()
print(wickets_count)