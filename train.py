import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt

df = pd.read_csv("merge_final.csv")
y = df["zeroBalCode"].tolist()

X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.3)


model = RandomForestClassifier(max_depth=3)
