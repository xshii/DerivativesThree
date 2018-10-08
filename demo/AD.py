import numpy as np
from demo.demoFunct import *
from AutomaticDifference import AutomaticDifference

ad = AutomaticDifference()
df1dx1 = ad.grad(f1,wrt=(0,))
print(df1dx1(1.0,1.0))
exactSol = exactDf1Dx1(1.0,1.0)
print(df1dx1(1.0,1.0) - exactSol)
