# Important note: you do not have to modify this file for your homework.
import matplotlib.pyplot as plt

import util
import numpy as np


def calc_grad(X, Y, theta):
    """Compute the gradient of the loss with respect to theta."""
    m, n = X.shape

    margins = Y * X.dot(theta)
    probs = 1. / (1 + np.exp(margins))
    grad = -(1./m) * (X.T.dot(probs * Y))

    return grad
 

def logistic_regression(X, Y):
    """Train a logistic regression model."""
    m, n = X.shape
    theta = np.zeros(n)
    learning_rate = 10

    i = 0
    while True:
        i += 1
        prev_theta = theta
        grad = calc_grad(X, Y, theta)
        theta = theta - learning_rate * grad
        if i <= 10:
            print("After %d iterations got " % i, theta)
            # print("with              grad ", grad)
            # print("doubled theta has grad ", calc_grad(X, Y, theta * 2))
            # print("0.5*    theta has grad ", calc_grad(X, Y, theta * 0.5))
            # print("")
        if i % 10000 == 0:
            print('Finished %d iterations' % i)
            # print("After %d iterations got " % i, theta)
            # print("with              grad ", grad)
            # print("doubled theta has grad ", calc_grad(X, Y, theta * 2))
            # print("0.5*    theta has grad ", calc_grad(X, Y, theta * 0.5))
            # print("")
        if np.linalg.norm(prev_theta - theta) < 1e-15:
            print('Converged in %d iterations' % i)
            # print("with              grad ", grad)
            # print("doubled theta has grad ", calc_grad(X, Y, theta * 2))
            # print("0.5*    theta has grad ", calc_grad(X, Y, theta * 0.5))
            # print("")
            break
    return


def main():
    print('==== Training model on data set A ====')
    Xa, Ya = util.load_csv('../data/ds1_a.csv', add_intercept=True)
    logistic_regression(Xa, Ya)

    print('\n==== Training model on data set B ====')
    Xb, Yb = util.load_csv('../data/ds1_b_fake.csv', add_intercept=True)
    logistic_regression(Xb, Yb)


if __name__ == '__main__':
    main()
