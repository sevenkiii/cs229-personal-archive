import matplotlib.pyplot as plt
import numpy as np
import util

from p05b_lwr import LocallyWeightedLinearRegression


def main(tau_values, train_path, valid_path, test_path, pred_path):
    """Problem 5(b): Tune the bandwidth paramater tau for LWR.

    Args:
        tau_values: List of tau values to try.
        train_path: Path to CSV file containing training set.
        valid_path: Path to CSV file containing validation set.
        test_path: Path to CSV file containing test set.
        pred_path: Path to save predictions.
    """
    # Load training set
    x_train, y_train = util.load_dataset(train_path, add_intercept=True)
    x_valid, y_valid = util.load_dataset(valid_path, add_intercept=True)
    x_test, y_test = util.load_dataset(test_path, add_intercept=True)
    # *** START CODE HERE ***
    # Search tau_values for the best tau (lowest MSE on the validation set)
    # Fit a LWR model with the best tau value
    # Run on the test set to get the MSE value
    # Save predictions to pred_path
    # Plot data
    best_tau, best_mse = None, None
    for tau in tau_values:
        clf = LocallyWeightedLinearRegression(tau)
        clf.fit(x_train, y_train)
        res = clf.predict(x_valid)
        mse = np.mean((y_valid - res) ** 2)
        if best_mse == None or mse < best_mse:
            best_tau, best_mse = tau, mse
        
        plt.scatter(x_train[:,1], y_train, c='blue', s=50, marker='x', label='Training Set')
        plt.scatter(x_valid[:,1], res, c='red', s=50, marker='o', label='Validation Set')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('P05C with tau = ' + str(tau))
        plt.legend()
        plt.savefig("./output/p05c_tau_" + str(tau) + ".png")
        plt.close()
    print("best tau: ", best_tau)
    
    clf = LocallyWeightedLinearRegression(best_tau)
    clf.fit(x_train, y_train)
    res = clf.predict(x_test)
    np.savetxt(pred_path, res.ravel(), fmt='%lf')
    print("Test MSE: ", np.mean((y_test - res) ** 2))
    # *** END CODE HERE ***
