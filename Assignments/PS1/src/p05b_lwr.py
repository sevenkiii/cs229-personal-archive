import matplotlib.pyplot as plt
import numpy as np
import util

from linear_model import LinearModel


def main(tau, train_path, eval_path):
    """Problem 5(b): Locally weighted regression (LWR)

    Args:
        tau: Bandwidth parameter for LWR.
        train_path: Path to CSV file containing dataset for training.
        eval_path: Path to CSV file containing dataset for evaluation.
    """
    # Load training set
    x_train, y_train = util.load_dataset(train_path, add_intercept=True)
    x_eval, y_eval = util.load_dataset(eval_path, add_intercept=True)
    # *** START CODE HERE ***
    # Fit a LWR model
    # Get MSE value on the validation set
    # Plot validation predictions on top of training set
    # No need to save predictions
    # Plot data
    clf = LocallyWeightedLinearRegression(tau)
    clf.fit(x_train, y_train)
    res = clf.predict(x_eval)

    plt.scatter(x_train[:,1], y_train, c='blue', s=50, marker='x', label='Training Set')
    plt.scatter(x_eval[:,1], res, c='red', s=50, marker='o', label='Validation Set')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('P05B Locally Weighted Linear Regression')
    plt.legend()
    plt.savefig("./output/p05b.png")
    plt.close()
    
    print("MSE: ", np.mean((y_eval - res) ** 2))
    # *** END CODE HERE ***


class LocallyWeightedLinearRegression(LinearModel):
    """Locally Weighted Regression (LWR).

    Example usage:
        > clf = LocallyWeightedLinearRegression(tau)
        > clf.fit(x_train, y_train)
        > clf.predict(x_eval)
    """

    def __init__(self, tau):
        super(LocallyWeightedLinearRegression, self).__init__()
        self.tau = tau
        self.x = None
        self.y = None

    def fit(self, x, y):
        """Fit LWR by saving the training set.

        """
        # *** START CODE HERE ***
        self.x = x
        self.y = y
        # *** END CODE HERE ***

    def predict(self, x):
        """Make predictions given inputs x.

        Args:
            x: Inputs of shape (m, n).

        Returns:
            Outputs of shape (m,).
        """
        # *** START CODE HERE ***
        m = self.x.shape[0]
        res = np.zeros(x.shape[0])
        for num in range(x.shape[0]):
            W = np.zeros((m, m))
            for i in range(m):
                W[i][i] = np.exp(-(np.linalg.norm(self.x[i] - x[num]) ** 2) / 2.0 / (self.tau ** 2)) / 2
            theta = np.linalg.inv(self.x.T @ W @ self.x) @ self.x.T @ W @ self.y
            res[num] = np.dot(theta, x[num])
        return res
        # *** END CODE HERE ***
