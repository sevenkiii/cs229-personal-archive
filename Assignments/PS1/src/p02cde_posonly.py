import numpy as np
import util

from p01b_logreg import LogisticRegression

# Character to replace with sub-problem letter in plot_path/pred_path
WILDCARD = 'X'


def main(train_path, valid_path, test_path, pred_path):
    """Problem 2: Logistic regression for incomplete, positive-only labels.

    Run under the following conditions:
        1. on y-labels,
        2. on l-labels,
        3. on l-labels with correction factor alpha.

    Args:
        train_path: Path to CSV file containing training set.
        valid_path: Path to CSV file containing validation set.
        test_path: Path to CSV file containing test set.
        pred_path: Path to save predictions.
    """
    pred_path_c = pred_path.replace(WILDCARD, 'c')
    pred_path_d = pred_path.replace(WILDCARD, 'd')
    pred_path_e = pred_path.replace(WILDCARD, 'e')

    # *** START CODE HERE ***
    # Part (c): Train and test on true labels
    # Make sure to save outputs to pred_path_c
    
    x_train, y_train = util.load_dataset(train_path, add_intercept=True, label_col='t')
    x_test, y_test = util.load_dataset(test_path, add_intercept=True, label_col='t')
    clf = LogisticRegression()
    clf.fit(x_train, y_train)
    test_res = clf.predict(x_test)
    np.savetxt(pred_path_c, test_res.ravel(), fmt='%d')
    util.plot(x_test, y_test, clf.theta, './output/p02c.png')
    # Acc: 98.3871%
    
    
    # Part (d): Train on y-labels and test on true labels
    # Make sure to save outputs to pred_path_d
    
    x_train, y_train = util.load_dataset(train_path, add_intercept=True, label_col='y')
    x_test, y_test = util.load_dataset(test_path, add_intercept=True, label_col='t')
    clf = LogisticRegression()
    clf.fit(x_train, y_train)
    test_res = clf.predict(x_test)
    np.savetxt(pred_path_d, test_res.ravel(), fmt='%d')
    util.plot(x_test, y_test, clf.theta, './output/p02d.png')
    # Acc: 50%? output all zeros
    
    # Part (e): Apply correction factor using validation set and test on true labels
    # Plot and use np.savetxt to save outputs to pred_path_e
    
    x_valid, y_valid = util.load_dataset(valid_path, add_intercept=True, label_col='y')
    
    valid_prb = clf.predict_prb(x_valid)
    alpha = np.mean(valid_prb[y_valid == 1])
    test_prb = clf.predict_prb(x_test)
    test_prb = test_prb / alpha
    test_res = test_prb >= 0.5
    np.savetxt(pred_path_e, test_res.ravel(), fmt='%d')
    util.plot(x_test, y_test, clf.theta, './output/p02e.png', alpha)
    # Acc: 95.1613%
    
    # *** END CODER HERE
