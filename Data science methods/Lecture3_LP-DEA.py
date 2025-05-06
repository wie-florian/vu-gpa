# import pandas as pd
# import numpy as np

# data=pd.read_excel(r'''\Users\spapadokonstantakis\OneDrive - TU Wien\Work\Lehre\Data Science_Gren Chem_Eng\DEA-example.xlsx''', sheet_name=4, header=None)
# print(data)
# par=data.iloc[0:7, 0:5]
# print(par)
# parA=np.matrix(par)
# print(parA)



#Initalize the LP
prob=LpProblem("DEA_SOLVENTS", LpMinimize)

#Decision Variables
lamda=LpVariable.dicts("lamda", [1,2,3,4,5,6,7], lowBound=0, cat="Continuous")
slack=LpVariable.dicts("slack", [1,2,3,4,5], lowBound=0, cat="Continuous")
z=LpVariable.dicts("eff", [1], lowBound=None, cat="Continuous")

#Objective Function
prob +=z[1]

#Constraints
prob +=lamda[1]*0.57+lamda[2]*1.32+lamda[3]*0.77+lamda[4]*1.18+lamda[5]*0.94+lamda[6]*1.08+lamda[7]*1.8+slack[1]==z[1]*0.94
prob +=lamda[1]*9.98+lamda[2]*6.37+lamda[3]*4.51+lamda[4]*5.97+lamda[5]*9.33+lamda[6]*8.34+lamda[7]*7.55+slack[2]==z[1]*9.33
prob +=lamda[1]*21.69+lamda[2]*34.28+lamda[3]*27.51+lamda[4]*23.26+lamda[5]*34.35+lamda[6]*28.85+lamda[7]*33.66+slack[3]==z[1]*34.35
prob +=lamda[1]*0.37+lamda[2]*0.20+lamda[3]*0.12+lamda[4]*0.17+lamda[5]*0.22+lamda[6]*0.28+lamda[7]*0.28+slack[4]==z[1]*0.22
prob +=lamda[1]*36.4+lamda[2]*17.4+lamda[3]*8.9+lamda[4]*23.7+lamda[5]*6.3+lamda[6]*27.1+lamda[7]*32.5-slack[5]==6.3
#prob +=lamda[1]+lamda[2]+lamda[3]+lamda[4]+lamda[5]+lamda[6]+lamda[7]==1

print(prob)

#Solve Problem
status=prob.solve()
print(LpStatus[status])

#Display Objective Value
print()

#Display Variables
for var in prob.variables():
    print(f"{var.name}={var.varValue}")

print(f"OBJECTIVE VALUE: {prob.objective.value()}")
