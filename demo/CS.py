from ComplexStep import ComplexStep
from demo.demoFunct import *


cs = ComplexStep()
df1dx1 = cs.grad(f1,wrt=(0,1))
print(df1dx1(1.0,1.0))