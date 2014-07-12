'''
Created on Jul 10, 2014
@author: Dongsheng Wei(12210240069@fudan.edu.cn)
'''

import random
import itertools
import time
import fullWeightedGraph as fwg

def spfnSelectNewComer(N, Ni, fnodei):
	backNewComers = list(set(range(N)) - set(Ni + [fnodei]))
	newcomer = random.choice(backNewComers)
	return newcomer

def spfnSelectProviders(Ni, di):
	providers = random.sample(Ni, di)
	return providers