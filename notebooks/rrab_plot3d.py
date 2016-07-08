import numpy as np
import matplotlib.pyplot as plt
import astropy.coordinates as coord
import astropy.units as u
from astropy.io import ascii
from mpl_toolkits.mplot3d import Axes3D

tbl = ascii.read('/home/glauffer/Dropbox/FURG/final_project/data/identification_onlyRRAB.dat', guess=False, Reader=ascii.Tab, header_start=0, data_start=1)

#Converter RA de horas para graus
ra = coord.Angle(tbl['RA'], unit = u.hour)

#Converter Dec em graus
dec = coord.Angle(tbl['Dec'], unit = u.degree)

#Ler os dados de magnitude das RRLYR AB
#Nome MagI MagV OGLE_period RA DEC CE_period...
magI = ascii.read('/home/glauffer/Dropbox/FURG/final_project/data/ID_mag_Period_RA_DE.dat')

#Ler os dados de magnitude corrigido das RRLYR AB
magI_correct = np.array(np.loadtxt('/home/glauffer/Dropbox/FURG/final_project/data/rrab_mag_corrected.txt'))

#Least squares regression for PL relation
A = np.column_stack((np.log(magI['col7']), np.ones_like(magI['col7'])))
x, res, rank, s = np.linalg.lstsq(A,magI_correct)

#Calculando o modulo de distancia u e a distacia r
u = np.zeros(len(magI_correct))
u = magI_correct - x[0]*np.log(magI['col7'])-x[1]
r = np.zeros(len(u))
r = 10**(0.2*u+0.2*5)

#sendo a distancia media 50 kpc -> r_lmc = r+50
r_lmc = np.zeros(len(r))
r_lmc = r + 50

#Calculando as coordenadas x, y, z
x, y, z = np.zeros(len(r_lmc)), np.zeros(len(r_lmc)), np.zeros(len(r_lmc))
r_lmc_0 = 50
ra_0 = np.mean(ra.radian)
dec_0 = np.mean(dec.radian)

x = -r_lmc * np.sin(ra.radian - ra_0) * np.cos(dec.radian)
y = r_lmc * np.sin(dec.radian)*np.cos(dec_0) - r_lmc * np.sin(dec_0) * np.cos(ra.radian - ra_0) * np.cos(dec.radian)
z = r_lmc_0 - r_lmc * np.sin(dec.radian) * np.sin(dec_0) - r_lmc * np.cos(dec_0)*np.cos(ra.radian) - ra_0 * np.cos(dec.radian)
#z = r_lmc * np.sin(dec.radian)*np.cos(dec_0) - r_lmc * np.sin(dec_0) * np.cos(ra.radian - ra_0) * np.cos(dec.radian)
#y = r_lmc_0 - r_lmc * np.sin(dec.radian) * np.sin(dec_0) - r_lmc * np.cos(dec_0)*np.cos(ra.radian) - ra_0 * np.cos(dec.radian)

#Plot3D
#plt.clf()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.plot(x, y, z, 'bo', ms=0.5)
ax.set_xlabel('X [kpc]')
ax.set_ylabel('Y [kpc]')
ax.set_zlabel('Z [kpc]')
plt.show()
