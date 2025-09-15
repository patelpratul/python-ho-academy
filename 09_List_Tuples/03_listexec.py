
# Given a list of service health statuses, print only the unhealthy ones.

services = ["healthy", "unhealthy", "healthy", "degraded", "unhealthy"]

# Expected Output:
# unhealthy
# degraded
# unhealthy


Exercise 2: Count High CPU Usage Nodes
# Given a list of CPU usages for nodes in a cluster, count how many are above 80%.

cpu_usages = [45, 82, 77, 91, 60, 88]

# Expected Output:
# 3


Exercise 3: Identify Services Needing Restart

# Given a list of service states, print the names of services that are "crashed".

services = [
    {"name": "auth-service", "state": "running"},
    {"name": "payment-service", "state": "crashed"},
    {"name": "user-service", "state": "running"},
    {"name": "email-service", "state": "crashed"}
]

# Expected Output:
# payment-service
# email-service

