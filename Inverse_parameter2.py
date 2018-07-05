from random import random
import math
import sys
from time import time
from simAnneal import SimAnneal
from simAnneal import OptSolution
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from sklearn import gaussian_process
import xlrd
import copy
# 2000 simulations
data1 = xlrd.open_workbook("DataGP_Cyclin1.xlsx")
table1 = data1.sheet_by_name("Sheet1")
data2 = xlrd.open_workbook("DataGP_Cyclin2.xlsx")
table2 = data2.sheet_by_name("Sheet1")
nrows = table1.nrows
ncols = table1.ncols
Data1 = np.zeros([nrows, ncols])
for i in xrange(0, nrows):
    Data1[i] = table1.row_values(i)
Data2 = np.zeros([nrows, ncols])
for i in xrange(0, nrows):
    Data2[i] = table2.row_values(i)
train_X = Data1[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
train_Y1 = Data1[:, [11]]
true_Y1 = Data2[:, [12]]
train_Y2 = Data2[:, [11]]
true_Y2 = Data2[:, [12]]
# g1 = 0.62
# g2 = 1.3
# g1 = 0.6
# g2 = 1.5
# g1 = 0.62
# g2 = 1.5
g1 = 0.63
g2 = 1.4
gp1 = gaussian_process.GaussianProcessRegressor(kernel=None,
                                                alpha=1e-10,
                                                optimizer="fmin_l_bfgs_b",
                                                n_restarts_optimizer=0,
                                                normalize_y=True,
                                                copy_X_train=True,
                                                random_state=None)
gp2 = gaussian_process.GaussianProcessRegressor(kernel=None,
                                                alpha=1e-10,
                                                optimizer="fmin_l_bfgs_b",
                                                n_restarts_optimizer=0,
                                                normalize_y=True,
                                                copy_X_train=True,
                                                random_state=None)
gp1.fit(train_X, train_Y1)
gp2.fit(train_X, train_Y2)


def Dfunc(x):
    x1 = copy.deepcopy(x)
    x1[0] = x1[0]/1000
    x1[1] = x1[1]/1000
    x1[2] = x1[2]/1000
    x1[3] = x1[3]/10
    x1[4] = x1[4]/10
    x1[5] = x1[5]/1000
    x1[6] = x1[6]/1000
    x1[7] = x1[7]/1000
    x1[8] = x1[8]/1000
    x1[9] = x1[9]/100
    x1[10] = x1[10]/100
    D11, D12 = gp1.predict(np.matrix(x1), return_std=True)
    D1 = D11 - 1.96 * D12
    D21, D22 = gp2.predict(np.matrix(x1), return_std=True)
    D2 = D21 - 1.96 * D22
    if D1 >= g1:
        D1 = 0
    else:
        D1 = D1 - g1
    if D2 >= g2:
        D2 = 0
    else:
        D2 = D2 - g2
    D = D1**2 + D2**2
    return D


def rmse(predictions, targets):
    return np.sqrt(((predictions - targets) ** 2).mean())
if __name__ == '__main__':

    targ = SimAnneal(target_text='max')
    # for maximun case
    # init = -sys.maxsize
    # for minimun case
    init = sys.maxsize
    xyRange = [[2, 6], [2, 6], [2, 6], [2, 6], [2, 6], [2, 6],
               [6, 12], [6, 12], [6, 12], [1, 3], [1, 3]]
    xRange = [[0, 1]]
    t_start = time()

    calculate = OptSolution(Markov_chain=1000, result=init, val_nd=[0, 0])
    output = calculate.soulution(SA_newV=targ.newVar, SA_juge=targ.juge,
                                 juge_text='min',
                                 ValueRange=xyRange, func=Dfunc)

    '''
    with open('out.dat', 'w') as f:
        for i in range(len(output)):
            f.write(str(output[i]) + '\n')
    # '''
    t_end = time()
    print('Running %.4f seconds' % (t_end-t_start))
