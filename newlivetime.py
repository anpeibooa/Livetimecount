# speed=8times of version1
import math,root_numpy,glob,timeit,multiprocessing,gc
import ROOT
import sys
from ROOT import TLine,TF1,std,TPolyLine3D,gStyle,TGraph
import ctypes,array
import numpy as np
from array import array
from ctypes import c_int,c_float

from root_numpy import root2array, tree2array
#channelID=ROOT.TH1D("channelID","channelID;channelID;counts",40,0,40)

#fname=[file for file in glob.glob("/var/phy/project/phil/shared/coherent/data/NaIvE/lowGainVetoProductionRun1/*.root")]

#print (fname[21])
fname1=[file for file in glob.glob("/var/phy/project/phil/shared/coherent/data/NaIvE/lowGainVetoProductionRun1/*_1.root")]
fname2=[file for file in glob.glob("/var/phy/project/phil/shared/coherent/data/NaIvE/lowGainVetoProductionRun2/*_1.root")]
fname3=[file for file in glob.glob("/var/phy/project/phil/shared/coherent/data/NaIvE/lowGainVetoProductionRun3/*_1.root")]
fname4=[file for file in glob.glob("/var/phy/project/phil/shared/coherent/data/NaIvE/lowGainVetoProductionRun4/*_1.root")]
fname5=[file for file in glob.glob("/var/phy/project/phil/shared/coherent/data/NaIvE/lowGainVetoProductionRun5/*_1.root")]
#fname6=[file for file in glob.glob("/var/phy/project/phil/shared/coherent/data/NaIvE/lowGainVetoProductionRun6/*.root")]
fname=fname1+fname2+fname3+fname4+fname5
start = timeit.default_timer()
print (len(fname))

#myarray=root2array(fname[0],'sis3302tree')
#rfile=ROOT.TFile(fname[0])
#intree=rfile.Get('sis3302tree')
#myarray=tree2array(intree,branches=['channelID'],selection='channelID==25')
#print (len(myarray))




def myget(f):


  dataFile = ROOT.TFile(fname[f],"R")
  
  N=0
  N2=dataFile.sis3302tree.GetEntries()-1
  dataFile.sis3302tree.GetEntry(N)
  T1=dataFile.sis3302tree.timestamp
  dataFile.sis3302tree.GetEntry(N2)
  T2=dataFile.sis3302tree.timestamp
  RunT=np.float((T2-T1)*10.0/10.0**9.0/3600.0)
  
  
  
  
  intree=dataFile.Get('sis3302tree')
  myarray=tree2array(intree,branches=['channelID'],selection='channelID==25')
  dataFile.Close()
  print ("Run time is "+str.format('{0:.6}',RunT)+" hours")
  print ("There are "+str(len(myarray))+" event61s in "+str(fname[f]))
  return (len(myarray),RunT, f, fname[f])

  



pool = multiprocessing.Pool(4)    
result=pool.map(myget,list(range(1469)))

  

stop = timeit.default_timer()
#print (countersum[:10])    
print('Time: ', stop - start)  
#print (result)
np.savez('newEvent61',a=result)

try:
	input("Press enter to continue")
except SyntaxError:
	pass








