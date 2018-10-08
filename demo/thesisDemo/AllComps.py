from openmdao.api import ExplicitComponent, ImplicitComponent
import numpy as np


class YImplicitComp(ImplicitComponent):
    def setup(self):
        self.add_input('x', val=[1.0,1.0])
        self.add_output('y', val=[1.0,1.0])
        self.declare_partials('*', '*',method='fd')

    def apply_nonlinear(self, inputs, outputs, residuals):
        x1, x2 = inputs['x']
        y1, y2 = outputs['y']
        residuals['y'][0] = x1*y1 + 2*y2 - np.sin(x1)
        residuals['y'][1] = -y1 + x2**2*y2


class YComp(ExplicitComponent):
    def setup(self):
        self.add_input('x', val=[1.0,1.0])
        self.add_output('y', val=[1.0,1.0])
        self.declare_partials('*', '*', method='fd')

    def compute(self, inputs, outputs):
        """
        Evaluates the equation
        y1 = 1/det*x2**2*sin(x1)
        :param inputs:
        :param outputs:
        :return:
        """
        x1,x2 = inputs['x']
        det = (2.0 + x1 * x2**2)
        outputs['y'][0] = 1.0 / det * x2**2 * np.sin(x1)
        outputs['y'][1] = 1.0 / det * np.sin(x1)

class FComp(ExplicitComponent):
    def setup(self):
        self.add_input('x',val=[1.0,1.0])
        self.add_input('y', val=[1.0,1.0])
        self.add_output('f', val=[1.0,1.0])
        self.declare_partials('*', '*', method='fd')

    def compute(self, inputs, outputs):
        """
        Evaluates the equation
        f1 = y1
        :param inputs:
        :param outputs:
        :return:
        """
        y1, y2 = inputs['y']
        x1, x2 = inputs['x']
        outputs['f'][0] = y1
        outputs['f'][1] = y2*np.sin(x1)

class YImplicitUnifiedComp(ImplicitComponent):
    def setup(self):
        self.add_input('x', val=[1.0,1.0])
        self.add_output('y', val=[1.0,1.0])
        self.declare_partials('*', '*')

    def apply_nonlinear(self, inputs, outputs, residuals):
        x1, x2 = inputs['x']
        y1, y2 = outputs['y']
        residuals['y'][0] = x1*y1 + 2*y2 - np.sin(x1)
        residuals['y'][1] = -y1 + x2**2*y2

    def linearize(self, inputs, outputs, partials):
        x1,x2 = inputs['x']
        y1,y2 = outputs['y']

        partials['y', 'x'] = [[y1-np.cos(x1), 0],[0, 2*x2*y2]]
        partials['y', 'y'] = [[x1, 2], [-1, x2**2]]

class FUnifiedComp(ExplicitComponent):
    def setup(self):
        self.add_input('x',val=[1.0,1.0])
        self.add_input('y', val=[1.0,1.0])
        self.add_output('f', val=[1.0,1.0])
        self.declare_partials('*', '*')

    def compute(self, inputs, outputs):
        """
        Evaluates the equation
        f1 = y1
        :param inputs:
        :param outputs:
        :return:
        """
        y1, y2 = inputs['y']
        x1, x2 = inputs['x']
        outputs['f'][0] = y1
        outputs['f'][1] = y2*np.sin(x1)

    def compute_partials(self, inputs, partials):
        y1, y2 = inputs['y']
        x1, x2 = inputs['x']
        partials['f','x'] = [[0,0],[y2*np.cos(x1),0]]
        partials['f','y'] = [[0,0],[0, np.sin(x1)]]