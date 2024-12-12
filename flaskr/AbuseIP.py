# imports
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Saves the graphs to the Charts file
if not os.path.exists("Charts"):
    os.mkdir("Charts")

# Reading the .csv file
data = pd.read_csv( filepath_or_buffer= 'WLD_RTP_details_2023-10-02.csv', index_col=0, parse_dates=True)

country = ["june"]

df = pd.DataFrame(data)
