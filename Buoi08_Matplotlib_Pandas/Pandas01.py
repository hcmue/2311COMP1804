import pandas as pd
import numpy as np

# Report
# Data storytelling

data = np.array(['a','b','c','d'])
s = pd.Series(data, index=[100,101,102,103])
print(s)