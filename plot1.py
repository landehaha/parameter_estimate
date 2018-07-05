import matplotlib.pyplot as plt
import numpy as np
import xlrd
import copy
# 2000 simulations
data1 = xlrd.open_workbook("fig2_1.xlsx")
table1 = data1.sheet_by_name("Sheet1")
data2 = xlrd.open_workbook("fig2_2.xlsx")
table2 = data2.sheet_by_name("Sheet1")
nrows = table1.nrows
ncols = table1.ncols
Data1 = np.zeros([nrows, ncols])
for i in xrange(0, nrows):
    Data1[i] = table1.row_values(i)
Data2 = np.zeros([nrows, ncols])
for i in xrange(0, nrows):
    Data2[i] = table2.row_values(i)
X = Data1[:, [0]]
Y1_1 = Data1[:, [1]]
Y2_1 = Data1[:, [2]]
Y3_1 = Data1[:, [3]]
Y4_1 = Data1[:, [4]]
Y1_2 = Data2[:, [1]]
Y2_2 = Data2[:, [2]]
Y3_2 = Data2[:, [3]]
Y4_2 = Data2[:, [4]]
plt.figure(1)
plt.subplot(211)
# plt.xlabel('T', fontsize=15)
plt.ylabel('Probability', fontsize=15)
plt.axis([0, 0.001, 0.1, 1])
my_x_ticks = np.arange(0.0001, 0.0011, 0.0001)
plt.xticks(my_x_ticks, fontsize=15)
plt.yticks(fontsize=15)
plt.plot(X, Y1_1, linewidth=2.5, label="u = 0.40")
plt.plot(X, Y2_1, linewidth=2.5, label="u = 0.44")
plt.plot(X, Y3_1, linewidth=2.5, label="u = 0.42")
plt.plot(X, Y4_1, linewidth=2.5, label="u = 0.40")
plt.annotate('(0.0005, 0.403)', xy=(0.0005, 0.403), fontsize=15, xytext=(0.0006, 0.9),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate('(0.0005, 0.442)', xy=(0.0005, 0.442), fontsize=15, xytext=(0.0006, 0.8),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate('(0.0005, 0.427)', xy=(0.0005, 0.427), fontsize=15, xytext=(0.0006, 0.7),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate('(0.0005, 0.403)', xy=(0.0005, 0.403), fontsize=15, xytext=(0.0006, 0.6),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.legend(loc='upper right', fontsize=15)
plt.subplot(212)
plt.xlabel('T', fontsize=15)
plt.ylabel('Expected percentage', fontsize=15)
plt.axis([0, 0.001, 50, 100], fontsize=15)
my_x_ticks = np.arange(0.0001, 0.0011, 0.0001)
plt.xticks(my_x_ticks, fontsize=15)
plt.yticks(fontsize=15)
plt.plot(X, Y1_2, linewidth=2.5, label="v = 70")
plt.plot(X, Y2_2, linewidth=2.5, label="v = 70")
plt.plot(X, Y3_2, linewidth=2.5, label="v = 74")
plt.plot(X, Y4_2, linewidth=2.5, label="v = 78")
plt.annotate('(0.0005, 71.69)', xy=(0.0005, 71.69), fontsize=15, xytext=(0.0006, 95),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate('(0.0005, 70.04)', xy=(0.0005, 70.03), fontsize=15, xytext=(0.0006, 90),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate('(0.0005, 74.80)', xy=(0.0005, 74.80), fontsize=15, xytext=(0.0006, 85),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.annotate('(0.0005, 79.26)', xy=(0.0005, 79.26), fontsize=15, xytext=(0.0006, 80),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.legend(loc='upper right', fontsize=15)
plt.show()
