import pandas as pd
df=pd.read_csv('matches.csv')
bat_cnt=df[df['toss_decision']=='bat'].groupby('toss_winner')['id'].count()
field_cnt=df[df['toss_decision']=='field'].groupby('toss_winner')['id'].count()
print("batting:",bat_cnt)
print("\n")
print("fielding:",field_cnt)
