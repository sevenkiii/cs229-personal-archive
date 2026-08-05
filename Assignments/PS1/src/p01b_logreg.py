import numpy as np
import util

from linear_model import LinearModel


def main(train_path, eval_path, pred_path):
    """Problem 1(b): Logistic regression with Newton's Method.

    Args:
        train_path: Path to CSV file containing dataset for training.
        eval_path: Path to CSV file containing dataset for evaluation.
        pred_path: Path to save predictions.
    """
    x_train, y_train = util.load_dataset(train_path, add_intercept=True)
    x_test, y_test = util.load_dataset(eval_path, add_intercept=True)
    
    # *** START CODE HERE ***
    model = LogisticRegression()
    model.fit(x_train, y_train)
    test_res = model.predict(x_test)
    np.savetxt(pred_path, test_res.ravel(), fmt='%d')
    return model.theta
    # *** END CODE HERE ***


class LogisticRegression(LinearModel):
    """Logistic regression with Newton's Method as the solver.

    Example usage:
        > clf = LogisticRegression()
        > clf.fit(x_train, y_train)
        > clf.predict(x_eval)
    """

    def fit(self, x, y):
        """Run Newton's Method to minimize J(theta) for logistic regression.

        Args:
            x: Training example inputs. Shape (m, n).
            y: Training example labels. Shape (m,).
        """
        # *** START CODE HERE ***
        n = x.shape[1] # size of theta and each x
        m = x.shape[0]
        theta = np.zeros(n)
        kep = True
        eps = self.eps
        def g(x):
            return 1/(1+np.exp(-x))
        while kep:
            delt = np.zeros(n)
            for k in range(0, m):
                delt += -1.0/m * x[k] * (y[k] - g(np.dot(theta, x[k])))
            # print(delt)
            # Calculate Hessian
            Hess = np.zeros((n, n))
            for k in range(0, m):
                Hess += (g(np.dot(theta, x[k])) * (1-g(np.dot(theta, x[k]))) / m *
                    np.outer(x[k], x[k]))
            # print(Hess)
            diff = np.linalg.inv(Hess) @ delt
            diff_norm = np.linalg.norm(diff, ord=1)
            if diff_norm < eps:
                kep = False
            theta = theta - diff
        self.theta = theta
        print("Logistic Regression Theta: ", theta)
        # *** END CODE HERE ***

    def predict(self, x):
        """Make a prediction given new inputs x.

        Args:
            x: Inputs of shape (m, n).

        Returns:
            Outputs of shape (m,).
        """
        # *** START CODE HERE ***
        res = x @ self.theta # (m,n)*(n,) gives (m,1)
        res = res>=0
        return res
        # *** END CODE HERE ***
