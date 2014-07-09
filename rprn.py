#generage a N node's full connected graph with random weights links

import random
import itertools
import time
import fullWeightedGraph as fwg



def randomSelectProviderNewComer(G, N, Ni, fnodei, di):
	backNewComers = list(set(range(N)) - set(Ni + [fnodei]))
	newcomer = random.choice(backNewComers)
	providers = random.sample(Ni, di)
	return newcomer, providers

def forceSelectProviderNewComer(G, N, Ni, fnodei, di):
	providers = []
	newcomer = -1
	bottleNetBW = -1.0

	backNewComers = list(set(range(N)) - set(Ni + [fnodei]))
	backProviders = list(itertools.permutations(Ni, di))

	for nc in backNewComers:
		for pds in backProviders:
			tmpBottleNetBW = min([G[i][nc] for i in pds])
			if tmpBottleNetBW > bottleNetBW:
				bottleNetBW = tmpBottleNetBW
				newcomer = nc
				providers = list(pds)
	return newcomer, providers

def optimalSelectProviderNewComer(G, N, Ni, fnodei, di):
	providers = []
	newcomer = -1
	backNewComers = list(set(range(N)) - set(Ni + [fnodei]))
	validLinks = []
	for nc in backNewComers:
		for pd in Ni:
			validLinks.append((pd, G[pd][nc], nc))
	validLinks.sort(key = lambda x: x[1], reverse = True)
	backncInfo = {}
	for link in validLinks:
		tmp = backncInfo.get(link[2], [])
		if tmp == []:
			backncInfo[link[2]] = [link[0]]
		else:
			tmp.append(link[0])
		if len(tmp) == di:
			newcomer = link[2]
			providers = tmp
			break
	return newcomer, providers

def getBottleNetBW(G, newcomer, providers):
	return min([G[i][newcomer] for i in providers])

if __name__ == '__main__':
	N = 1000
	(b1, b2) = (0.3, 120)
	ni = 14
	ki = 10
	di = 10

	loopNum = 10

	randomOutputFile = open("./output/rprn_random_%s_%s_%s_%s_%s_%s_%s.txt" % \
		(N, b1, b2, ni, ki, di,loopNum), "w")
	# forceOutputFile = open("forceOutputFile.txt", "w")
	optimalOutputFile = open("./output/rprn_optimal_%s_%s_%s_%s_%s_%s_%s.txt" % \
		(N, b1, b2, ni, ki, di,loopNum), "w")

	for i in range(loopNum):
		G = fwg.fullConnectedGraph(N)
		G = fwg.randomLinkWeight(G, (b1, b2))
		
		Ni = fwg.randomSelectBlocksStoredNodes(N, ni)
		(fnodei, Ni) = 	fwg.randomFailedStoredNode(Ni)

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

