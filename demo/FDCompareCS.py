import numpy as np
import scipy.linalg as linalg
import matplotlib.pyplot as plt
from demo.demoFunct import *

x1 = np.pi/4
x2 = 1
stepsize = np.array([0.1**x for x in range(1,20)])

errorFD = np.zeros(shape=stepsize.shape)
errorCS = np.zeros(shape=stepsize.shape)

exactSol = exactDf1Dx1(x1,x2)

for idx,val in enumerate(stepsize):
    f1_val = f1(x1,x2)
    f1_new = f1(x1+val,x2)
    errorFD[idx] = ((f1_new-f1_val)/val-exactSol)/exactSol
    errorCS[idx] = (np.imag(f1(x1+complex(0,1)*val,x2))/val-exactSol)/exactSol

plt.loglog(stepsize,abs(errorFD),'r')
plt.loglog(stepsize,abs(errorCS),'b')
plt.gca().invert_xaxis()
plt.legend(['FD','CS'])
plt.xlabel('h')
#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')
plt.ylabel(r'Relative error $\frac{\partial{f1}}{\partial{x1}}|_{x=[\frac{\pi}{4}, 1]}$')
plt.title('Relative error compared between FD and CS')
plt.grid('on')
plt.gca().xaxis.label.set_size(16)

plt.gca().yaxis.labelpad = -5
plt.gca().yaxis.label.set_size(16)
plt.gca().title.set_size(16)
plt.gca().xaxis.labelpad = -5
plt.savefig('FD_vs_CS.eps')
plt.show()



