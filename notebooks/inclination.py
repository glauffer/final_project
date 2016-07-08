import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

ab = np.array(np.loadtxt('ab_plot.txt'))
c = np.array(np.loadtxt('c_plot.txt'))
fu= np.array(np.loadtxt('fu_plot.txt'))
#fu= np.array(np.loadtxt('fu50e3_plot.txt'))
fo = np.array(np.loadtxt('fo_plot.txt'))


x_all_1 = np.insert(c.T[0], [0],ab.T[0])#, ra_cepfo.degree)
x_all_2 = np.insert(x_all_1, [0], fo.T[0])
x_all = np.insert(x_all_2, [0], fu.T[0])

y_all_1 = np.insert(c.T[1], [0],ab.T[1])#, ra_cepfo.degree)
y_all_2 = np.insert(y_all_1, [0], fo.T[1])
y_all = np.insert(y_all_2, [0], fu.T[1])

z_all_1 = np.insert(c.T[2], [0],ab.T[2])#, ra_cepfo.degree)
z_all_2 = np.insert(z_all_1, [0], fo.T[2])
z_all = np.insert(z_all_2, [0], fu.T[2])

#print(len(x_all), len(y_all), len(z_all))
A_all = np.column_stack((np.ones(x_all.size), x_all, y_all))
c_all, resid_all, rank_all, sigma_all = np.linalg.lstsq(A_all,z_all)

inclination = np.arccos(1 / np.sqrt(1 + c_all[0]**2 + c_all[1]**2))
theta = np.arctan( -c_all[0] / c_all[1]) + np.sign(c_all[2]) * np.pi / 2

#from matplotlib.patches import Ellipse
#elli = Ellipse(xy=[0], width=[2], height=[1], angle=[np.rad2deg(inclination)])
#fig = plt.figure()
##ax = fig.add_subplot(111, aspect='equal')
##for e in elli:
##    ax.add_artist(e)
#ax.add_artist(elli)
#plt.plot(x_all, y_all, '.', ms=0.5)
##plt.gca().add_artist(elli)

##plt.plot(c_all[0]*x_all - c_all[2], c_all[1]*y_all - c_all[2], '.', color='green')
plt.show(True)
