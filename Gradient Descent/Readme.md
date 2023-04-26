# Binary Classification using Gradient Descent 

## Introduction 

This code implements binary classification using the Gradient Descent algorithm. The purpose of the code is to predict whether a given set of features belongs to class 0 or class 1.

## Usage 

1. Define the input features and target outputs as numpy arrays.
2. Initialize the weights and bias as numpy arrays/scalars respectively.
3. Define the number of epochs and the learning rate.
4. Call the gradient_descent() function inside nested for loops that iterate over the epochs and the features respectively.
5. Calculate the loss by calling the predict() and cross_entropy() functions inside the epoch loop.
6. Append the loss values to a list and print the average loss for each epoch.
