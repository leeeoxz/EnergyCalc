# Leonardo Santos #
# June 2017 #

import copy
import math
import numpy as np

class itpRead ():
	everything= [] #ALL FILE CONTENT
	titleSym = ["[ atomtypes ]"] #TITLE SYMBOL
	columnNameSym = [";"] #COLUMN NAME SYMBOL
	content = [] #CONTENT OF FILE
	titles = [] #TITLES
	columnNames = [] #COUMN NAMES
	dictionary = {} #ATOMS DICTIONARY dic[ATOM1ATOM2]:{EPSLON I J,R MIN I, R MIN J, R MIN IJ}

	def __init__(self,FileName):
		file = open(FileName,"r")
		for line in file:
			self.everything.append(line)
			if line.replace("\n","") in self.titleSym:
				self.titles.append(line.replace("[","").replace("]","").replace("\n","").replace(" ",""))
			elif (line[0] not in self.columnNameSym) & (line.replace("\n","") not in self.titleSym):
				self.content.append(line.replace("\n","").split()) 
			elif (line[0] in self.columnNameSym) & (not self.columnNames):
				self.columnNames.append(line)
			else:
				break
		self.createDic()

	def epslonIJ(self,epsi,epsj): # GETS EPSLON I AND J
		eij= math.sqrt(epsi*epsj)
		return eij

	def rmin(self, sigma):
		r = sigma*(2**(1/6))
		return r

	def rIJ(self,pi,pj):
		pi_array = np.array(pi)
		pj_array = np.array(pj)
		return np.linalg.norm(pi_array-pj_array)/10.

	def rminIJ(self,rmini,rminj):
		return (rmini+rminj)/2

	def uijLJ(self, epsij, rij, rminij):
		u = epsij*(((rminij/rij)**12)-(2*((rminij/rij)**6)))
		return u

	def getEpslonOne(self):
		e = 9*(10e9)*((1.6022*10e-19)/10e-9)*((6.022140857*10e23)/1000)
		return e

	def createDic(self):
		for x,item in enumerate(self.content):
			for y,item1 in enumerate(self.content[x:]):
				epsIJ = self.epslonIJ(float(item[6]),float(item1[6]))
				rmini = self.rmin(float(item[5]))
				rminj = self.rmin(float(item1[5]))
				rminij = self.rminIJ(rmini,rminj)
				self.dictionary[item[0]+item1[0]] =[epsIJ,rmini,rminj,rminij]

	def getDic(self):
		return copy.deepcopy(self.dictionary)