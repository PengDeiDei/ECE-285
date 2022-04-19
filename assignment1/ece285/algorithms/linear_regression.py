"""
Linear Regression model
"""

import numpy as np


class Linear(object):
    def __init__(self, n_class: int, lr: float, epochs: int, weight_decay: float):
        """Initialize a new classifier.

        Parameters:
            n_class: the number of classes
            lr: the learning rate
            epochs: the number of epochs to train for
        """
        self.w = None  # Initialize in train
        self.lr = lr
        self.epochs = epochs
        self.n_class = n_class
        self.weight_decay = weight_decay
        
    def train(self, X_train: np.ndarray, y_train: np.ndarray, weights: np.ndarray) -> np.ndarray:
        """Train the classifier.

        Use the linear regression update rule as introduced in the Lecture.

        Parameters:
            X_train: a number array of shape (N, D) containing training data;
                N examples with D dimensions
            y_train: a numpy array of shape (N,) containing training labels
        """

        N, D = X_train.shape
        num_class = self.n_class
        y_train_2class = np.zeros((N,num_class))
        
        # I use one vs rest, assign 1 to the class and 0 to the rest rather than -1 to avoid overflow
        for i in range(N):
            y_train_2class[i,y_train[i]] = 1
        
        # the loss function should be the L2 norm of the difference between y_hat - y_train
        # for conveniently calculating the gradient, only use y_hat - y_train
        for i in range(self.epochs):
            y_hat = np.dot(X_train,weights.T)
            loss = y_hat - y_train_2class
            gradient = np.dot(loss.T,X_train)/N
            weights = weights - self.lr*gradient - self.weight_decay*weights
            
        self.w = weights
        return self.w

    def predict(self, X_test: np.ndarray) -> np.ndarray:
        """Use the trained weights to predict labels for test data points.

        Parameters:
            X_test: a numpy array of shape (N, D) containing testing data;
                N examples with D dimensions

        Returns:
            predicted labels for the data in X_test; a 1-dimensional array of
                length N, where each element is an integer giving the predicted
                class.
        """
        # return the prediction with highest score
        y_pred = np.dot(X_test,self.w.T)
        y_test_pred = np.argmax(y_pred,axis = 1)
        
        return y_test_pred
