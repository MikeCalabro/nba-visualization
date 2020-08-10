# Creates a bar graph of NBA career point leaders for players drafted after 1995

import pandas as pd
import matplotlib.pyplot as plt

nba_clean = pd.read_csv("~/PycharmProjects/pycharm-test/nba_clean.csv")

print(nba_clean)

# Creates a list of leading all time scorers whose careers started in `96 or later
# Need to turn draft_year into an int first :p
career_point_leaders = (
      nba_clean
      .loc[nba_clean.draft_year > 1995]
      .loc[:, ['player_name', 'draft_year', 'total_points']]
      .groupby(['player_name', 'draft_year'])
      .sum()
      .sort_values(by='total_points', ascending=False)
      .iloc[0:15]
      .rename(columns={'total_points': 'career_points'})
      .reset_index()
      )

print(career_point_leaders)

# Plots the career point leaders
fig, ax = plt.subplots()
ax.grid(axis='y', alpha=0.4)
ax.bar(x=career_point_leaders.player_name, height=career_point_leaders.career_points)
ax.set_ylabel('Career Points')
ax.set_title('Career Point Leaders For Players Drafted After 1995')
# Code below tilts the x-axis names so they don't overlap
fig.autofmt_xdate()
plt.show()
