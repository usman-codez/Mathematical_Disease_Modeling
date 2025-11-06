'''
I made a mathematical model of a fictional zombie epidemic using a system of four differential
equations. I learned how infection, killing, and recovery rates affect population. The model is
inspired by epidemic modeling and I used the Forward Euler numerical method in Python.

Zombie Apocalypse
S' = sigma - beta*S*Z - delta_S*S
I' = beta*S*Z - rho*I - delta_I*I
Z' = rho*I - alpha*S*Z
R' = delta_S*S + delta_I*I + alpha*S*Z
'''

import numpy as np
from ODEclass import ForwardEuler
from matplotlib import pyplot as plt
class SIZR:
    def __init__(self, sigma, beta, rho, delta_S, delta_I, alpha, S0, I0, Z0, R0):

         if isinstance(sigma, (int, float)):
             self.sigma = lambda t : sigma
         elif callable(sigma):
             self.sigma = sigma

         if isinstance(beta, (int, float)):
             self.beta = lambda t : beta
         elif callable(beta):
             self.beta = beta

         if isinstance(rho, (int, float)):
             self.rho = lambda t : rho
         elif callable(rho):
             self.rho = rho

         if isinstance(delta_S, (int, float)):
             self.delta_S = lambda t : delta_S
         elif callable(delta_S):
             self.delta_S = delta_S

         if isinstance(delta_I, (int, float)):
             self.delta_I = lambda t : delta_I
         elif callable(delta_I):
             self.delta_I = delta_I

         if isinstance(alpha, (int, float)):
             self.alpha = lambda t : alpha
         elif callable(alpha):
             self.alpha = alpha

         self.initial_conditions = [S0, I0, Z0, R0]

    def __call__(self, u, t):
        'RHS of the system'
        S,I,Z,R = u
        return np.asarray([
            self.sigma(t) - self.beta(t)*S*Z - self.delta_S(t)*S,
            self.beta(t)*S*Z - self.rho(t)*I - self.delta_I(t)*I,
            self.rho(t)*I - self.alpha(t)*S*Z,
            self.delta_S(t)*S + self.delta_I(t)*I + self.alpha(t)*S*Z
        ])

if __name__ == '__main__':

    beta0 = 0.012  # starting infection rate
    decay = 0.05  # how fast humans adapt
    beta = lambda t: beta0 * np.exp(-decay * t)  #probability a zombie infect human
    alpha  = 0.0016  #how likely a human is to kill zombie
    sigma = 2  #population growth
    rho = 1  #how many people go to zombie
    delta_I = 0.014  #infected are killed
    delta_S = 0.0  #Zombie kills a human

    S0 = 60
    I0 = 0
    Z0 = 1
    R0 = 0

    model = SIZR(
        sigma, beta, rho, delta_S, delta_I, alpha, S0, I0, Z0, R0
    )
    solver = ForwardEuler(model)
    solver.initial_conditions(model.initial_conditions)

    timesteps = np.linspace(0, 24, 1001)
    u,t = solver.solve(timesteps)

    plt.plot(t, u[:,0], label = 'Susceptible Humans')
    plt.plot(t, u[:,1], label = 'Infectd Humans')
    plt.plot(t, u[:,2], label = 'Zombies')
    plt.plot(t, u[:,3], label = 'Killed')
    plt.title('SIZR model Zombie Apocalypse')
    plt.xlabel('Time')
    plt.ylabel('Population')
    plt.legend()
    plt.grid(True)
    plt.show()