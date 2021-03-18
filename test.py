import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0,10,100)
b = np.sin(a)

plt.figure()
plt.plot(a,b)
plt.savefig('test.png')