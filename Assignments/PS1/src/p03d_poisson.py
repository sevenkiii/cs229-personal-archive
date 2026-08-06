import numpy as np
import util

from linear_model import LinearModel


def main(lr, train_path, eval_path, pred_path):
    """Problem 3(d): Poisson regression with gradient ascent.

    Args:
        lr: Learning rate for gradient ascent.
        train_path: Path to CSV file containing dataset for training.
        eval_path: Path to CSV file containing dataset for evaluation.
        pred_path: Path to save predictions.
    """
    # Load training set
    x_train, y_train = util.load_dataset(train_path, add_intercept=True)
    x_test, y_test = util.load_dataset(eval_path, add_intercept=True)
    # The line below is the original one from Stanford. It does not include the intercept, but this should be added.
    # x_train, y_train = util.load_dataset(train_path, add_intercept=False)

    # *** START CODE HERE ***
    # Fit a Poisson Regression model
    # Run on the validation set, and use np.savetxt to save outputs to pred_path
    clf = PoissonRegression(step_size=lr)
    clf.fit(x_train, y_train)
    print("Poisson Regression Theta: ", clf.theta)
    test_res = clf.predict(x_test)
    np.savetxt(pred_path, test_res.ravel(), fmt='%lf')
    # *** END CODE HERE ***


class PoissonRegression(LinearModel):
    """Poisson Regression.

    Example usage:
        > clf = PoissonRegression(step_size=lr)
        > clf.fit(x_train, y_train)
        > clf.predict(x_eval)
    """

    def fit(self, x, y):
        """Run gradient ascent to maximize likelihood for Poisson regression.

        Args:
            x: Training example inputs. Shape (m, n).
            y: Training example labels. Shape (m,).
        """
        # *** START CODE HERE ***
        m = x.shape[0]
        n = x.shape[1]
        alpha = self.step_size
        theta = np.zeros(n)
        # Using SGA is BAD here
        kep = True
        while kep:
            nxt = np.copy(theta)
            for i in range(m):
                nxt += alpha * (y[i] - np.exp(np.dot(theta, x[i]))) * x[i] / m
            if np.linalg.norm(nxt-theta, ord=1) <= self.eps:
                kep = False
            theta = nxt
        self.theta = theta
        # *** END CODE HERE ***

    def predict(self, x):
        """Make a prediction given inputs x.

        Args:
            x: Inputs of shape (m, n).

        Returns:
            Floating-point prediction for each input, shape (m,).
        """
        # *** START CODE HERE ***
        res = x @ self.theta
        res = np.exp(res)
        return res
        # *** END CODE HERE ***
