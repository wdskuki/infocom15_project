'''
Created on Jul 12, 2014
@author: Dongsheng Wei(12210240069@fudan.edu.cn)
'''
import random

def randomSelectNewComer(N, Ni, fnodei):
	backNewComers = list(set(range(N)) - set(Ni + [fnodei]))
	print backNewComers
	newcomer = random.choice(backNewComers)
	return newcomer

def randomSelectProviders(Ni, di):
	providers = random.sample(Ni, di)
	return providers

def randomSelectProviderNewComer(G, N, Ni, fnodei, di):
	backNewComers = list(set(range(N)) - set(Ni + [fnodei]))
	newcomer = random.choice(backNewComers)
	return newcomer, providers

