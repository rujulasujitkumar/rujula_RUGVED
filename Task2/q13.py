import pandas as pd
df=pd.read_csv('matches.csv')
#self note-Combine all three umpire columns into one long list of names
umpires_comb=pd.concat([df['umpire1'],df['umpire2'],df['umpire3']])
umpire_cnt=umpires_comb.value_counts()
print(umpire_cnt.idxmax(),":",umpire_cnt.max())