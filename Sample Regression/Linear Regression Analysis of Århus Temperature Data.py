#--Import Required Libraries--#
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

#--Load The Dataset --#
df = pd.read_csv('GlobalLandTemperaturesByCity.csv')
df.info()

#--Select a region of interest--#
region = df[df['City']=='Århus'][['dt', 'AverageTemperature']]
region['Year'] = pd.to_datetime(region['dt']).dt.year

##--Drop any rows with Missing Values--#
region.dropna(inplace=True)
region.info()
region.head()

#--Split the Data into Training and Testing sets--#
X_train, X_test, y_train, y_test = train_test_split(region[['Year']], region['AverageTemperature'], test_size=0.8, random_state=123)
print('Training predictor variable shape:', X_train.shape)
print('Training target variable shape:', y_train.shape)
print('Testing predictor variable shape:', X_test.shape)
print('Testing target variable shape:', y_test.shape)

#--Fit a Linear Regression to the Training Data--#
lr_ = LinearRegression()
lr_.fit(X_train, y_train)

#--Making a Prediction on the Test Data--#
y_pred = lr_.predict(X_test)

#--Calculate the mean squared error of the prediction--#
mse = mean_squared_error(y_test, y_pred)
print('Mean squared error', mse)

#--Plot the prediction and the actual values--#
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.show()
