import numpy as np
from ODEclass import ForwardEuler
from matplotlib import pyplot as plt

'''
SEIR Disease Model
S' = -beta*S*I
E' = beta*S*I - sigma*E
I' = sigma*E - gamma*I
R' = gamma*I
'''
class SEIR:
    def __init__(self, beta, sigma, gamma, S0, E0, I0, R0):
        if isinstance(beta, (int, float)):
            self.beta = lambda t: beta
        elif callable(beta):
            self.beta = beta

        if isinstance(sigma, (int, float)):
            self.sigma = lambda t: sigma
        elif callable(sigma):
            self.sigma = sigma

        # Recovery rate (gamma)
        if isinstance(gamma, (int, float)):
            self.gamma = lambda t: gamma
        elif callable(gamma):
            self.gamma = gamma

        # Initial conditions
        self.initial_conditions = [S0, E0, I0, R0]

    def __call__(self, u, t):
        '''Right-hand side of the SEIR system'''
        S, E, I, R = u
        return np.asarray([
            -self.beta(t)*S*I,
            self.beta(t)*S*I - self.sigma(t)*E,
            self.sigma(t)*E - self.gamma(t)*I,
            self.gamma(t)*I
        ])

if __name__ == '__main__':
    beta = 0.04          # infection rate
    sigma = 1/5.2       # incubation rate (1/incubation period)
    gamma = 1/10         # recovery rate (1/infectious period)

    # Initial conditions
    N = 1000
    S0 = N-1
    E0 = 0
    I0 = 1
    R0 = 0

    model = SEIR(beta, sigma, gamma, S0, E0, I0, R0)
    solver = ForwardEuler(model)
    solver.initial_conditions(model.initial_conditions)

    timesteps = np.linspace(0, 180, 1801)
    u, t = solver.solve(timesteps)

    # Plot results
    plt.plot(t, u[:,0], label='Susceptible')
    plt.plot(t, u[:,1], label='Exposed')
    plt.plot(t, u[:,2], label='Infectious')
    plt.plot(t, u[:,3], label='Recovered')
    plt.title('SEIR Epidemic Model Simulation')
    plt.xlabel('Time (days)')
    plt.ylabel('Population')
    plt.legend()
    plt.grid(True)
    plt.show()
