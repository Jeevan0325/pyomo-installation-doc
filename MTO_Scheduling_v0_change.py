from pyomo.environ import *

# Sample data
N = 4  # Number of orders
M = 2  # Number of resources
T = 10  # Number of time periods

# Order data
processing_times = [3, 2, 4, 2]
due_dates = [8, 6, 12, 7]
priority_weights = [
    [1.5, 1.2],
    [1.2, 1.5],
    [1.0, 1.0],
    [1.3, 1.1]
]

# Resource data
resource_availabilities = [
    [1] * T,  # Availability for Resource 1
    [1] * T   # Availability for Resource 2
]
processing_times_resource = [
    [1, 0.8, 1.5, 0.7, 1, 0.8, 1.5, 0.7, 1, 0.8],  # Processing times for Resource 1
    [0.5, 1, 2, 0.7, 0.5, 1, 2, 0.7, 0.5, 1]       # Processing times for Resource 2
]

# Print the dimensions of data structures for debugging
print("Number of Orders (N):", N)
print("Number of Resources (M):", M)
print("Number of Time Periods (T):", T)
print("Resource Availabilities Dimensions:", len(resource_availabilities), len(resource_availabilities[0]))

# Create Pyomo model
model = ConcreteModel()

# Decision variables
model.x = Var(range(N), range(M), range(T), within=Binary)

# Objective function: Minimize total production cost
model.objective = Objective(
    expr=sum(processing_times_resource[i][j] * model.x[i, j, t] for i in range(N) for j in range(M) for t in range(T)),
    sense=minimize
)

# Constraints
model.order_process_once = ConstraintList()
for i in range(N):
    model.order_process_once.add(sum(model.x[i, j, t] for j in range(M) for t in range(T)) == 1)

model.resource_availability = ConstraintList()
for j in range(M):
    for t in range(T):
        model.resource_availability.add(
            sum(processing_times_resource[i][j] * model.x[i, j, t] for i in range(N)) <= resource_availabilities[j][t]
        )

model.time_slot_allocation = ConstraintList()
for t in range(T):
    model.time_slot_allocation.add(sum(model.x[i, j, t] for i in range(N) for j in range(M)) <= 1)

# Solve the model
solver = SolverFactory('glpk')
solver.solve(model)

# Print the results
for i in range(N):
    for j in range(M):
        for t in range(T):
            if model.x[i, j, t].value == 1:
                print(f"Order {i+1} is processed on Resource {j+1} at Time {t+1}")

print("Total Production Cost:", model.objective())
