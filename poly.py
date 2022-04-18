import numpy as np
import pandas as pd
import matplotlib.pyplot as pt

df = pd.read_csv('/data/Real estate.csv')
df = df.drop_duplicates(keep="first")
