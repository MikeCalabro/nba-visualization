# Creates a line graph of total points scored in the NBA for each team in each season since 1996/7
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

nba_clean = pd.read_csv("~/PycharmProjects/pycharm-test/nba_clean.csv")

league_points = (nba_clean
                 .loc[:, ['team_abbreviation', 'season', 'total_points']]
                 .groupby(['season', 'team_abbreviation'])
                 .sum()
                 .reset_index()
                 )

print(league_points)

# Creates a list of every nba team that I can loop through
nba_teams = league_points['team_abbreviation'].unique()

# Honestly does not create a very interesting plot at all
# However, I got a handle for using seaborn and looping through a list to make multiple lines
for team in nba_teams[0:6]:
    team_points = league_points.total_points[league_points.team_abbreviation == team]
    sns.lineplot(league_points.season, team_points, label=team)
plt.grid(alpha=0.4)
plt.xlabel('Season')
plt.ylabel('Team Points Scored')
plt.show()
