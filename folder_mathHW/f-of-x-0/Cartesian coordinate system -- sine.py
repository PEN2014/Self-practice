import matplotlib.pyplot as plt
import numpy as np

N = 80
n = np.arange(-N/2, N/2, 1.0/N)
s = 2*n*np.cos(2*n)-(n-2)*(n-2)

plt.plot(n, s)
plt.axis([-5, 30, -530, 20])
plt.show()