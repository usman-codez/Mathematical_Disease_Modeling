'''
SIR disease model which has the following mathematical equations
S = -beta*S*I
I = beta*S*I - mu*I
R = mu*I
'''
import numpy as np
from ODEclass import ForwardEuler
from matplotlib import pyplot as plt

class SIR:
    def __init__(self, beta, mu, S0, I0, R0):
        'beta and mu are the parameters while S0, I0, R0 are initial values in ODE'

        if isinstance(mu, (float, int)):
            self.mu = lambda t:mu
        elif callable(mu):
            self.mu = mu

        if isinstance(beta, (float, int)):
            self.beta = lambda t:beta
        elif callable(beta):
            self.beta = beta

        self.i_c = [S0, I0, R0]

    def __call__(self, u, t):
        S,I,R = u
        return np.asarray([
            -self.beta(t)*S*I,
            self.beta(t)*S*I - self.mu(t)*I,
            self.mu(t)*I
        ])

if __name__ == "__main__":
    sir = SIR(0.002, 0.5,1000,1,0)
    solver = ForwardEuler(sir)
    solver.initial_conditions(sir.i_c)
    timestpes = np.linspace(0,60,6001)
    u, t = solver.solve(timestpes)

    plt.plot(t, u[:,0], label='Susceptible')
    plt.plot(t, u[:,1], label='Infected')
    plt.plot(t, u[:,2], label='Recovered')
    plt.legend()
    plt.show()