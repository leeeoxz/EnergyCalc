# Leonardo Santos #
# June 2017 #

import copy
import math
import numpy as np

class rtpRead ():
	everything= [] #ALL FILE CONTENT
	aminoacids = ["ARG","HIS","LYS","ASP","GLU","SER","THR","ASN","GLN","CYS","GLY","PRO","ALA","ILE","LEU","MET","PHE","TRP","TYR","VAL"]
	caminoacids = ["CARG","CHIS","CLYS","CASP","CGLU","CSER","CTHR","CASN","CGLN","CCYS","CGLY","CPRO","CALA","CILE","CLEU","CMET","CPHE","CTRP","CTYR","CVAL"]
	naminoacids = ["NARG","NHIS","NLYS","NASP","NGLU","NSER","NTHR","NASN","NGLN","NCYS","NGLY","NPRO","NALA","NILE","NLEU","NMET","NPHE","NTRP","NTYR","NVAL"]
	index = [] #just a list of index and items
	dictionary = {}
	def __init__(self,FileName):
		file = open(FileName,"r")
		for line in file:
			if not line.replace("\n","").replace("[","").replace("]","").split():
				pass
			else:
				self.everything.append(line.replace("\n","").replace("[","").replace("]","").split())
		self.everything = self.everything[139:] #STARTS FROM THE FISRT AMINO ACID
		self.getIndex()
		self.setDicOfAA()


	def getIndex(self): #SETS A INDEX LIST [[AMINO ACID, INDEX, START ATOMS' INDEX, END OF ATOMS/START BONDS' INDEX, END OF BONDS]]
		bonds = [] #GETS THE INDEX WHERE THE BONDS STARTS
		finish = [] #GETS THE INDEX WHERE THE BONDS ENDS
		for i,line in enumerate(self.everything):
			if line[0] in self.aminoacids:
				self.index.append([line[0],i,i+1])
				p = i
			elif line[0] in self.caminoacids:
				self.index.append([line[0],i,i+1])
				p = i
			elif line[0] in self.naminoacids:
				p = i
				self.index.append([line[0],i,i+1])
			elif (line[0] == 'bonds'):
				bonds.append(i)
			elif line[0] == 'impropers':
				finish.append(i)
		for i,item in enumerate(self.index):
			for bond in bonds:
				if bond > item[2]:
					item.append(bond)
					break
		for i,item in enumerate(self.index):
			for fin in finish:
				if fin > item[3]:
					item.append(fin)
					break

	def setDicOfAA(self):
		for item in self.index:
			self.dictionary[item[0]] = [self.everything[item[2]:item[3]],self.everything[item[3]:item[4]]]


	def getDic(self):
		return copy.deepcopy(self.dictionary)


rtpRead("aminoacids.rtp")