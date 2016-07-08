import numpy as np
import matplotlib.pyplot as plt
import astropy.coordinates as coord
import astropy.units as u
from mpl_toolkits.mplot3d import Axes3D

#Ler a tabela de dados com RA e Dec de cada RRLyr AB
# a estrela OGLE-LMC-RRLYR-15485 (posição 11013 no arquivo) não possui DatabaseNumber, estava dando problema para ler os dados. Coloquei manualmente o valor 0000
from astropy.io import ascii
tbl = ascii.read('/home/glauffer/Dropbox/FURG/final_project/data/identification_onlyRRAB.dat', guess=False, Reader=ascii.Tab, header_start = 0, data_start = 1)

#Converter RA de horas para graus
ra = coord.Angle(tbl['RA'], unit = u.hour)

#Converter Dec em graus
dec = coord.Angle(tbl['Dec'], unit = u.degree)

#Converter RA e Dec em X e Y de acordo com o paper do Pejcha (2009)
x = (ra.degree - 80.35) * np.cos(dec.degree)
y = dec.degree + 69.68
ra_dec = np.around(np.column_stack((x,y)), decimals=1) #arrendondamento para o primeiro decimal apos a virgula

#Ler os dados do extinction map
ext_map = np.array(np.loadtxt('/home/glauffer/Dropbox/FURG/final_project/data/extinction_map/lmcextmap.dat', skiprows=29))

#Separar os valor x_min, x_max e y_min, y_max
x_map = np.column_stack((ext_map.T[0], ext_map.T[1]))
y_map = np.column_stack((ext_map.T[2], ext_map.T[3]))

#Buscar os valores das extincoes
ext = np.ones(len(ra_dec))
for i in range(len(ra_dec)):
    if ra_dec[i,0]>(-4.7): # or ():
        ext[i] = 0
    if ra_dec[i,0]>4.9:
        ext[i] = 0
    if ra_dec[i,1]>(-3.4): #or 
        ext[i] = 0
    if ra_dec[i,1]>3.2:
        ext[i] = 0
    else:
        try:
            ext[i] = ext_map[np.where((x_map.T[0] == ra_dec[i,0]) & (y_map.T[0] == ra_dec[i,1]))][0][4]
        except IndexError:
            ext[i] = 0

#Ler os dados de magnitude das RRLYR AB
#Nome MagI MagV OGLE_period RA DEC CE_period...
magI = ascii.read('/home/glauffer/Dropbox/FURG/final_project/data/ID_mag_Period_RA_DE.dat')

#Corrigir as magnitude pela extincao
magI_correct = magI['col2'] - 1.10*ext
np.savetxt('rrab_mag_corrected.txt', magI_correct, fmt='%s')
'''
#Least squares regression for PL relation
A = np.column_stack((np.log(magI['col7']), np.ones_like(magI['col7'])))
x, res, rank, s = np.linalg.lstsq(A,magI_correct)
#print('m - A= ', x[0], '*log P + ', x[1])

#Plot da dispersao de mag vs log(P) e relacao PL
plt.plot(np.log(magI['col7']), magI_correct, 'bo', ms=0.4)
plt.plot(np.log(magI['col7']), x[0]*np.log(magI['col7']) + x[1], 'r-', label='m - A= %f*log P +%f'%(x[0],x[1]))
plt.gca().invert_yaxis()
plt.legend()
plt.xlabel(r'$\log (P)$', fontsize = 14)
plt.ylabel('Magnitude', fontsize = 14)
plt.title('Relação PL', fontsize = 18)
plt.xlim(-2.0,0)
plt.savefig('relacao_pl.png', dpi = 200)

#Calculando o modulo de distancia u e a distacia r
u = np.zeros(len(magI_correct))
u = magI_correct - x[0]*np.log(magI['col7'])-x[1]
r = np.zeros(len(u))
r = 10**(0.2*u+0.2*5)

#sendo a distancia media 50 kpc -> r_lmc = r+50
r_lmc = np.zeros(len(r))
r_lmc = r + 40

#Calculando as coordenadas x, y, z
x, y, z = np.zeros(len(r_lmc)), np.zeros(len(r_lmc)), np.zeros(len(r_lmc))
r_lmc_0 = 40
ra_0 = 0
dec_0 = 0

#x = -r_lmc * np.sin(ra.degree - ra_0) * np.cos(dec.degree)
#y = r_lmc * np.sin(dec.degree)*np.cos(dec_0) - r_lmc * np.sin(dec_0) * np.cos(ra.degree - ra_0) * np.cos(dec.degree)
#z = r_lmc_0 - r_lmc * np.sin(dec.degree) * np.sin(dec_0) - r_lmc * np.cos(dec_0)*np.cos(ra.degree) - ra_0 * np.cos(dec.degree)
x = -r_lmc * np.sin(ra.radian - ra_0) * np.cos(dec.radian)
y = r_lmc * np.sin(dec.radian)*np.cos(dec_0) - r_lmc * np.sin(dec_0) * np.cos(ra.radian - ra_0) * np.cos(dec.radian)
z = r_lmc_0 - r_lmc * np.sin(dec.radian) * np.sin(dec_0) - r_lmc * np.cos(dec_0)*np.cos(ra.radian) - ra_0 * np.cos(dec.radian)
#z = r_lmc * np.sin(dec.radian)*np.cos(dec_0) - r_lmc * np.sin(dec_0) * np.cos(ra.radian - ra_0) * np.cos(dec.radian)
#y = r_lmc_0 - r_lmc * np.sin(dec.radian) * np.sin(dec_0) - r_lmc * np.cos(dec_0)*np.cos(ra.radian) - ra_0 * np.cos(dec.radian)

#Plot3D
plt.clf()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.plot(x, y, z, 'bo' ,ms=0.8)
ax.set_xlabel('X [kpc]')
ax.set_ylabel('Y [kpc]')
ax.set_zlabel('Z [kpc]')
plt.show()
'''