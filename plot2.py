import matplotlib.pyplot as plt
import numpy as np
import xlrd
import copy
# 2000 simulations
data1 = xlrd.open_workbook("fig3_1.xlsx")
table1 = data1.sheet_by_name("Sheet1")
data2 = xlrd.open_workbook("fig3_2.xlsx")
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
plt.subplot(421)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel('Probability', fontsize=15)
plt.plot(X, Y1_1, Color='blue', linewidth=2.5, label="u = 0.62")
plt.legend(loc='lower right', fontsize=15)
plt.annotate('(10, 0.650)', xy=(10, 0.650), fontsize=15, xytext=(12, 0.7),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.subplot(423)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel('Probability', fontsize=15)
plt.plot(X, Y2_1, Color='red', linewidth=2.5, label="u = 0.60")
plt.legend(loc='lower right', fontsize=15)
plt.annotate('(10, 0.645)', xy=(10, 0.645), fontsize=15, xytext=(12, 0.7),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.subplot(425)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel('Probability', fontsize=15)
plt.plot(X, Y3_1, Color='green', linewidth=2.5, label="u = 0.62")
plt.legend(loc='lower right', fontsize=15)
plt.annotate('(10, 0.654)', xy=(10, 0.654), fontsize=15, xytext=(12, 0.7),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.subplot(427)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('T', fontsize=15)
plt.ylabel('Probability', fontsize=15)
plt.plot(X, Y4_1, Color='purple', linewidth=2.5, label="u = 0.63")
plt.legend(loc='lower right', fontsize=15)
plt.annotate('(10, 0.642)', xy=(10, 0.642), fontsize=15, xytext=(12, 0.7),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.subplot(422)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel('Expected quantity', fontsize=15)
plt.plot(X, Y1_2, Color='blue', linewidth=2.5, label="v = 1.3")
plt.legend(loc='lower right', fontsize=15)
plt.annotate('(10, 1.60)', xy=(10, 1.60), fontsize=15, xytext=(12, 1.65),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.subplot(424)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel('Expected quantity', fontsize=15)
plt.plot(X, Y2_2, Color='red', linewidth=2.5, label="v = 1.5")
plt.legend(loc='lower right', fontsize=15)
plt.annotate('(10, 1.59)', xy=(10, 1.59), fontsize=15, xytext=(12, 1.65),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.subplot(426)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel('Expected quantity', fontsize=15)
plt.plot(X, Y3_2, Color='green', linewidth=2.5, label="v = 1.5")
plt.legend(loc='lower right', fontsize=15)
plt.annotate('(10, 1.60)', xy=(10, 1.60), fontsize=15, xytext=(12, 1.65),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.subplot(428)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel('T', fontsize=15)
plt.ylabel('Expected quantity', fontsize=15)
plt.plot(X, Y4_2, Color='purple', linewidth=2.5, label="v = 1.4")
plt.legend(loc='lower right', fontsize=15)
plt.annotate('(10, 1.59)', xy=(10, 1.59), fontsize=15, xytext=(12, 1.65),
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.show()
