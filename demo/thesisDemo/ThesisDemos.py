import sys
import os.path

sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
import numpy as np
from openmdao.api import Problem, Group, IndepVarComp, NewtonSolver,ScipyKrylov
from demo.thesisDemo.AllComps import *



class ThesisDemos(Group):
    def setup(self):
        indeps = self.add_subsystem('indeps', IndepVarComp())
        indeps.add_output('x', val=[1.0,1.0])

        #constraintDomain = self.add_subsystem('y', YComp())
        self.add_subsystem('y', YImplicitComp())

        # Nonlinear Block Gauss Seidel is a gradient free solver
        # cycle.nonlinear_solver = NonlinearBlockGS()

        self.add_subsystem('f', FComp())

        self.connect('indeps.x', ['f.x', 'y.x'])
        self.connect('y.y', ['f.y'])


prob = Problem()

model = prob.model = ThesisDemos()


model.nonlinear_solver = NewtonSolver()
model.nonlinear_solver.options['solve_subsystems'] = True
model.nonlinear_solver.options['max_sub_solves'] = 1
model.linear_solver = ScipyKrylov()

prob.setup()

prob['indeps.x'] = [1.0,1.0]
prob.run_model()
print(prob['y.y'])
print(prob.compute_totals(of=['f.f'],wrt=['indeps.x']))