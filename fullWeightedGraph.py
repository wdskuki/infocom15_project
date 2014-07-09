'''
Created on Jul 10, 2014
@author: Dongsheng Wei(12210240069@fudan.edu.cn)
'''

import random
import itertools
import time

# Input: number of nodes
# Output: Graph struct
def fullConnectedGraph(N = 0):
	return [[0]*N]*N

# Input: 
#	Graph struct
#	 Weight Range
# Output: 
#	Weighted graph struct
def randomLinkWeight(G, (b1, b2)):
	if len(G) == 0 or b1 > b2 or b1 < 0:
		print 'error: in randomLinkWeight()'
		return G

	for i in range(len(G)):
		for j in range(len(G[i])):
			G[i][j] = random.uniform(b1, b2)
	return G

# Input: 
#	number of nodes
#	number of a specific nodes set
# Output:
#	specific nodes set
def randomSelectBlocksStoredNodes(N, ni):
	if ni > N or ni <= 0 or N <= 0:
		print 'error: in randomSelectBlocksStoredNodes()'
		return []
	return random.sample(range(N), ni)

# Input: set of nodes
# Output: a random node in the input set
def randomFailedStoredNode(Ni):
	if Ni == []:
		print 'error: in randomFailedStoredNode()'
		return -1
	fnodei = random.choice(Ni)
	Ni.remove(fnodei)
	return fnodei, Ni