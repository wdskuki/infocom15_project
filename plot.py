'''
Created on Jul 10, 2014
@author: Dongsheng Wei(12210240069@fudan.edu.cn)
'''

import matplotlib.pyplot as plt
import numpy as np

def plot_change_b1(N, B1, b2, ni, ki, di, loopNum):
	rd_bwMeans = []
	rd_bwStd = []
	rd_timeMeans = []
	rd_timeStd = []

	fpsn_bwMeans = []
	fpsn_bwStd = []
	fpsn_timeMeans = []
	fpsn_timeStd = []

	spsn_bwMeans = []
	spsn_bwStd = []
	spsn_timeMeans = []
	spsn_timeStd = []

	for i in B1:
		output_bw = np.loadtxt("./output/bw_%s_%s_%s_%s_%s_%s_%s.txt" % \
			(N, i, b2, ni, ki, di,loopNum))
		output_time = np.loadtxt("./output/time_%s_%s_%s_%s_%s_%s_%s.txt" % \
			(N, i, b2, ni, ki, di,loopNum))
		
		means_bw = np.mean(output_bw, axis = 0)
		stds_bw = np.std(output_bw, axis = 0)
		
		means_time = np.mean(output_time, axis = 0)
		stds_time = np.std(output_time, axis = 0)

		rd_bwMeans.append(means_bw[0])
		rd_bwStd.append(stds_bw[0])
		rd_timeMeans.append(means_time[0])
		rd_timeStd.append(stds_time[0])

		fpsn_bwMeans.append(means_bw[1])
		fpsn_bwStd.append(stds_bw[1])
		fpsn_timeMeans.append(means_time[1])
		fpsn_timeStd.append(stds_time[1])

		spsn_bwMeans.append(means_bw[2])
		spsn_bwStd.append(stds_bw[2])
		spsn_timeMeans.append(means_time[2])
		spsn_timeStd.append(stds_time[2])


	# plot rd vs fpsn vs spsn in BW
	plt.figure(1)
	ind = np.arange(len(B1))  # the x locations for the groups
	width = 0.25      # the width of the bars

	plt.bar(ind, rd_bwMeans, width, linewidth = '2', color='r', yerr=rd_bwStd)
	plt.bar(ind+width, fpsn_bwMeans, width, linewidth = '2', color='y', yerr=fpsn_bwStd)
	plt.bar(ind+2*width, spsn_bwMeans, width, linewidth = '2', color='g', yerr=spsn_bwStd)

	plt.ylabel('BottleNetBW(MB/s)')
	plt.xlabel('link BW range(MB/s)')
	plt.title("rd vs fpsn vs spsn \n (N = %s, ni = %s, ki = %s, di = %s, loopNum = %s)"\
		% (N, ni, ki, di, loopNum))

	plt.xticks(ind+width*1.5, map(lambda x: (x, b2), B1))
	plt.legend(('rd', 'fpsn', 'spsn'), loc = 4)
	plt.ylim(0, b2+20)
	plt.show()

	# plot rd v.s. fpsn in BW
	plt.figure(2)
	ind = np.arange(len(B1))  # the x locations for the groups
	width = 0.35      # the width of the bars
	plt.bar(ind, rd_bwMeans, width, linewidth = '2', color='r', yerr=rd_bwStd)
	plt.bar(ind+width, fpsn_bwMeans, width, linewidth = '2', color='y', yerr=fpsn_bwStd)

	plt.ylabel('BottleNetBW(MB/s)')
	plt.xlabel('link BW range(MB/s)')
	plt.title("rd v.s. fpsn. (N = %s, ni = %s, ki = %s, di = %s, loopNum = %s)"\
		% (N, ni, ki, di, loopNum))

	plt.xticks(ind+width, map(lambda x: (x, b2), B1))
	plt.legend(('rd', 'fpsn'), loc = 4)
	plt.ylim(0, b2+20)
	plt.show()

	# plot rd v.s. spsn in BW
	plt.figure(3)
	ind = np.arange(len(B1))  # the x locations for the groups
	width = 0.35      # the width of the bars
	plt.bar(ind, rd_bwMeans, width, linewidth = '2', color='r', yerr=rd_bwStd)
	plt.bar(ind+width, spsn_bwMeans, width, linewidth = '2', color='g', yerr=spsn_bwStd)

	plt.ylabel('BottleNetBW(MB/s)')
	plt.xlabel('link BW range(MB/s)')
	plt.title("rd vs spsn (N = %s, ni = %s, ki = %s, di = %s, loopNum = %s)"\
		% (N, ni, ki, di, loopNum))

	plt.xticks(ind+width, map(lambda x: (x, b2), B1))
	plt.legend(('rd', 'spsn'), loc = 4)
	plt.ylim(0, b2+20)
	plt.show()

	# plot rd v.s. spsn in BW
	plt.figure(4)
	ind = np.arange(len(B1))  # the x locations for the groups
	width = 0.35      # the width of the bars
	plt.bar(ind, fpsn_bwMeans, width, linewidth = '2', color='r', yerr=rd_bwStd)
	plt.bar(ind+width, spsn_bwMeans, width, linewidth = '2', color='g', yerr=spsn_bwStd)

	plt.ylabel('BottleNetBW(MB/s)')
	plt.xlabel('link BW range(MB/s)')
	plt.title("fpsn vs spsn (N = %s, ni = %s, ki = %s, di = %s, loopNum = %s)"\
		% (N, ni, ki, di, loopNum))

	plt.xticks(ind+width, map(lambda x: (x, b2), B1))
	plt.legend(('fpsn', 'spsn'), loc = 4)
	plt.ylim(0, b2+20)
	plt.show()

	# # plot rd v.s. fpsn v.s. spsn in Time
	# plt.figure(4)
	# ind = np.arange(len(B1))  # the x locations for the groups
	# width = 0.25      # the width of the bars

	# plt.bar(ind, rd_timeMeans, width, linewidth = '2', color='r', yerr=rd_timeStd)
	# plt.bar(ind+width, fpsn_timeMeans, width, linewidth = '2', color='y', yerr=fpsn_timeStd)
	# plt.bar(ind+2*width, spsn_timeMeans, width, linewidth = '2', color='g', yerr=spsn_timeStd)

	# plt.xlabel('BottleNetBW(MB/s)')
	# plt.ylabel('Time(s)')
	# plt.title("rd vs fpsn vs spsn \n (N = %s, ni = %s, ki = %s, di = %s, loopNum = %s)"\
	# 	% (N, ni, ki, di, loopNum))

	# plt.xticks(ind+width*1.5, map(lambda x: (x, b2), B1))
	# plt.legend(('rd', 'fpsn', 'spsn'), loc = 2)
	# plt.show()


def plot_change_N(N, b1, b2, ni, ki, di, loopNum):
	rd_bwMeans = []
	rd_bwStd = []
	rd_timeMeans = []
	rd_timeStd = []

	fpsn_bwMeans = []
	fpsn_bwStd = []
	fpsn_timeMeans = []
	fpsn_timeStd = []

	spsn_bwMeans = []
	spsn_bwStd = []
	spsn_timeMeans = []
	spsn_timeStd = []

	for i in N:
		output_bw = np.loadtxt("./output/bw_%s_%s_%s_%s_%s_%s_%s.txt" % \
			(i, b1, b2, ni, ki, di,loopNum))
		output_time = np.loadtxt("./output/time_%s_%s_%s_%s_%s_%s_%s.txt" % \
			(i, b1, b2, ni, ki, di,loopNum))
		
		means_bw = np.mean(output_bw, axis = 0)
		stds_bw = np.std(output_bw, axis = 0)
		
		means_time = np.mean(output_time, axis = 0)
		stds_time = np.std(output_time, axis = 0)

		rd_bwMeans.append(means_bw[0])
		rd_bwStd.append(stds_bw[0])
		rd_timeMeans.append(means_time[0])
		rd_timeStd.append(stds_time[0])

		fpsn_bwMeans.append(means_bw[1])
		fpsn_bwStd.append(stds_bw[1])
		fpsn_timeMeans.append(means_time[1])
		fpsn_timeStd.append(stds_time[1])

		spsn_bwMeans.append(means_bw[2])
		spsn_bwStd.append(stds_bw[2])
		spsn_timeMeans.append(means_time[2])
		spsn_timeStd.append(stds_time[2])


	# plot rd v.s. fpsn v.s. spsn in Time
	plt.figure(1)
	ind = np.arange(len(N))  # the x locations for the groups
	width = 0.25      # the width of the bars

 	plt.plot(N, rd_timeMeans, 'r-', N, fpsn_timeMeans, 'ys-', N, spsn_timeMeans,'g^-')
	# plt.bar(ind, rd_timeMeans, width, linewidth = '2', color='r', yerr=rd_timeStd)
	# plt.bar(ind+width, fpsn_timeMeans, width, linewidth = '2', color='y', yerr=fpsn_timeStd)
	# plt.bar(ind+2*width, spsn_timeMeans, width, linewidth = '2', color='g', yerr=spsn_timeStd)

	plt.xlabel('Total nodes number')
	plt.ylabel('Time(s)')
	plt.title("rd vs fpsn vs spsn \n (ni = %s, ki = %s, di = %s, (%s, %s)MB/s, loopNum = %s)"\
		% (ni, ki, di, b1, b2, loopNum))

	# plt.xticks(ind+width*1.5, map(lambda x: (x, b2), N))
	plt.legend(('rd', 'fpsn', 'spsn'), loc = 2)
	# plt.semilogx()
	plt.show()


if __name__ == '__main__':
	N = 100
	b1 = [0.3, 1, 10, 30, 50, 70, 90]
	b2 = 120
	ni = 14
	ki = 8
	di = 10
	loopNum = 100
	plot_change_b1(N, b1, b2, ni, ki, di, loopNum)