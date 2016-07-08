import numpy as np
import matplotlib.pyplot as plt

dados = np.array(np.loadtxt('/home/glauffer/Dropbox/FURG/final_project/data/rrab_ti_tf_pontos.txt'))

#Histograma t_i
fig,(ax,ax2) = plt.subplots(1, 2, sharey=True)
a, b, c = ax.hist(dados.T[0], bins=90)
ax2.hist(dados.T[0], bins=90)

ax.set_xlim(0,1000) # most of the data
ax2.set_xlim(2000,2500) # outliers only

# hide the spines between ax and ax2
ax.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax.yaxis.tick_left()
ax.tick_params(labeltop='off') # don't put tick labels at the top
ax2.yaxis.tick_right()

# Make the spacing between the two axes a bit smaller
plt.subplots_adjust(wspace=0.15)

d = .015 # how big to make the diagonal lines in axes coordinates
# arguments to pass plot, just so we don't keep repeating them
kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
ax.plot((1-d,1+d),(-d,+d), **kwargs) # top-left diagonal
ax.plot((1-d,1+d),(1-d,1+d), **kwargs) # bottom-left diagonal

kwargs.update(transform=ax2.transAxes) # switch to the bottom axes
ax2.plot((-d,d),(-d,+d), **kwargs) # top-right diagonal
ax2.plot((-d,d),(1-d,1+d), **kwargs) # bottom-right diagonal


#plt.title('Data Juliana $t_i$  RRab, max = %s'%b[np.argmax(a)])
#plt.suptitle('HJD $t_i$  max = %s'%b[np.argmax(a)], fontsize = 18)
plt.suptitle('Histograma - $t_i$', fontsize = 18)
#ax.set_ylabel('Frequência', fontsize = 14)
#ax2.set_xlabel('Tempo Inicial')

fig.text(0.5, 0.0, 'Tempo Inicial [JD]', ha='center', fontsize = 14)
fig.text(0.0, 0.5, 'Frequência', va='center', rotation='vertical', fontsize = 14)


print('t_i maximo = %s'%b[np.argmax(a)])
plt.savefig('hist_ti.png', dpi=200)
plt.clf()

#Histograma t_f
a, b, c = plt.hist(dados.T[1], bins=300)
plt.xlim(4300, 4600)
plt.suptitle('Histograma - $t_f$', fontsize=18)
plt.xlabel('Tempo Final [JD]', fontsize=14)
plt.ylabel('Frequência', fontsize=14)
plt.savefig('hist_tf.png', dpi=200)
print('t_f maximo = %s'%b[np.argmax(a)])
plt.clf()

#Histograma n
a, b, c = plt.hist(dados.T[2], bins=140)
plt.xlim(0,1400)
plt.title('Histograma - $n$', fontsize=18)
plt.xlabel('Quantidade de pontos', fontsize=14)
plt.ylabel('Frequência', fontsize=14)
b[np.argmax(a)]
plt.savefig('hist_n.png', dpi=200)
print('n maximo = %s'%b[np.argmax(a)])

