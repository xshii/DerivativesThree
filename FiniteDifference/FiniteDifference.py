from Component.Equation import Equation


class FiniteDifference(Equation):
    def __init__(self):
        self.method = "Finite Differnce"
        pass
    def __repr__(self):
        return super(FiniteDifference,self).__repr__() + "\n method = " + self.method

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
                    newList = head+(desired+stepsize,)+tail
                    result.append((funct(*newList)-funct(*list))/stepsize)
            return result
        return derivatives