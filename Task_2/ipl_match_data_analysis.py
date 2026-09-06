
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

df_win_high_idx = df_win["win_by_runs"].idxmax()
print("Team that won by the highest number of runs:", df.loc[df_win_high_idx, "winner"],"-", df.loc[df_win_high_idx, "win_by_runs"], "runs") 

df_win_low_idx = df_win["win_by_runs"].idxmin()
print("Team that won by the lowest number of runs:",df.loc[df_win_low_idx, "winner"],"-", df.loc[df_win_low_idx, "win_by_runs"], "runs\n")



