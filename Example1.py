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
import matplotlib.pyplot as plt

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

axis1 = plt.subplot(111)
axis1.plot (result[:,0], result[:,1], linestyle='-', linewidth=2, color='r')
axis1.plot (result[:,0], result[:,2], linestyle='--', linewidth=2, color='b')
plt.title("Example 1", fontsize="xx-large")
plt.xlabel("Time", fontsize="xx-large")
plt.ylabel("Individuals", fontsize="xx-large")
box = axis1.get_position()
axis1.set_position([box.x0, box.y0 +  box.height*0.2, box.width , box.height*0.8])
# Put a legend to the right of the current axis
axis1.legend(['[A]', '[D]'], loc='upper center', bbox_to_anchor=(0.5, -0.225), ncol=2, fontsize=9)
plt.show()
