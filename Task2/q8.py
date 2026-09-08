import pandas as pd
df=pd.read_csv("matches.csv")
mean_=df['win_by_runs'].mean()
median_=df['win_by_runs'].median()
std_=df['win_by_runs'].std()
print("Mean:",mean_)
print("Median:",median_)
print("Standard Deviation:",std_)