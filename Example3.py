#Example 3: Stratified Markov Model
#
#
#There are 3 disease states:
#
#Healthy, Sick, Dead
#There are Two cohorts, Male, Female
#
#The yearly transition probabilities are :
#Healthy to Dead 0.01
#Healthy to Sick 0.2 for Male, 0.1 for Female
#Sick to Healthy 0.1
#Sick to Dead 0.3
#The transition Matrix now depends on the cohort, Male or Female and can be expressed as a function of a boolean covariate Male.
#[[ 1-0.1-0.1*Male-0.01 ,  0.1+0.1*Male ,  0.01],
#[0.1,      1-0.1-0.3,     0.3],
#[ 0  ,      0 ,     1]]
#
#
#Initial conditions:
#
#Healthy = (50 Male, 50 Female), Sick = (0,0), Dead = (0,0)
#
#Output: How many Male, Female, Total are in each disease state for the first 10 years?
#
#
#Output requested: Amount of people in each state for years 1-10.
#
#This implementation uses a flattened model separated to M=Male and F=Female

import tellurium as te
import matplotlib.pyplot as plt

r = te.loada ('''
MJ00: MH -> MS; MH*0.2
MJ02: MH -> MD; MH*0.01
MJ10: MS -> MH; MS*0.1
MJ12: MS -> MD; MS*0.3
FJ00: FH -> FS; FH*0.1
FJ02: FH -> FD; FH*0.01
FJ10: FS -> FH; FS*0.1
FJ12: FS -> FD; FS*0.3
MH = 50
MS = 0
MD = 0
FH = 50
FS = 0
FD = 0
''')

# This will create the SBML XML file
te.saveToFile ('Example3.xml', r.getSBML())

r.setIntegrator('gillespie')
r.integrator.variable_step_size = True
r.getIntegrator().setValue('seed', 0)
result = r.simulate(0,10)
#r.plot (result)

plt.plot (result[:,0], result[:,1], linestyle='-', linewidth=2)
plt.plot (result[:,0], result[:,2], linestyle='--', linewidth=2)
plt.plot (result[:,0], result[:,3], linestyle=':', linewidth=2)
plt.plot (result[:,0], result[:,4], linestyle='-.', linewidth=2)
plt.plot (result[:,0], result[:,5], linestyle='-', linewidth=2)
plt.plot (result[:,0], result[:,6], linestyle='--', linewidth=2)
plt.xlabel("Time", fontsize="xx-large")
plt.ylabel("Individuals", fontsize="xx-large")
plt.legend(['[MH]', '[MS]', '[MD]', '[FH]', '[FS]', '[FD]'])
plt.show()
