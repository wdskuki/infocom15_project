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

	# The shallow copies
	# return [[0]*N]*N
	return [[0]*N for i in range(N)] # deep copies

# Input: 
#	Graph struct
#	 Weight Range
# Output: 
#	Weighted graph struct
def randomLinkWeight(G, (b1, b2)):
	# print G
	row = len(G)
	col = len(G[0])
	if row == 0 or b1 > b2 or b1 < 0:
		print 'error: in randomLinkWeight()'
		return G

	for i in range(row):
		for j in range(col):
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

# Input: 
#	Graph struct
#	a node
# 	a node set
# Output:
#	minimum weighted link value between the node to the node's set
def getBottleNetBW(G, newcomer, providers):
	bottleNetBW = G[providers[0]][newcomer]
	bottleLinkNode = providers[0]
	for i in providers:
		if bottleNetBW > G[i][newcomer]:
			bottleNetBW = G[i][newcomer]
			bottleLinkNode = i
	return bottleNetBW, bottleLinkNode