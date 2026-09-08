import pandas as pd
df=pd.read_csv("matches.csv")
match_n=df[df["result"]=="normal"]
match_t=df[df["result"]=="tie"]
print("normal matches:",match_n["id"].count())
print("tied matches:",match_t["id"].count())
