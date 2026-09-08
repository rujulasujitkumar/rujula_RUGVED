import pandas as pd
df=pd.read_csv('deliveries.csv')
score_six=df[df['batsman_runs']==6]
print("all deliveries of when the batsman scored a six:",score_six)