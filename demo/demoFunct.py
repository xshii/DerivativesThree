import numpy as np

def exactDf1Dx1(x1,x2):
    det = 1.0/(x2+2)
    return det*x2*(np.cos(x1)**2-2*x1*np.sin(x1)*np.cos(x1))

def Y1Y2(x1,x2):
    det = 1.0/(x2+2)
    y1 = det * x2*np.cos(x1)
    y2 = det * (-np.cos(x1))
    return y1,y2

def f1(x1,x2):
    y1,y2 = Y1Y2(x1, x2)

    return y1*x1*np.cos(x1)

def f2(x1,x2):
    y1, y2 = Y1Y2(x1, x2)
    return y2*np.sin(x1)