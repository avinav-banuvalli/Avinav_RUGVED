
import pandas as pd
import numpy as np

df = pd.read_csv("./data/matches.csv")


print("Q1 - Count the total number of matches conducted in 2008.")
print("Total number of matches conducted in 2008 are:", df[df["season"] == 2008].shape[0],"\n\n")

print("Q2 - Find the cities where the maximum and minimum number of matches were conducted")
counts = df["city"].value_counts()
print("City where most number of matches were conducted: ")
print(counts.idxmax(),"-",counts.max(),"matches\n")
print("City where least number of matches were conducted: ")
print(counts.idxmin(),"-",counts.min(),"matches\n\n")

print("Q3 - ")
print("Total number of matches in each city:")
print(counts,"\n\n")

#Q4
print("The toss decision taken by each team:\n")
print(df.groupby("toss_winner")["toss_decision"].value_counts(),"\n\n")


print("Q7 - Find the team which won the match by the highest and lowest number of runs.")
df_win = df[df["win_by_runs"] > 0]

win_high = df_win["win_by_runs"].max()
print("Team that won by the highest number of runs, which is", win_high, "is", df.loc[df["win_by_runs"] == win_high, "winner"].tolist()) 

win_low = df_win["win_by_runs"].min()
print("Team that won by the lowest number of runs, which is", win_low, "is", df.loc[df["win_by_runs"] == win_low, "winner"].tolist())





