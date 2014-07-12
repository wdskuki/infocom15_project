'''
Created on Jul 10, 2014
@author: Dongsheng Wei(12210240069@fudan.edu.cn)
'''

#generage a N node's full connected graph with random weights links

import random
import itertools
import time
import fullWeightedGraph as fwg

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

def spsnSelectProviderNewComer(G, N, Ni, fnodei, di):
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

