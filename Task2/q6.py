import pandas as pd
df=pd.read_csv("matches.csv")
team_tie=df[df["result"]=="tie"]
print("teams whos result was a tie",team_tie[["season","team1","team2"]])