import pandas as pd
import numpy as np
import glob
import re

next_day = glob.glob('data_clean/aemo_public_next_day/*.CSV')

print(next_day)

read = pd.read_csv(next_day[0])

print(read.head())