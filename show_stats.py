#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

# For better resolution graph
plt.rcParams['figure.dpi'] = 120

# The idea is to use pandas to obtain a data frame object from data.csv
# file and use matplotlib to plot the graph of the available data, plot
# all if less than 5 else plot the last five
# P.S. would love to make it interactive.😉
pd_stat = pd.read_csv("data.csv")

pd_stat.plot()
plt.show()
