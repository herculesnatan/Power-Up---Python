import matplotlib.pyplot as plt
import numpy as np

# Definindo o tempo
t = np.linspace(-2, 2, 100)

# Função degrau unitário
def u(t):
    return np.where(t >= 0, 1, 0)

# Plotando os sinais
plt.subplot(3, 1, 1)
plt.plot(t, u(t))
plt.title('x(t)')

plt.subplot(3, 1, 2)
plt.plot(t, u(t-1))
plt.title('x(t-1)')

plt.subplot(3, 1, 3)
plt.plot(t, 2*u(t)+2)
plt.title('2x(t) + 2')

plt.tight_layout()
plt.show()