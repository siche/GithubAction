import numpy as np
import time
import matplotlib.pyplot as plt

a = np.linspace(0,10,100)
b = np.sin(a)

plt.figure()
t1 = time.time()
plt.plot(a,b)
plt.savefig('test.png')
t2 = time.time()
print("time cost:%s" % (t2-t1))
