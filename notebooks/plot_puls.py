import numpy as np
import matplotlib.pyplot as plt

f =  2.0
omega = 2 * np.pi / f
t = np.linspace(0, 1, 100, endpoint = True)

plt.plot(t, np.sin(1 * omega * t), t, -np.sin(1 * omega * t), '--r', linewidth=1.5)
plt.xticks([])
plt.yticks([])
plt.ylim(-1.5, 1.5)
#plt.title('Frequência Fundamental')
plt.savefig('pulsacao_1d_corda_fu.png', dpi = 100, bbox_inches='tight')
plt.clf()

plt.plot(t, np.sin(2 * omega * t), t, -np.sin(2 * omega * t), '--r', linewidth=1.5)
plt.xticks([])
plt.yticks([])
plt.ylim(-1.5, 1.5)
#plt.title('Primeiro Harmônico')
plt.savefig('pulsacao_1d_corda_FO.png', dpi = 100, bbox_inches='tight')
plt.clf()

plt.plot(t, np.sin(3 * omega * t), t, -np.sin(3 * omega * t), '--r', linewidth=1.5)
plt.xticks([])
plt.yticks([])
plt.ylim(-1.5, 1.5)
#plt.title('Segundo Harmônico')
plt.savefig('pulsacao_1d_corda_SO.png', dpi = 100, bbox_inches='tight')
plt.clf()

plt.plot(t, np.sin(0.5 * omega * t), t, -np.sin(0.5 * omega * t), '--r', linewidth=1.5)
plt.xticks([])
plt.yticks([])
plt.ylim(-1.5, 1.5)
#plt.title('Frequência Fundamental')
plt.savefig('pulsacao_1d_sopro_FU.png', dpi = 100, bbox_inches='tight')
plt.clf()

plt.plot(t, np.sin(1.5 * omega * t), t, -np.sin(1.5 * omega * t), '--r', linewidth=1.5)
plt.xticks([])
plt.yticks([])
plt.ylim(-1.5, 1.5)
#plt.title('Primeiro Harmônico')
plt.savefig('pulsacao_1d_sopro_FO.png', dpi = 100, bbox_inches='tight')
plt.clf()

plt.plot(t, np.sin(2.5 * omega * t), t, -np.sin(2.5 * omega * t), '--r', linewidth=1.5)
plt.xticks([])
plt.yticks([])
plt.ylim(-1.5, 1.5)
#plt.title('Segundo Harmônico')
plt.savefig('pulsacao_1d_sopro_SO.png', dpi = 100, bbox_inches='tight')
plt.clf()