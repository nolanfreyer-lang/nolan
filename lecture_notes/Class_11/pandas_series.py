import pandas as pd
import numpy as np

pd.Series()

# data = {"Name": ["Alice", "Bob", "Charlie"],
#         "Age": [25, 30, 35],
#         "City": ["SF", "LA", "NY"]
# }

# df = pd.DataFrame(data)

# df[df["Age"] > 25]

# df[df["City"] == "SF"]

# df["Age"] = df 

# df.loc[0, :]
# #df.loc[row, column]

df = pd.read_csv("students.csv")
# print(df)

# print(df["Grade"].mean())

# print(df[df["Grade"] > 85])

print(df["Major"].value_counts())

df["Pass"] = df["Grade"] > 75
print(df)