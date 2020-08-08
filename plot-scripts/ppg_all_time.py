# Creates a bar graph of the highest NBA season points per game leaders since 1996/7

import pandas as pd
import matplotlib.pyplot as plt

nba_clean = pd.read_csv("~/PycharmProjects/pycharm-test/nba_clean.csv")


# Easier to plot if the season is a string
def string_season(row):
    row.season = str(row.season)
    return row


# Select [all rows, [some columns]].sort by points_scored.print the top x (15) columns
ppg_all_time = (nba_clean
                .loc[:, ['player_name', 'season', 'pts']]
                .sort_values(by='pts', ascending=False)
                .iloc[0:15]
                .apply(string_season, axis='columns')
                )

print(ppg_all_time)

fig, ax = plt.subplots()
ax.bar(x=ppg_all_time.player_name + ' - ' + ppg_all_time.season,
       height=ppg_all_time.pts,
       color="C9")
ax.set_ylabel("Points Per Game")
ax.set_title("Highest NBA Season Points Per Game Since 1996/97")
fig.autofmt_xdate()
plt.show()
