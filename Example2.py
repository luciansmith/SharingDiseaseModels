#Example 2: Three State Markov Model
#
#
#There are 3 disease states:
#Healthy, Sick, Dead
#
#The yearly transition probabilities are :
#Healthy to Dead 0.01
#Healthy to Sick 0.2
#Sick to Healthy 0.1
#Sick to Dead 0.3
#
#This builds the following transition Matrix
#[[ 1-0.2-0.01 ,  0.2 ,  0.01],
# [0.1,      1-0.1-0.3,     0.3],
#[ 0  ,      0 ,     1]]
#
#Initial conditions:
#Healthy = 100, Sick = 0, Dead = 0
#
#
#
#Output requested: Amount of people in each state for years 1-10.

import tellurium as te
import matplotlib.pyplot as plt

r = te.loada ('''
J00: H -> S; H*0.2
J02: H -> D; H*0.01
J10: S -> H; S*0.1
J12: S -> D; S*0.3
H = 100
S = 0
D = 0''')

# This will create the SBML XML file
te.saveToFile ('Example2.xml', r.getSBML())

r.setIntegrator('gillespie')
r.integrator.variable_step_size = True
r.getIntegrator().setValue('seed', 0)
result = r.simulate(0,10)
#r.plot (result)

plt.plot (result[:,0], result[:,1], linestyle='-', linewidth=2)
plt.plot (result[:,0], result[:,2], linestyle='--', linewidth=2)
plt.plot (result[:,0], result[:,3], linestyle=':', linewidth=2)
plt.xlabel("Time", fontsize="xx-large")
plt.ylabel("Individuals", fontsize="xx-large")
plt.legend(['[H]', '[S]', '[D]'])
plt.show()
