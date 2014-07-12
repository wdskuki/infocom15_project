'''
Created on Jul 10, 2014
@author: Dongsheng Wei(12210240069@fudan.edu.cn)
'''

import matplotlib.pyplot as plt
import numpy as np

mytype = "fpsn"
N = 20
b1 = [0.3, 1, 10, 30, 50, 70, 90]
b2 = 120
ni = 10
ki = 6
di = 8
loopNum = 100

randomMeans = []
randomStd = []
optimalMeans = []
optimalStd = []


for i in b1:
	random = np.loadtxt("./output/%s_random_%s_%s_%s_%s_%s_%s_%s.txt" % \
		(mytype, N, i, b2, ni, ki, di,loopNum))
	randomMeans.append(np.mean(random, axis = 0)[0])
	randomStd.append(np.std(random, axis = 0)[0])


	optimal = np.loadtxt("./output/%s_optimal_%s_%s_%s_%s_%s_%s_%s.txt" % \
		(mytype, N, i, b2, ni, ki, di,loopNum))
	optimalMeans.append(np.mean(optimal, axis = 0)[0])
	optimalStd.append(np.std(optimal, axis = 0)[0])

ind = np.arange(len(b1))  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, randomMeans, width, color='r', yerr=randomStd)

rects2 = ax.bar(ind+width, optimalMeans, width, color='y', yerr=optimalStd)

# add some
ax.set_ylabel('BottleNetBW(MB/s)')
ax.set_xlabel('link BW range(MB/s)')
ax.set_title("(N = %s, ni = %s, ki = %s, di = %s, loopNum = %s)"\
 % (N, ni, ki, di, loopNum))
ax.set_xticks(ind+width)
ax.set_xticklabels( [(b1[i], b2) for i in range(len(b1))] )


ax.legend( (rects1[0], rects2[0]), ('Random', 'Optimal'), loc = 4)

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()
