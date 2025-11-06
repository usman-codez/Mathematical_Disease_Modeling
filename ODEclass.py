import numpy as np

class ODE:
    '''
    Superclass to solve the diffrential equations

    '''
    def __init__(self,f):
        self.f = f

    def advanced(self):
        'solution with one timestep'
        raise NotImplementedError

    def initial_conditions(self, U0):
        if isinstance(U0, (int,float)):
            self.no_eqns = 1
            U0 = float(U0)
        else:
            U0 = np.asarray(U0)  #System of equations
            self.no_eqns = U0.size
        self.U0 = U0

    def solve(self, time_points):
        self.t = np.asarray(time_points)
        n = self.t.size
        self.u = np.zeros((n,self.no_eqns))

        self.u[0,:] = self.U0

        #Now we take integration on the equations
        for i in range(n-1):
            self.i = i
            self.u[i+1] = self.advanced()

        return self.u[:i+2], self.t[:i+2]

class ForwardEuler(ODE):
    def advanced(self):
        u, f, i, t = self.u, self.f, self.i, self.t
        dt = t[i+1] - t[i]
        return u[i,:]+dt * f(u[i,:], t[i])
