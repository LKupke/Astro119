'''script that tests numpy functionality'''
import numpy as np
#vector notation is this instead of for loop in append test?
N=10
start=1
stop=10 #stopping value -1
step=1
aV=np.arange(start,stop+1,step)
print(aV)
av2=np.linspace(start,stop,N, dtype=int)
print (av2)

#why do same length vectors allign while unequal vectors don't
