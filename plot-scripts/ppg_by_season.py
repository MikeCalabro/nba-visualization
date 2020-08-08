# Creates a bar graph NBA season points per game leaders for each season since 1996/7

import pandas as pd
import matplotlib.pyplot as plt

nba_clean = pd.read_csv("~/PycharmProjects/pycharm-test/nba_clean.csv")


# Easier to plot if the season is a string
def string_season(row):
    row.season = str(row.season)
    return row


# Selects the name, pts per game, and assists per game, of the highest scoring player (per game) from each season
# I don't know if this is the best way to organize the command, but it was getting long
ppg_by_season = (nba_clean
                 .loc[:, ['player_name', 'season', 'pts', 'ast']]
                 .groupby(['season'])
                 .apply(lambda group: group.loc[group.pts.idxmax()])
                 .loc[:, ['player_name', 'pts', 'ast']]
                 .reset_index()
                 .apply(string_season, axis='columns')
                 )

print(ppg_by_season)

fig, ax = plt.subplots()
ax.bar(x=ppg_by_season.player_name + ' - ' + ppg_by_season.season,
       height=ppg_by_season.pts,
       color="C3")
ax.set_ylabel("Points Per Game")
ax.set_title("Highest NBA Points Per Game In Each Season Since 1996/97")
fig.autofmt_xdate()
plt.show()
