import numpy as np
import util

from linear_model import LinearModel


def main(train_path, eval_path, pred_path):
    """Problem 1(e): Gaussian discriminant analysis (GDA)

    Args:
        train_path: Path to CSV file containing dataset for training.
        eval_path: Path to CSV file containing dataset for evaluation.
        pred_path: Path to save predictions.
    """
    # Load dataset
    x_train, y_train = util.load_dataset(train_path, add_intercept=False)
    x_test, y_test = util.load_dataset(eval_path, add_intercept=False)
    
    # *** START CODE HERE ***
    clf = GDA()
    clf.fit(x_train, y_train)
    
    test_res = clf.predict(x_test)
    np.savetxt(pred_path, test_res.ravel(), fmt='%d')
    return np.insert(clf.theta, 0, clf.theta_0)
    # *** END CODE HERE ***


class GDA(LinearModel):
    """Gaussian Discriminant Analysis.

    Example usage:
        > clf = GDA()
        > clf.fit(x_train, y_train)
        > clf.predict(x_eval)
    """

    def fit(self, x, y):
        """Fit a GDA model to training set given by x and y.

        Args:
            x: Training example inputs. Shape (m, n).
            y: Training example labels. Shape (m,).

        Returns:
            theta: GDA model parameters.
        """
        # *** START CODE HERE ***
        m = x.shape[0]
        n = x.shape[1]
        phi = 1.0/m * np.sum(y)
        mu = [0, 0]
        mu[0] = np.sum(x[y == 0], axis=0) / (m - np.sum(y))
        mu[1] = np.sum(x[y == 1], axis=0) / np.sum(y)
        sigma = np.zeros((n, n))
        for i in range(0, m):
            sigma += 1.0/m * np.outer(x[i] - mu[int(y[i])], x[i] - mu[int(y[i])])
        sigma_inv = np.linalg.inv(sigma)
        self.theta = sigma_inv @ (mu[1] - mu[0])
        self.theta_0 = (1.0/2 * (np.dot(mu[0], sigma_inv @ mu[0]) 
            - np.dot(mu[1], sigma_inv @ mu[1])) + np.log(phi / (1 - phi)))
        
        print("GDA Theta: ", self.theta)
        print("GDA Theta_0: ", self.theta_0)
        # *** END CODE HERE ***

    def predict(self, x):
        """Make a prediction given new inputs x.

        Args:
            x: Inputs of shape (m, n).

        Returns:
            Outputs of shape (m,).
        """
        # *** START CODE HERE ***
        res = x @ self.theta + self.theta_0
        res = res>=0
        return res
        # *** END CODE HERE
