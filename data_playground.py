import pandas as pd
import numpy as np

# Code below allows me to view entire table when I print it
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 30)

# nba_data.csv downloaded from Kaggle
nba = pd.read_csv("nba_data.csv", index_col=0)

print(nba)
