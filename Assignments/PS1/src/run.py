import argparse

import util
from p01b_logreg import main as p01b
from p01e_gda import main as p01e
from p02cde_posonly import main as p02
from p03d_poisson import main as p03
from p05b_lwr import main as p05b
from p05c_tau import main as p05c

parser = argparse.ArgumentParser()
parser.add_argument('p_num', nargs='?', type=int, default=0,
                    help='Problem number to run, 0 for all problems.')
args = parser.parse_args()

# Problem 1
if args.p_num == 0 or args.p_num == 1:
    theta_b1 = p01b(train_path='../data/ds1_train.csv',
         eval_path='../data/ds1_valid.csv',
         pred_path='output/p01b_pred_1.txt')

    theta_b2 = p01b(train_path='../data/ds2_train.csv',
         eval_path='../data/ds2_valid.csv',
         pred_path='output/p01b_pred_2.txt')

    theta_e1 = p01e(train_path='../data/ds1_train.csv',
         eval_path='../data/ds1_valid.csv',
         pred_path='output/p01e_pred_1.txt')

    theta_e2 = p01e(train_path='../data/ds2_train.csv',
         eval_path='../data/ds2_valid.csv',
         pred_path='output/p01e_pred_2.txt')
    
    # plot
#     x1_train, y1_train = util.load_dataset('../data/ds1_train.csv', add_intercept=False)
#     util.plot(x1_train, y1_train, theta_b1, 'output/p01b_pred_1.png')
#     util.plot(x1_train, y1_train, theta_e1, 'output/p01e_pred_1.png')
    
#     x2_train, y2_train = util.load_dataset('../data/ds2_train.csv', add_intercept=False)
#     util.plot(x2_train, y2_train, theta_b2, 'output/p01b_pred_2.png')
#     util.plot(x2_train, y2_train, theta_e2, 'output/p01e_pred_2.png')

# Problem 2
if args.p_num == 0 or args.p_num == 2:
    p02(train_path='../data/ds3_train.csv',
        valid_path='../data/ds3_valid.csv',
        test_path='../data/ds3_test.csv',
        pred_path='output/p02X_pred.txt')

# Problem 3
if args.p_num == 0 or args.p_num == 3:
    p03(lr=1e-7,
        train_path='../data/ds4_train.csv',
        eval_path='../data/ds4_valid.csv',
        pred_path='output/p03d_pred.txt')

# Problem 5
if args.p_num == 0 or args.p_num == 5:
    p05b(tau=5e-1,
         train_path='../data/ds5_train.csv',
         eval_path='../data/ds5_valid.csv')

    p05c(tau_values=[3e-2, 5e-2, 1e-1, 5e-1, 1e0, 1e1],
         train_path='../data/ds5_train.csv',
         valid_path='../data/ds5_valid.csv',
         test_path='../data/ds5_test.csv',
         pred_path='output/p05c_pred.txt')
