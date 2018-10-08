from FiniteDifference.FiniteDifference import *

fd = FiniteDifference()
fd.addVariable(name='x1')
fd.addVariable(name='x2')
fd.addOutput(name='f1')
fd.addEquation(equation='f1 = x1+x2')
fd.addDiffPoint([1,1])
fd.dYdX(X=['x1'],Y=['f1'])
