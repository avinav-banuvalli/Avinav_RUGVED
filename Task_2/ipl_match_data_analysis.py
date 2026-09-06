
import pandas as pd
import numpy as np

df = pd.read_csv("./data/matches.csv")
df_d = pd.read_csv("./data/deliveries.csv")

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

print("\nQ5 - Count the total number of normal and tied matches.")
print("Count by result type:", df["result"].value_counts())

print("\nQ6 - Find the teams where the result was a tie.")
print("The teams which were tied:", df.loc[df["result"] == "tie", ["team1", "team2"]].reset_index(drop=True))

print("\nQ7 - Find the team which won the match by the highest and lowest number of runs.")
df_win = df[df["win_by_runs"] > 0]

win_high = df_win["win_by_runs"].max()
print("Team that won by the highest number of runs, which is", win_high, "is", df.loc[df["win_by_runs"] == win_high, "winner"].unique().tolist()) 

win_low = df_win["win_by_runs"].min()
print("Team that won by the lowest number of runs, which is", win_low, "is", df.loc[df["win_by_runs"] == win_low, "winner"].unique().tolist())

print("\nQ8 - Calculate mean, median and standard deviation of win_by_runs")

# Since many rows have 0 win_by_run values, computing the mean,median and standard deviation with and without zero values

print("Computing with zero values:")
win_by_runs = df["win_by_runs"]
print("Mean of win_by_runs column:", win_by_runs.mean())
print("Median of win_by_runs column:", win_by_runs.median())
print("Standard Deviation of win_by_runs column:", win_by_runs.std())

print("\nComputing without zero values:")
win_by_runs_nonzero = df.loc[df["win_by_runs"] > 0, "win_by_runs"]
print("Mean of win_by_runs column:", win_by_runs_nonzero.mean())
print("Median of win_by_runs column:", win_by_runs_nonzero.median())
print("Standard Deviation of win_by_runs column:", win_by_runs_nonzero.std())

print("\nQ9 - Find the venue where the team won by the highest and lowest number of runs.")
df_win = df[df["win_by_runs"] > 0]

win_high = df_win["win_by_runs"].max()
print("Venue of the match where team won by highest number of runs:", df.loc[df["win_by_runs"] == win_high, "venue"].unique().tolist()) 

win_low = df_win["win_by_runs"].min()
print("Venue of the match where team won by lowest number of runs:", df.loc[df["win_by_runs"] == win_low, "venue"].unique().tolist()) 

print("\nQ10 - Find the players who have won Player of the Match more than 3 times.")
pom_value_count = df["player_of_match"].value_counts()
print("The list of players who got player of the match more than 3 times:", pom_value_count[pom_value_count > 3].to_string())

print("\nQ11 - Find all deliveries where the batsman scored a six")
print("All deliveries where batsman scored a six is:", df_d[df_d["batsman_runs"] == 6].reset_index(drop=True).to_string())










