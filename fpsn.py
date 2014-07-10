'''
Created on Jul 10, 2014
@author: Dongsheng Wei(12210240069@fudan.edu.cn)
'''

import random
import itertools
import time
import fullWeightedGraph as fwg

def randomSelectNewComer(N, Ni, fnodei):
	backNewComers = list(set(range(N)) - set(Ni + [fnodei]))
	newcomer = random.choice(backNewComers)
	return newcomer

def optimalSelectNewComer(G, N, Ni, fnodei, providers):
	backNewComers = list(set(range(N)) - set(Ni + [fnodei]))
	bottleNetBW = -1.0
	newcomer = -1
	for nc in backNewComers:
		tmpBottleNetBW = min(G[j][nc] for j in providers)
		if tmpBottleNetBW > bottleNetBW:
			bottleNetBW = tmpBottleNetBW
			newcomer = nc
	return newcomer

if __name__ == '__main__':
	N = 1000
	(b1, b2) = (70, 120)
	ni = 14
	ki = 10
	di = 10

	loopNum = 100

	randomOutputFile = open("./output/fpsn_random_%s_%s_%s_%s_%s_%s_%s.txt" % \
		(N, b1, b2, ni, ki, di,loopNum), "w")
	# forceOutputFile = open("forceOutputFile.txt", "w")
	optimalOutputFile = open("./output/fpsn_optimal_%s_%s_%s_%s_%s_%s_%s.txt" % \
		(N, b1, b2, ni, ki, di,loopNum), "w")

	for i in range(loopNum):
		G = fwg.fullConnectedGraph(N)
		G = fwg.randomLinkWeight(G, (b1, b2))
		
		Ni = fwg.randomSelectBlocksStoredNodes(N, ni)
		(fnodei, Ni) = 	fwg.randomFailedStoredNode(Ni)

		providers = random.sample(Ni, di)
		
		#random select newcomer
		start = time.time()
		newcomer = randomSelectNewComer(N, Ni, fnodei)
		elapsed = time.time() - start
		bottleNetBW = fwg.getBottleNetBW(G, newcomer, providers)
		randomOutputFile.write("%s\t%s\n" % (bottleNetBW, elapsed))
		print "random: (%s, %s)" % (fnodei, Ni)
		print "random: (%s, %s)" % (newcomer, providers) 
		print "random: bottleNetBW = %s" % bottleNetBW
		print "random: elapsed = %ss\n" % elapsed

		#optimal select newcomer
		start = time.time()
		newcomer = optimalSelectNewComer(G, N, Ni, fnodei, providers)
		elapsed = time.time() - start
		bottleNetBW = fwg.getBottleNetBW(G, newcomer, providers)
		optimalOutputFile.write("%s\t%s\n" % (bottleNetBW, elapsed))
		print "optimal: (%s, %s)" % (fnodei, Ni)
		print "optimal: (%s, %s)" % (newcomer, providers) 
		print "optimal: bottleNetBW = %s" % bottleNetBW
		print "optimal: elapsed = %ss\n" % elapsed

	randomOutputFile.close()
	optimalOutputFile.close()