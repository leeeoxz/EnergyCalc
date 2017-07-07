# Leonardo Santos #
# June 2017 #

import copy
import math
import numpy as np

class rtpRead ():
	everything= [] #ALL FILE CONTENT
	aminoacids = ["ARG","HIS","LYS","ASP","GLU","SER","THR","ASN","GLN","CYS","GLY","PRO","ALA","ILE","LEU","MET","PHE","TRP","TYR","VAL"]

	def __init__(self,FileName):
		file = open(FileName,"r")
		for line in file:
			if not line.replace("\n","").replace("[","").replace("]","").split():
				pass
			#print line.replace("\n","").replace("[","").replace("]","").split()
			else:
				self.everything.append(line.replace("\n","").replace("[","").replace("]","").split())
		for line in self.everything:
			if line[0] in self.aminoacids:
				print line[0]

#guardar os indices, de todos os items, dai depois disso percorre a partir daquele indice pra pegar os atomos com as cargas e os ligantes #


rtpRead("aminoacids.rtp")