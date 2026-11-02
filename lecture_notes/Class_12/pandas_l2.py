import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

grades = pd.Series([88,92,79,93])
print(grades.mean())
print(grades.max())
print(grades.min())

sns.load_dataset