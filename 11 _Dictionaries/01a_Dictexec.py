#Exercise 1: Print Services with High Error Rate 

# Given a dictionary of services and their error rates, print the names of services with error rate > 0.05.

# error_rates = {
#     "auth": 0.02,
#     "billing": 0.08,
#     "search": 0.01,
#     "email": 0.10
# }

# Expected Output:
# billing
# email

# error_rates = {
#     "auth": 0.02,
#     "billing": 0.08,
#     "search": 0.01,
#     "email": 0.10
# }
# for service, rate in error_rates.items():
#     if rate > 0.05:
#         print(service)





# Exercise 2: Count Services in Each State
# Given a dictionary of services and their states, count how many are in each state.

# service_states = {
#     "auth": "running",
#     "billing": "stopped",
#     "search": "running",
#     "email": "crashed",
#     "notifications": "running"
# }

# Expected Output:
# running: 3
# stopped: 1
# crashed: 1

service_states = {
    "auth": "running",
    "billing": "stopped",
    "search": "running",
    "email": "crashed",
    "notifications": "running"
}
state_counts = {}
for state in service_states.values():
    if state in state_counts:
        state_counts[state] += 1
    else:
        state_counts[state] = 1
for state, count in state_counts.items():
    print(f"{state}: {count}")


#Exercise 3: Restart Crashed Services
# Given a dictionary of services and their states, print a restart message for each crashed service.

# services = {
#     "auth": "running",
#     "billing": "crashed",
#     "search": "running",
#     "email": "crashed"
# }

# Expected Output:
# Restarting billing...
# Restarting email...

services = {
    "auth": "running",
    "billing": "crashed",
    "search": "running",
    "email": "crashed"
}
for service, state in services.items():
    if state == "crashed":
        print(f"Restarting {service}")
