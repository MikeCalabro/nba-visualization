# Creates a line graph of total points scored in the NBA for each team in each season since 1996/7

import pandas as pd
import matplotlib.pyplot as plt

nba_clean = pd.read_csv("~/PycharmProjects/pycharm-test/nba_clean.csv")

league_points = (nba_clean
                 .loc[:, ['team_abbreviation', 'season', 'total_points']]
                 .groupby(['season', 'team_abbreviation'])
                 .sum()
                 .reset_index()
                 )

print(league_points)

