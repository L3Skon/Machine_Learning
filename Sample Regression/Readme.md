# Global Temperature Analysis

## Introduction

This is a simple analysis of global temperature data using Python. In this project, we will be analyzing the temperature data for the city of Århus.

## Data

We will be using the Global Land Temperatures By City dataset which can be downloaded from Kaggle. The dataset contains 8 columns and over 8 million rows of temperature data collected from various cities around the world since 1743.

## Libraries

We will be using the following libraries:

- pandas
- numpy
- scikit-learn
- matplotlib

## Methodology

1. Load the dataset
2. Select the region of interest (city of Århus)
3. Drop any rows with missing values
4. Split the data into training and testing sets
5. Fit a linear regression model to the training data
6. Make a prediction on the test data using the fitted model
7. Calculate the mean squared error of the prediction
8. Plot the predicted values against the actual values

## Results

After analyzing the temperature data for the city of Århus, we were able to fit a linear regression model to the data and make predictions on the test set. The mean squared error of the prediction was calculated to be 2.0065, indicating that the model was able to make fairly accurate predictions.

## Conclusion

In this project, we were able to analyze temperature data for the city of Århus and build a simple linear regression model to make predictions on the test set. This analysis can be expanded upon by incorporating additional features or by analyzing temperature data for other cities around the world.

