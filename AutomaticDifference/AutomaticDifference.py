import tangent
from Component.Equation import Equation
import numpy as np

class AutomaticDifference(Equation):
    def __init__(self):
        self.method = "Automatic Difference"
        pass
    def __repr__(self):
        return super(AutomaticDifference,self).__repr__() + "\n method = " + self.method

    def grad(self, funct, wrt=(0,), verbose=0):
        """
        :param funct: top-level function hander
        :param wrt: tuple, define the desired interest, default is first (0)
        :param verbose: output the source code of computing derivatives
        :return: df dwrt
        """
        derivatives = tangent.grad(funct, wrt=wrt, verbose=verbose)
        return derivatives