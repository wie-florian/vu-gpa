from pulp import LpProblem, LpVariable, LpMaximize, LpStatus


#Initalize the LP
prob=LpProblem("Problem_1", LpMaximize)

#Decision Variables
x=LpVariable.dicts("x", [1,2], lowBound=0, cat="Continuous")

#Objective Function
prob +=10*x[1]+20*x[2]

#Constraints
prob +=-x[1]+2*x[2]<=15
prob +=x[1]+x[2]<=12
prob +=5*x[1]+3*x[2]<=45

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

