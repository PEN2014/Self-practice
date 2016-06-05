import matplotlib.pyplot as plt
import numpy as np

N = 30
n = np.arange(-N/2, N/2, 1.0/N)
s = np.exp(n)-3*n*n



plt.plot(n, s)
plt.axis([-6, 6, -10, 10])
plt.show()