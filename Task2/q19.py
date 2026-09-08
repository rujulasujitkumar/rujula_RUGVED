import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('matches.csv')
bat_count=df[df['toss_decision']=='bat'].groupby('season')['id'].count()
field_count=df[df['toss_decision']=='field'].groupby('season')['id'].count()
plt.bar(bat_count.index,bat_count.values,color='cyan',label='Bat')
plt.scatter(field_count.index,field_count.values,color='red',s=80,label='Field')
plt.xlabel("Season")
plt.ylabel("No. of matches")
plt.title('Toss decision across all seasons')
plt.legend()
plt.show()