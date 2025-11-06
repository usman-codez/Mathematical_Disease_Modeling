# Mathematical_Disease_Modeling

This is a mathematical modeling project of diseases spread in a population. I built three different models, **SIR**, **SEIR**, and **SIZR (Zombie Model)**, and learned how changing parameters like infection rate, recovery rate, and incubation period affect the spread of a disease.
I used Python to write my ODE solver using the Forward Euler method and applied it to all models.  
This helped me connect mathematics with programming and understand how models will be used in to solve real-world problems.

## Mathematical Background

Each model is based on **ordinary differential equations (ODEs)** that describe how people move between stages.

### SIR Model
The SIR model divides the population into three groups:  
- **S(t)**: Susceptible (can get infected)  
- **I(t)**: Infected (can spread the disease)  
- **R(t)**: Recovered (immune or removed)
The equations are:

**dS/dt = -β * S * I <br>
dI/dt = β * S * I - μ * I <br>
dR/dt = μ * I** <br>
Where:  
- **β** = infection rate  
- **μ** = recovery rate
### SEIR Model
This model adds an **Exposed (E)** group, which represents people who are infected but not yet infectious.  

**dS/dt = -β * S * I <br>
dE/dt = β * S * I - σ * E <br>
dI/dt = σ * E - γ * I <br>
dR/dt = γ * I** <br>
Where:  
- **β** = infection rate  
- **σ** = incubation rate (1 / incubation period)  
- **γ** = recovery rate (1 / infectious period)
### SIZR (Zombie Model)

This is a fun, fictional version where, instead of a normal disease, we model a zombie outbreak.  
It includes four groups:  
- **S(t)**: Susceptible humans  
- **I(t)**: Infected humans  
- **Z(t)**: Zombies  
- **R(t)**: Removed (dead or neutralized)

**dS/dt = σ - β * S * Z - δ_S * S <br>
dI/dt = β * S * Z - ρ * I - δ_I * I <br>
dZ/dt = ρ * I - α * S * Z <br>
dR/dt = δ_S * S + δ_I * I + α * S * Z** <br>
Where:  
- **σ** = birth rate  
- **β** = infection rate (zombie bite chance)  
- **ρ** = rate infected become zombies  
- **α** = rate humans kill zombies  
- **δ_S**, **δ_I** = natural death rates
## How the Code Works
All these equations are solved numerically using the **Forward Euler method**, implemented in `ODEclass.py`.  
The solver calculates the next step of the solution based on the previous step using:
\[
u_{n+1} = u_n + \Delta t \cdot f(u_n, t_n)
\]

This method is simple but effective for learning and understanding how systems evolve over time.
