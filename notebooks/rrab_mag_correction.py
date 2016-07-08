'''
Programa para corrigir as magnitudes das RRLYR AB em relacao a extincao estelar
'''
import numpy as np
import matplotlib.pyplot as plt
import astropy.coordinates as coord
import astropy.units as u

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
