from pyomo.environ import *
import pandas as pd
import os

# Load data
data = pd.read_csv('data/customers.csv')
n = len(data)

model = ConcreteModel()

# Sets
model.Nodes = RangeSet(0, n-1)  # 0 = depot, 1...n-1 = customers
model.Customers = RangeSet(1, n-1)  # Customers (excluding depot)

# Parameters: Euclidean distance between nodes
distance = {(i, j): ((data.iloc[i]['x'] - data.iloc[j]['x'])**2 + (data.iloc[i]['y'] - data.iloc[j]['y'])**2 )**0.5
            for i in range(n) for j in range(n)}

# Decision Variables
model.x = Var(model.Nodes, model.Nodes, domain=Binary)
model.u = Var(model.Customers, within=NonNegativeIntegers)  # Auxiliary variable for MTZ

# Objective: Minimize total distance
model.obj = Objective(expr=sum(distance[i, j] * model.x[i, j] for i in model.Nodes for j in model.Nodes if i != j),
                      sense=minimize)

# Constraints: Each customer has exactly one incoming and one outgoing edge
def in_flow_rule(model, i):
    if i == 0:
        return Constraint.Skip
    return sum(model.x[j, i] for j in model.Nodes if j != i) == 1
model.in_flow = Constraint(model.Nodes, rule=in_flow_rule)

def out_flow_rule(model, i):
    if i == 0:
        return Constraint.Skip
    return sum(model.x[i, j] for j in model.Nodes if j != i) == 1
model.out_flow = Constraint(model.Nodes, rule=out_flow_rule)

# Depot constraints: start and end at depot
def depot_out(model):
    return sum(model.x[0, j] for j in model.Nodes if j != 0) == 1
model.depot_out = Constraint(rule=depot_out)

def depot_in(model):
    return sum(model.x[i, 0] for i in model.Nodes if i != 0) == 1
model.depot_in = Constraint(rule=depot_in)

# MTZ Subtour Elimination Constraints
def mtz_constraint_rule(model, i, j):
    if i == j:
        return Constraint.Skip
    return model.u[i] - model.u[j] + n * model.x[i, j] <= n - 1
model.mtz_constraints = Constraint(model.Customers, model.Customers, rule=mtz_constraint_rule)

# Optional: Lower bound for u[i] >= 1
def lower_bound_u(model, i):
    return model.u[i] >= 1
model.lower_bound_constraints = Constraint(model.Customers, rule=lower_bound_u)

# Solve
solver = SolverFactory('cbc')  # Or 'gurobi' if available
result = solver.solve(model)

# Save results
os.makedirs('results', exist_ok=True)
with open('results/solution.txt', 'w') as f:
    for i in model.Nodes:
        for j in model.Nodes:
            if i != j and model.x[i, j].value > 0.5:
                f.write(f'{i} -> {j}\n')

print("Solution saved to results/solution.txt")