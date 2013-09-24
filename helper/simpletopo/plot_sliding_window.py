import matplotlib
# Force matplotlib to not use x-server
matplotlib.use('Agg')

import matplotlib.pyplot as mpl
import numpy as np
import csv


fileIn=list(csv.reader(open("/afs/pdc.kth.se/misc/pdc/volumes/sbc/prj.sbc.chrisp.1/scampi/output/completeOutput.txt","rb"),delimiter=';'))

markerList = ["+",".","o","*","p","s","<",">","h","H","v","_","D"]

matrix = []
x_axis = []
names = fileIn[0][1:len(fileIn[0])]

print names

for i in range(1, len(fileIn)):
    matrix.append(fileIn[i][1:len(fileIn[i])])
    x_axis.append(fileIn[i][0])

np_array = np.asarray(matrix)


for i in range(0, np.transpose(np_array).shape[0]):
    mpl.plot(x_axis, np.transpose(np_array)[i], marker=markerList[i], label=names[i])
mpl.legend(loc=4, ncol=2)
#mpl.show()
mpl.savefig("/afs/pdc.kth.se/misc/pdc/volumes/sbc/prj.sbc.chrisp.1/scampi/output/simpleTopo.png")