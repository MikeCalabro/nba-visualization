import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# nba_data.csv downloaded from Kaggle
nba = pd.read_csv("nba_data.csv", index_col=0)

# Code below allows me to view entire table when I print it (in PyCharm IDE)
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 30)

# Shows the head and tail of the data in PyCharm
print(nba)


# THE CODE BELOW IS FOR THE PURPOSE OF CLEANING THE DATA
#
# Function to fix the season column to be a single year int
# For each row, the season column now = only the first four digits, +1 ('2018/19' -> 2018), (2018 -> 2019)
def fix_season(row):
    row.season = int(row.season[0:4]) + 1
    return row


# Applies the function above to the nba data frame
nba = nba.apply(fix_season, axis='columns')

# Adding a total_points for the season column
nba['total_points'] = 0


def total_points(row):
    row.total_points = round(row.pts * row.gp)
    return row


nba = nba.apply(total_points, axis='columns')


# Turning draft_year into an int instead of a char
# Changing "Undrafted" Years into 0's
def draft_year_int(row):
    if row.draft_year != "Undrafted":
        row.draft_year = int(row.draft_year)
    else:
        row.draft_year = 0
    return row


nba = nba.apply(draft_year_int, axis='columns')

print(nba)

# Makes a clean csv file to be used for visualizations
nba.to_csv(path_or_buf="nba_clean.csv", index=False)

# CLEANING DONE
# Now we can explore
# Select [all rows, [some columns]].sort by points_scored.print the top x (15) columns
print(nba.loc[:, ['player_name', 'season', 'pts']].sort_values(by='pts', ascending=False).iloc[0:15])

# Selects the name, pts per game, and assists per game, of the highest scoring player (per game) from each season
# I don't know if this is the best way to organize the command, but it was getting long
print(nba
      .loc[:, ['player_name', 'season', 'pts', 'ast']]
      .groupby(['season'])
      .apply(lambda group: group.loc[group.pts.idxmax()])
      .set_index('season')
      )
