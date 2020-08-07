# Creates a bar graph NBA season points per game leaders for each season since 1996/7

import pandas as pd
import matplotlib.pyplot as plt

nba_clean = pd.read_csv("nba_clean.csv")

# Selects the name, pts per game, and assists per game, of the highest scoring player (per game) from each season
# I don't know if this is the best way to organize the command, but it was getting long
print(nba_clean
      .loc[:, ['player_name', 'season', 'pts', 'ast']]
      .groupby(['season'])
      .apply(lambda group: group.loc[group.pts.idxmax()])
      .set_index('season')
      )
