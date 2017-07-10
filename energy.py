# Leonardo Santos #
# June 2017 #

import copy
import math
import numpy as np
from aminoacids_rtp import rtpRead as rtpr 
from nonBonded import itpRead as itpr 
from PDB_read import PDB_read as pdb

x=[]
dictionary_nonbonded = itpr("ffnonbonded.itp").getDic() #ATOMS DICTIONARY dic[ATOM1ATOM2]:{EPSLON I J,R MIN I, R MIN J, R MIN IJ}
dictionary_aminoacid = rtpr("aminoacids.rtp").getDic() #AMINO ACID DICTIONARY dic["AA"] = {atoms:{DICTIONARY WITH ATOMS NAME SUBSTITUITION},bonds:{DICTIONARY WITH ATOM'S BOND}}
pdb_file = pdb("NLYIQWLKDGGPSSGRPPPS.pdb").getAtom()
for item in pdb_file:
	for i in dictionary_aminoacid[item[3]][0]:
		if item[2] in i:
			x.append(i[1])
print len(x)