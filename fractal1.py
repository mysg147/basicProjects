import numpy as np
import matplotlib.pyplot as plt
import time
def mandlebrot(h,w,maxit=20):
    y,x=np.ogrid[-1.4:1.4:h*1j,-2:0.8:w*1j]
    c=x+y*1j
    z=c
    divtime =maxit +np.zeros(z.shape,dtype=int)
    for i in range(maxit):
        z=z**2+((c*(c))//2)+z
        diverge=z*np.conj(z)>2**2
        div_now=diverge & (divtime==maxit)
        divtime[div_now]=i
        z[diverge]=10
    return divtime

plt.imshow(mandlebrot(1000,1000))
plt.show()