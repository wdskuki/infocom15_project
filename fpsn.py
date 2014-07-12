'''
Created on Jul 10, 2014
@author: Dongsheng Wei(12210240069@fudan.edu.cn)
'''

import random
import itertools
import time
import fullWeightedGraph as fwg


def fpsnSelectNewComer(G, N, Ni, fnodei, providers):
	backNewComers = list(set(range(N)) - set(Ni + [fnodei]))
	bottleNetBW = -1.0
	newcomer = -1

	for nc in backNewComers:
		tmpBottleNetBW = min([G[j][nc] for j in providers])
		if tmpBottleNetBW > bottleNetBW:
			bottleNetBW = tmpBottleNetBW
			newcomer = nc
	return newcomer

def fpsnSelectProviders(Ni, di):
	providers = random.sample(Ni, di)
	return providers

