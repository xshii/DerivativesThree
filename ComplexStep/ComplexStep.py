from Component.Equation import Equation
import numpy as np

class ComplexStep(Equation):
    def __init__(self):
        self.method = "Complex Step"
        pass
    def __repr__(self):
        return super(ComplexStep,self).__repr__() + "\n method = " + self.method

    def grad(self, funct, wrt=(0,), stepsize=1e-10, direction='fwd'):
        """
        :param funct: top-level function hander
        :param wrt: tuple, define the desired interest, default is first (0)
        :param stepsize: perturbation
        :param direction: 'fwd', 'bwd','center'
        :return:
        """
        def derivatives(*list):
            result = []
            for idx in wrt:
                head, desired, tail = list[0:idx], list[idx],list[idx+1:]
                if direction == 'fwd':
                    newList = head+(desired+complex(0,stepsize),)+tail
                    result.append(np.imag(funct(*newList))/stepsize)
            return result
        return derivatives