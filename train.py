import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("merge_final.csv")
y = df["zeroBalCode"].tolist()

X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.3)

print (len(X_train))
print (len(y_train))
print (len(X_test))
print (len(y_test))
