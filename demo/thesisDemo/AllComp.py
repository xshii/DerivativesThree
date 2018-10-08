from openmdao.api import ExplicitComponent
import numpy as np
class Y1Comp(ExplicitComponent):
    def setup(self):
        self.add_input('x1', 1.0)
        self.add_input('x2', 1.0)
        self.add_output('y1', 1.0)
        self.declare_partials('*', '*', method='fd')

    def compute(self, inputs, outputs):
        """
        Evaluates the equation
        y1 = 1/det*x2**2*sin(x1)
        :param inputs:
        :param outputs:
        :return:
        """
        x1 = inputs['x1']
        x2 = inputs['x2']
        det = (2.0 + x1 * x2**2)
        outputs['y1'] = 1.0 / det * x2**2 * np.sin(x1)


class Y2Comp(ExplicitComponent):
    def setup(self):
        self.add_input('x1', 1.0)
        self.add_input('x2', 1.0)
        self.add_output('y2',1.0)
        self.declare_partials('*', '*', method='fd')

    def compute(self, inputs, outputs):
        """
        Evaluates the equation
        y2 = 1/det*sin(x1)
        :param inputs:
        :param outputs:
        :return:
        """
        x1 = inputs['x1']
        x2 = inputs['x2']
        det = 1.0 / (2.0 + x1 * x2**2)
        outputs['y2'] = 1.0 / det * np.sin(x1)

class F1Comp(ExplicitComponent):
    def setup(self):
        self.add_input('y1', 1.0)
        self.add_output('f1', 0.0)
        self.declare_partials('*', '*', method='fd')

    def compute(self, inputs, outputs):
        """
        Evaluates the equation
        f1 = y1
        :param inputs:
        :param outputs:
        :return:
        """
        y1 = inputs['y1']
        outputs['f1'] = y1

class F2Comp(ExplicitComponent):
    def setup(self):
        self.add_input('x1', 1.0)
        self.add_input('y2', 1.0)
        self.add_output('f2', 0.0)
        self.declare_partials('*', '*', method='fd')

    def compute(self, inputs, outputs):
        """
        Evaluates the equation
        f2 = y2 * sin x1
        :param inputs:
        :param outputs:
        :return:
        """
        x1 = inputs['x1']
        y2 = inputs['y2']
        outputs['f2'] = y2 * np.sin(x1)

