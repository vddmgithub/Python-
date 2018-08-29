"""
Consider a random 10 x 2 matrix representing Cartesian
coordinates, convert them to Polar coordinates.
Basically we need show them (r, Theta)
"""

import numpy as np
z= np.random.random((10,2))
x,y = z[:,0], z[:,1]
r = np.sqrt(x**2+y**2)
t = np.arctan2(y,x)
print(r)
print(t)

"""
Create random vector of size 50 and replace the maximum value
by 0 and minimum value by 100.
"""
import numpy as np
x = np.random.random(50)
print("Original array:")
print(x)
x[x.argmax()] = 0
x[x.argmin()] =100
print(x)


"""
Create below matrix using scipy.
"""
import numpy as np
d = np.eye(10) * 2
d1 = np.diag(np.ones(8),2)
d2 = np.diag(np.ones(8),-2)
d1 = d1.__add__(d2)
d = d.__add__(d1)
print (d)



"""
Reproduce given plot by correcting the below code.
"""
from pylab import *
n = 256
X = np.linspace(-np.pi,np.pi,n,endpoint=True)
Y = np.sin(2*X)
plot (X, Y+1, color='blue', alpha=0.8, fillstyle="full")
plt.fill_between(X, 1, Y + 1, color='blue', alpha=.25)
plot (X, Y-1, color='blue', alpha=0.8, linestyle='solid')
plt.fill_between(X, -1, Y - 1, (Y - 1) > -1, color='blue', alpha=.25)
plt.fill_between(X, -1, Y - 1, (Y - 1) < -1, color='red',  alpha=.25)
show()

