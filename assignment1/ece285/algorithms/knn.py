"""
K Nearest Neighbours Model
"""
import numpy as np


class KNN(object):
    def __init__(self, num_class: int):
        self.num_class = num_class

    def train(self, x_train: np.ndarray, y_train: np.ndarray, k: int):
        """
        Train KNN Classifier

        KNN only need to remember training set during training

        Parameters:
            x_train: Training samples ; np.ndarray with shape (N, D)
            y_train: Training labels  ; snp.ndarray with shape (N,)
        """
        self._x_train = x_train
        self._y_train = y_train
        self.k = k

    def predict(self, x_test: np.ndarray, k: int = None, loop_count: int = 1):
        """
        Use the contained training set to predict labels for test samples

        Parameters:
            x_test    : Test samples; np.ndarray with shape (N, D)
            k       : k to overwrite the one specificed during training; int
            loop_count : parameter to choose different knn implementation ; int

        Returns:
            predicted labels for the data in X_test; a 1-dimensional array of
                length N, where each element is an integer giving the predicted
                class.
        """
        # Fill this function in
        k_test = k if k is not None else self.k

        if loop_count == 1:
            distance = self.calc_dis_one_loop(x_test)
        elif loop_count == 2:
            distance = self.calc_dis_two_loop(x_test)

        # TODO: implement me
        num_test = x_test.shape[0]
        y_test = np.zeros(num_test)
        
        for i in range(num_test):
            sorted_distance = np.argsort(distance[i])
            y_knn = list(self._y_train[sorted_distance[0:k]])
            y_test[i] = np.argmax(np.bincount(y_knn))
            
        return y_test

    def calc_dis_one_loop(self, x_test: np.ndarray):
        """
        Calculate distance between training samples and test samples

        This function could one for loop

        Parameters:
            x_test: Test samples; np.ndarray with shape (N, D)
        """
        num_train = self._x_train.shape[0]
        num_test = x_test.shape[0]
        
        # distance matrix, size = (num_test,num_train)
        distance = np.zeros((num_test,num_train))
        """
        I found a way without using any loop at all,and it is much faster. Here is the code:
        
        dists = np.zeros((num_test, num_train)) 
        dists = np.sqrt(np.sum(np.square(self._x_train), axis=1) + np.sum(np.square(x_test), axis=1)[:, np.newaxis] - 
                       2 * np.dot(x_test, self._x_train.T))
        """
        for j in range(num_train):
            distance[:,j] = np.sum((x_test - self._x_train[j])**2, axis=1)
        
        distance = np.sqrt(distance)
        return distance

    def calc_dis_two_loop(self, x_test: np.ndarray):
        """
        Calculate distance between training samples and test samples

        This function could contain two loop

        Parameters:
            x_test: Test samples; np.ndarray with shape (N, D)
        """
        num_train = self._x_train.shape[0]
        num_test = x_test.shape[0]
        
        # distance matrix, size = (num_test,num_train)
        distance = np.zeros((num_test,num_train))
        
        for i in range(num_test):
            for j in range(num_train):
                distance[i,j] = np.sum((x_test[i] - self._x_train[j])**2)
            
        distance = np.sqrt(distance)
        return distance
             
