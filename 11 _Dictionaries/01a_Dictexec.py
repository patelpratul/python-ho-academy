#Exercise 1: Print Services with High Error Rate 

# Given a dictionary of services and their error rates, print the names of services with error rate > 0.05.

error_rates = {
    "auth": 0.02,
    "billing": 0.08,
    "search": 0.01,
    "email": 0.10
}

# Expected Output:
# billing
# email


# Exercise 2: Count Services in Each State
# Given a dictionary of services and their states, count how many are in each state.

service_states = {
    "auth": "running",
    "billing": "stopped",
    "search": "running",
    "email": "crashed",
    "notifications": "running"
}

# Expected Output:
# running: 3
# stopped: 1
# crashed: 1


#Exercise 3: Restart Crashed Services
# Given a dictionary of services and their states, print a restart message for each crashed service.

services = {
    "auth": "running",
    "billing": "crashed",
    "search": "running",
    "email": "crashed"
}

# Expected Output:
# Restarting billing...
# Restarting email...

