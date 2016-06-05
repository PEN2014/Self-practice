import matplotlib.pyplot as plt
import numpy as np

N = 30
n = np.arange(0.001, N/2, 1.0/N)
s = (n-2)*(n-2)-np.log(n)



plt.plot(n, s)
plt.axis([0, 8, -10, 10])
plt.show()