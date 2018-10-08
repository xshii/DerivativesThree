from openmdao.api import ImplicitComponent
class demoComp(ImplicitComponent):
    """
    x + y + xy = 2
    """
    def setup(self):
        self.add_input('x',val=1.0)
        self.add_output('y',val=0.)
        self.declare_partials('*','*',method='fd')

    def apply_nonlinear(self, inputs, outputs, residuals):
        x = inputs['x']
        y = outputs['y']
        residuals['y']=2*x+y-2

from openmdao.api import Problem, Group, IndepVarComp,NewtonSolver, ScipyKrylov
problem =  Problem()
model = problem.model = Group()
model.add_subsystem('x', IndepVarComp('x', 1.0))
model.add_subsystem('demoComp', demoComp())
model.connect('x.x', 'demoComp.x')

model.nonlinear_solver = NewtonSolver()
model.nonlinear_solver.options['solve_subsystems'] = True
model.nonlinear_solver.options['max_sub_solves'] = 1
model.linear_solver = ScipyKrylov()

problem.setup(check=True)
totals = problem.compute_totals(['demoComp.y'], ['x.x'])

print(totals)