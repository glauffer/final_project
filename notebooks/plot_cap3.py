import numpy as np
import matplotlib.pyplot as plt


def normalization(data):
	'''
	Normalize the magnitude of the star
	'''
	norm = np.ma.copy(data)
	norm[:,1] = (norm[:,1] - np.min(norm[:,1])) \
		/ (np.max(norm[:,1]) - np.min(norm[:,1]))

	return norm


def rephase(data, period, col=0, copy=True):
	'''
	transform the time of observations to the phase space
	'''
	rephased = np.ma.array(data, copy=copy)
	rephased[:, col] = get_phase(rephased[:, col], period)
	return rephased


def get_phase(time, period):
	'''
	divide the time of observations by the period
	'''
	return (time / period) % 1


data = np.array(np.loadtxt('/home/glauffer/Dropbox/FURG/final_project/data/OGLE-LMC-CEP-0018.dat'))

norm = normalization(data)
phased1 = rephase(norm, 4.0478)
#phased = rephase(norm, 2.2)
plt.plot(phased1.T[0], phased1.T[1], 'bo')
plt.xticks(np.linspace(0,1,11))
plt.grid()
plt.xlabel('Fase (P = 4,0478)', fontsize = 14)
plt.ylabel('Magnitude Normalizada', fontsize = 14 )
plt.title('OGLE-LMC-CEP-0018', fontsize = 18)
plt.savefig('esp_fase_correto.png', dpi = 200)


plt.clf()
phased2 = rephase(norm, 1.0)
plt.plot(phased2.T[0], phased2.T[1], 'bo')
plt.xticks(np.linspace(0,1,11))
plt.grid()
plt.xlabel('Fase (P = 1,0)', fontsize = 14)
plt.ylabel('Magnitude Normalizada', fontsize = 14 )
plt.title('OGLE-LMC-CEP-0018', fontsize = 18)
plt.savefig('esp_fase_1dia.png', dpi = 200)


plt.clf()
phased3 = rephase(norm, 3.0123)
plt.plot(phased3.T[0], phased3.T[1], 'bo')
plt.xticks(np.linspace(0,1,11))
plt.grid()
plt.xlabel('Fase (P = 3,0123)', fontsize = 14)
plt.ylabel('Magnitude Normalizada', fontsize = 14 )
plt.title('OGLE-LMC-CEP-0018', fontsize = 18)
plt.savefig('esp_fase_errado.png', dpi = 200)
