#Example 1: Simple Markov Model
#
#
#The Model uses 2 disease states: Alive, Dead
#
#The Yearly Probability of transition between state Alive and State Dead is: 0.05
#
#Initial Conditions: 100 people start in state Alive, None are Dead
#
#Output requested: Amount of people in each state for years 1-10.

import tellurium as te

r = te.loada ('''
J0: A -> D; A*0.05
A = 100
D = 0
''')

# This will create the SBML XML file
te.saveToFile ('Example1.xml', r.getSBML())

r.setIntegrator('gillespie')
r.integrator.variable_step_size = True
r.getIntegrator().setValue('seed', 0)
result = r.simulate(0,10)
r.plot (result)
