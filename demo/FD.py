import numpy as np
from FiniteDifference import FiniteDifference
from demo.demoFunct import *


fd = FiniteDifference()
df1dx1 = fd.grad(f1,wrt=(0,1))
print(df1dx1(1.0,1.0))