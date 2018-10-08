import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
import numpy as np
from openmdao.api import Problem, Group, IndepVarComp, ExecComp, NonlinearBlockGS, ScipyOptimizeDriver
from demo.thesisDemo.AllComp import F1Comp, F2Comp, Y1Comp, Y2Comp



class ThesisDemo(Group):
    def setup(self):
        indeps = self.add_subsystem('indeps', IndepVarComp())
        indeps.add_output('x1', 1.0)
        indeps.add_output('x2', 1.0)

        constraintDomain = self.add_subsystem('y1y2', Group())
        d1 = constraintDomain.add_subsystem('y1', Y1Comp())
        d2 = constraintDomain.add_subsystem('y2', Y2Comp())
        #constraintDomain.connect('y1.x1', 'y2.x1')
        #constraintDomain.connect('y1.x2', 'y2.x2')

        ######################################
        # This is a "forgotten" connection!!
        ######################################
        # cycle.connect('d2.y2', 'd1.y2')

        # Nonlinear Block Gauss Seidel is a gradient free solver
        # cycle.nonlinear_solver = NonlinearBlockGS()

        self.add_subsystem('f1', F1Comp())
        self.add_subsystem('f2', F2Comp())

        self.connect('indeps.x1', ['f2.x1', 'y1y2.y1.x1', 'y1y2.y2.x1'])
        self.connect('indeps.x2', ['y1y2.y1.x2', 'y1y2.y2.x2'])
        self.connect('y1y2.y1.y1', ['f1.y1'])
        self.connect('y1y2.y2.y2', ['f2.y2'])


prob = Problem()

prob.model = ThesisDemo()


prob.setup()

prob['indeps.x1'] = 1.0
prob['indeps.x2'] = 1.0
prob.run_model()
print(prob.compute_totals(of=['f1.f1'],wrt=['indeps.x1']))