
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

print("\nQ12 - Compute the average runs scored in matches in all the venues.")
runs_per_match = df_d.groupby("match_id")["total_runs"].sum().reset_index()
runs_per_match = runs_per_match.merge(df[["id", "venue"]], left_on = "match_id", right_on = "id")
print("The average runs scored in matches at all the venues:",runs_per_match.groupby("venue")["total_runs"].mean())

print("\nQ13 - Find the umpires who umpired the maximum number of times.")
umps = pd.concat([df["umpire1"], df["umpire2"], df["umpire3"]]).value_counts()
print(umps.idxmax(),"umpired the most")
print("Umpires who umpired the most:\n", umps.head(5))

print("\nQ14 - Find the total number of matches played in each season.")
print("Total number of matches played in each season are:",df["season"].value_counts().sort_index())

print("\nQ15 - Find total runs scored in each season")
runs_per_match = df_d.groupby("match_id")["total_runs"].sum().reset_index()
runs_per_match = runs_per_match.merge(df[["id", "season"]], left_on = "match_id", right_on = "id")
print("The total runs scored in each season:\n",runs_per_match.groupby("season")["total_runs"].sum())

print("\nQ16 - Calculate total number of runs scored by each batsman and display top 10")
top_10_runs_scorres = df_d.groupby("batsman")["batsman_runs"].sum().sort_values(ascending=False).head(10)
print("Top 10 run scorres are:\n", top_10_runs_scorres)

print("\nQ17 - Compute the total number of wickets taken by each bowler")
not_bowler_credit = {"hit wicket","retired hurt","runout","stumped","obstructing the field"}
bowler_wickets = df_d[df_d["player_dismissed"].notna() & ~df_d["dismissal_kind"].isin(not_bowler_credit)]
per_bowler_wickets = bowler_wickets.groupby("bowler").size().sort_values(ascending = False)
print("Total number of wickets taken by each bowler:\n",per_bowler_wickets.to_string())

print("\nQ18 - Compute batting averages and display top 10.")
runs = df_d.groupby("batsman")["batsman_runs"].sum()
dismissals = df_d["player_dismissed"].value_counts()
avg = (runs/dismissals)
print("Top 10 batting averages:", avg.sort_values(ascending = False).head(10))

print("\nQ19 - Visualize toss decisions across all seasons")

toss_by_season = df.groupby(["season","toss_decision"]).size().unstack()
toss_by_season.plot(kind="bar", stacked = True)
plt.title('Toss decisions across seasons')
plt.xlabel('Season')
plt.ylabel('Number of matches')
plt.legend(title='Decision')
plt.show()

print("\nQ20 - Visualize Total Matches vs Winning Matches vs Win Rate for all teams.")
team_played = pd.concat([df["team1"], df["team2"]]).value_counts()
team_wins = df["winner"].value_counts()

team_summary = pd.DataFrame({"played":team_played, "won":team_wins}).fillna(0)
team_summary["win_rate"] = (team_summary["won"] / team_summary["played"] * 100)
team_summary = team_summary.sort_values("win_rate", ascending = False)
print(team_summary)

fig, ax1 = plt.subplots(figsize=(12, 6))

team_summary[["played","won"]].plot(kind="bar", ax=ax1, color=["#bbb", "#4c9"])
ax1.set_ylabel("Matches")
ax2 = ax1.twinx()
ax2.plot(range(len(team_summary)),team_summary["win_rate"], "o-",color="crimson", label="win rate %")
ax2.set_ylabel("Win rate (%)")

ax1.set_title("Total vs Won vs Win Rate by team")
fig.tight_layout()
plt.show()

print("\nQ21 - Find the distribution of the teams who won the matches")
team_wins = df["winner"].value_counts()

team_wins.plot(kind="bar",figsize=(10,5))
plt.title('Distribution of match winning teams')
plt.xlabel('Team')
plt.ylabel('Matches won')
plt.xticks(rotation=60, ha='right')
plt.tight_layout()
plt.show()

print("\nQ22 - Visualize the toss outcomes of all teams.")

toss_wins = df["toss_winner"].value_counts()

toss_wins.plot(kind="bar",figsize=(10,5))
plt.title('Toss wins per team')
plt.xlabel('Team')
plt.ylabel('Toss wins')
plt.xticks(rotation=60, ha='right')
plt.tight_layout()
plt.show()

print("\nQ23 - Visualize the top 5 teams with the most wins across all seasons.")

team_wins = df["winner"].value_counts().head(5)

team_wins.plot(kind="bar",figsize=(10,5))
plt.title('Top 5 teams by most wins')
plt.xlabel('Team')
plt.ylabel('Matches won')
plt.xticks(rotation=60, ha='right')
plt.tight_layout()
plt.show()




























