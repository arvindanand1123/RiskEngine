import os

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.metrics import confusion_matrix

import keras
import keras.backend as K
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import Embedding
from keras.layers import LSTM

X = pd.read_csv("final_zero_b.csv")
X.fillna('')
print(X.shape)

y = X['zeroBalCode']



labelencoder_X_1 = LabelEncoder()
X['origChannel'] = labelencoder_X_1.fit_transform(X['origChannel'])

labelencoder_X_2 = LabelEncoder()
X['sellerName'] = labelencoder_X_2.fit_transform(X['sellerName'])

labelencoder_X_3 = LabelEncoder()
X['firstTimeHomeBuyer'] = labelencoder_X_3.fit_transform(X['firstTimeHomeBuyer'])

labelencoder_X_4 = LabelEncoder()
X['loanPurpose'] = labelencoder_X_4.fit_transform(X['loanPurpose'])

labelencoder_X_5 = LabelEncoder()
X['propType'] = labelencoder_X_5.fit_transform(X['propType'])

labelencoder_X_6 = LabelEncoder()
X['occType'] = labelencoder_X_6.fit_transform(X['occType'])

labelencoder_X_7 = LabelEncoder()
X['prodType'] = labelencoder_X_7.fit_transform(X['prodType'])

labelencoder_X_8 = LabelEncoder()
X['reloMortIndicator'] = labelencoder_X_8.fit_transform(X['reloMortIndicator'])

# onehotencoder = OneHotEncoder(categorical_features = ['origChannel', 'sellerName', 'loanPurpose', 'propType', 'occType', 'prodType'])
# X = onehotencoder.fit_transform(X).toarray()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
X_train.fillna('')
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

print("Training data shape:", X_train.shape)
print("Test data shape:", y_train.shape)

classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(output_dim = 10, init = 'uniform', activation = 'relu',input_dim = 22))

# Adding the second hidden layer
classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))

# Compiling Neural Network
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting our model
classifier.fit(X_train, y_train, batch_size = 10, nb_epoch = 50)
classifier.save_weights("model.h5")
print("Saved model to disk")

# Predicting the Test set results
y_pred = classifier.predict(X_test)
print(y_pred[0:100])
