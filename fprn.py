'''
Created on Jul 10, 2014
@author: Dongsheng Wei(12210240069@fudan.edu.cn)
'''

import random
import itertools
import time
import fullWeightedGraph as fwg

if __name__ == '__main__':
	N = 1000
	(b1, b2) = (0.3, 120)
	ni = 14
	ki = 10
	di = 10

	loopNum = 100

	randomOutputFile = open("./output/fprn_random_%s_%s_%s_%s_%s_%s_%s.txt" % \
		(N, b1, b2, ni, ki, di,loopNum), "w")
	# forceOutputFile = open("forceOutputFile.txt", "w")
	optimalOutputFile = open("./output/fprn_optimal_%s_%s_%s_%s_%s_%s_%s.txt" % \
		(N, b1, b2, ni, ki, di,loopNum), "w")

	for i in range(loopNum):
		G = fwg.fullConnectedGraph(N)
		G = fwg.randomLinkWeight(G, (b1, b2))
		
		Ni = fwg.randomSelectBlocksStoredNodes(N, ni)
		(fnodei, Ni) = 	fwg.randomFailedStoredNode(Ni)

		providers = random.sample(Ni, di)
		randomNewcomer = random.choice(list(set(range(N)) - set(Ni + [fnodei]))) 

		#TODO:		optimalNewcomer = 
'''
		(fnodei, Ni) = 	randomFailedStoredNode(Ni)

		start = time.time()
		(newcomer, providers) = randomSelectProviderNewComer(G, N, Ni, fnodei, di)
		elapsed = time.time() - start
		bottleNetBW = getBottleNetBW(G, newcomer, providers)
		randomOutputFile.write("%s\t%s\n" % (bottleNetBW, elapsed))
		print "random: (%s, %s)" % (fnodei, Ni)
		print "random: (%s, %s)" % (newcomer, providers) 
		print "random: bottleNetBW = %s" % bottleNetBW
		print "random: elapsed = %ss\n" % elapsed

		# start = time.time()
		# (newcomer, providers) = forceSelectProviderNewComer(G, N, Ni, fnodei, di)
		# elapsed = time.time() - start
		# bottleNetBW = getBottleNetBW(G, newcomer, providers)
		# print "force: (%s, %s)" % (fnodei, Ni)
		# print "force: (%s, %s)" % (newcomer, providers)
		# print "force: bottleNetBW = %s" % bottleNetBW
		# print "force: elapsed = %ss\n" % elapsed

		start = time.time()
		(newcomer, providers) = optimalSelectProviderNewComer(G, N, Ni, fnodei, di)
		elapsed = time.time() - start
		bottleNetBW = getBottleNetBW(G, newcomer, providers)
		optimalOutputFile.write("%s\t%s\n" % (bottleNetBW, elapsed))	
		print "optimal: (%s, %s)" % (fnodei, Ni)
		print "optimal: (%s, %s)" % (newcomer, providers) 
		print "optimal: bottleNetBW = %s" % bottleNetBW
		print "optimal: elapsed = %ss\n" % elapsed

	randomOutputFile.close()
	#forceOutputFile.close()
	optimalOutputFile.close()

'''