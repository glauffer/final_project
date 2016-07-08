import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii

#Sistema Binário
data = ascii.read('/home/glauffer/Dropbox/FURG/final_project/data/kplr001026032-2009166043257_llc.dat')
mag = -2.5 * np.log(data['col4'])

plt.plot(data['col1'], mag)
plt.gca().invert_yaxis()
plt.title('KIC 1026032', fontsize = 18)
plt.xlabel('Dias [JD]', fontsize = 14)
plt.ylabel('Magnitude', fontsize = 14)
plt.savefig('binary.png', dpi=200)

#Exoplaneta
kpl6b = ascii.read('/home/glauffer/Dropbox/FURG/final_project/data/kplr010874614-2009131105131_llc.dat')
mag6b = -2.5 * np.log(kpl6b['col4'])

plt.clf()
plt.plot(kpl6b['col1'], mag6b)
plt.gca().invert_yaxis()
plt.title('Kepler 6B - KIC 10874614', fontsize = 18)
plt.xlabel('Dias [JD]', fontsize = 14)
plt.ylabel('Magnitude', fontsize = 14)
plt.savefig('kepler6b.png', dpi=200)


#Supernova
sn = ascii.read('/home/glauffer/Dropbox/FURG/final_project/data/kplr008480662-2011271113734_llc.dat')
magSN = -2.5 * np.log(sn['col4'])

plt.clf()
plt.plot(sn['col1'], magSN)
plt.gca().invert_yaxis()
plt.title('KSN 2011a - KIC 8480662', fontsize = 18)
plt.xlabel('Dias [JD]', fontsize = 14)
plt.ylabel('Magnitude', fontsize = 14)
plt.savefig('sn2011a.png', dpi=200)