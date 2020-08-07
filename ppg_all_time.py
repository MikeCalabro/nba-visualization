# Creates a bar graph of the highest NBA season points per game leaders since 1996/7

import pandas as pd
import matplotlib.pyplot as plt

nba_clean = pd.read_csv("nba_clean.csv")


# Select [all rows, [some columns]].sort by points_scored.print the top x (15) columns
print(nba_clean.loc[:, ['player_name', 'season', 'pts']].sort_values(by='pts', ascending=False).iloc[0:15])
