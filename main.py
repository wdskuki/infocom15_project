'''
Created on Jul 12, 2014
@author: Dongsheng Wei(12210240069@fudan.edu.cn)
'''
import time
import rd
import fpsn
import spsn
import fullWeightedGraph as fwg
import plot
# spsn test


def setEnv(N, b1, b2, ni, ki, di):
	G = fwg.fullConnectedGraph(N)
	G = fwg.randomLinkWeight(G, (b1, b2))

	# graph = open("./output/graph2.txt","w")
	# for i in range(N):
	# 	for j in range(N):
	# 		graph.write("%s\t" % G[i][j])
	# 	graph.write("\n")
	# graph.close()

	Ni = fwg.randomSelectBlocksStoredNodes(N, ni)
	(fnodei, Ni) = 	fwg.randomFailedStoredNode(Ni)
	


	return G, Ni, fnodei



# loopNum = 1
def singleLoopTestResult(N, b1, b2, ni, ki, di):
	G, Ni, fnodei = setEnv(N, b1, b2, ni, ki, di)

	# Random select newcomer and providers
	start = time.time()
	rd_providers = rd.randomSelectProviders(Ni, di)
	rd_newcomer = rd.randomSelectNewComer(N, Ni, fnodei)
	rd_elapsed = time.time() - start

	rd_bottleBW, rd_bottleLinkNode = fwg.getBottleNetBW(G, rd_newcomer, rd_providers)
	print "random: (%s, %s)" % (rd_newcomer, sorted(rd_providers))
	print "random: G[%s][%s] = %s" % (rd_bottleLinkNode, rd_newcomer,G[rd_bottleLinkNode][rd_newcomer])
	print "random: (%s, %s)\n\n" % (rd_bottleBW, rd_elapsed)
	
	# fix providers and then select newcomer
	start = time.time()
	fpsn_providers = rd_providers[:] # providers are the same with random scheme
	#fpsn_providers = fpsn.fpsnSelectProviders(Ni, di)
	fpsn_newcomer = fpsn.fpsnSelectNewComer(G, N, Ni, fnodei, fpsn_providers)
	fpsn_elapsed = time.time() - start

	fpsn_bottleBW, fpsn_bottleLinkNode = fwg.getBottleNetBW(G, fpsn_newcomer, fpsn_providers)
	print "fpsn: (%s, %s)" % (fpsn_newcomer, sorted(fpsn_providers))
	print "fpsn: G[%s][%s] = %s" % (fpsn_bottleLinkNode, fpsn_newcomer, G[fpsn_bottleLinkNode][fpsn_newcomer])
	print "fpsn: (%s, %s)\n\n" % (fpsn_bottleBW, fpsn_elapsed)

	# both select providers and newcomer
	start = time.time()
	spsn_newcomer, spsn_providers = spsn.spsnSelectProviderNewComer(G, N, Ni, fnodei, di)
	spsn_elapsed = time.time() - start

	spsn_bottleBW, spsn_bottleLinkNode = fwg.getBottleNetBW(G, spsn_newcomer, spsn_providers)
	print "spsn: (%s, %s)" % (spsn_newcomer, sorted(spsn_providers))
	print "spsn: G[%s][%s] = %s" % (spsn_bottleLinkNode,spsn_newcomer, G[spsn_bottleLinkNode][spsn_newcomer])
	print "spsn: (%s, %s)\n\n" % (spsn_bottleBW, spsn_elapsed)

	if rd_bottleBW > fpsn_bottleBW or fpsn_bottleBW > spsn_bottleBW:
		print "Error: there are some logical error in algorithm"
		exit(1)

	return rd_bottleBW, fpsn_bottleBW, spsn_bottleBW, rd_elapsed, fpsn_elapsed, spsn_elapsed


# loopNum > 0
def mutliLoopTestResult(N, b1, b2, ni, ki, di, loopNum):
	outputFile_bw = open("./output/bw_%s_%s_%s_%s_%s_%s_%s.txt" % \
		(N, b1, b2, ni, ki, di,loopNum), "w")
	outputFile_time = open("./output/time_%s_%s_%s_%s_%s_%s_%s.txt" % \
		(N, b1, b2, ni, ki, di,loopNum), "w")
	
	for i in range(loopNum):
		print "<<<<<loopNum = %d>>>>>>" % (i+1)
		rd_bw, fpsn_bw, spsn_bw, rd_time, fpsn_time, spsn_time = singleLoopTestResult(N, b1, b2, ni, ki, di)
		outputFile_bw.write("%s\t%s\t%s\n" % (rd_bw, fpsn_bw, spsn_bw))
		outputFile_time.write("%s\t%s\t%s\n" % (rd_time, fpsn_time, spsn_time))
	
	outputFile_bw.close()
	outputFile_time.close()

def test_change_b1():
	N = 1000
	b1 = [0.3, 1, 10, 30, 50, 70, 90]
	b2 = 120
	ni = 14
	ki = 8
	di = 10
	loopNum = 100

	# for i in b1:
	# 	mutliLoopTestResult(N, i, b2, ni, ki, di, loopNum)
	plot.plot_change_b1(N, b1, b2, ni, ki, di, loopNum)


def test_change_N():
	N = range(20,100)
	b1 = 1
	b2 = 120
	ni = 14
	ki = 8
	di = 10
	loopNum = 100

	# for i in N:
	# 	mutliLoopTestResult(i, b1, b2, ni, ki, di, loopNum)
	plot.plot_change_N(N, b1, b2, ni, ki, di, loopNum)
if __name__ == '__main__':
#	test_change_b1()
