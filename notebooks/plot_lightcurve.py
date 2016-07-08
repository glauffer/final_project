'''
Programa para plotar a curva de luz e espaco de fase para uma cefeida,
os plot serao utilizados como exemplos no TCC
'''
import numpy as np
import matplotlib.pyplot as plt
import os


def rephase(data, period, shift=0.0, col=0, copy=True):
	'''
	transform the time of observations to the phase space
	'''
	rephased = np.ma.array(data, copy=copy)
	rephased[:, col] = get_phase(rephased[:, col], period, shift)
	return rephased

def get_phase(time, period, shift=0.0):
	'''
	divide the time of observations by the period
	'''
	return (time / period - shift) % 1


path = '/home/glauffer/Dropbox/FURG/final_project/data'
out = '/home/glauffer/Dropbox/FURG/final_project'
data = np.ma.array(data=np.loadtxt(os.path.join(path,
						'OGLE-LMC-CEP-0018.dat')), mask=None, dtype=float)
#data = np.ma.array(data=np.loadtxt(os.path.join(path,
#						'OGLE-LMC-T2CEP-003.dat')), mask=None, dtype=float)
#data2 = np.ma.array(data=np.loadtxt(os.path.join(path,
#						'OGLE-LMC-CEP-00032.dat')), mask=None, dtype=float)


fig= plt.figure()
plt.plot(data.T[0], data.T[1], 'ko')
plt.errorbar(data.T[0], data.T[1],
			yerr = data.T[2], linestyle="None",
			color = 'black')
fig.suptitle('Curva de Luz')
plt.xlabel('Tempo [JD]')
plt.ylabel('Magnitude I')
plt.gca().invert_yaxis()
fig.savefig(os.path.join(out,'0018_curva.png'),dpi=200)
plt.clf()
'''
r = rephase(data,  35.6599298, 0)
fig = plt.figure()
plt.plot(r.T[0],r.T[1], 'ro')
plt.plot(1+r.T[0], r.T[1], 'ro')
fig.suptitle('OGLE-LMC-T2CEP-003', fontsize = 18)
plt.xlabel('Fase',fontsize = 14)
plt.ylabel('Magnitude I',fontsize = 14)
plt.grid()
plt.gca().invert_yaxis()
#fig.savefig(os.path.join(out,'type2Cep.png'),dpi=200) # bbox_inches='tight')
plt.show()
#plt.clf()
'''
'''
p = 3.0123 #Wrong Period = 3.0123
r1= rephase(data, p, 0)
fig = plt.figure()
plt.plot(r1.T[0],r1.T[1], 'ro')
plt.plot(1+r1.T[0], r1.T[1], 'ro')
fig.suptitle('OGLE-LMC-CEP-0018', fontsize = 18)
plt.xlabel('Fase',fontsize = 14)
plt.ylabel('Magnitude I',fontsize = 14)
plt.grid()
plt.gca().invert_yaxis()
fig.savefig(os.path.join(out,'0018_wrong.png'),dpi=200) # bbox_inches='tight')
'''
