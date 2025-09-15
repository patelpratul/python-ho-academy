Exercise 1: Identify Offline Nodes

# Given a list of tuples representing (node_name, status), print the names of nodes that are offline.

nodes = [
    ("node-1", "online"),
    ("node-2", "offline"),
    ("node-3", "online"),
    ("node-4", "offline")
]

# Expected Output:
# node-2
# node-4
Exercise 2: Count Services with High Latency
    
    # Each tuple contains (service_name, latency_ms). Count how many services have latency > 300ms.

services = [
    ("auth", 120),
    ("billing", 450),
    ("search", 310),
    ("email", 290)
]

# Expected Output:
# 2


Exercise 3: Print Services Needing Restart
# Each tuple contains (service_name, is_crashed). Print names of services where is_crashed is True.

services = [
    ("api-gateway", False),
    ("user-db", True),
    ("cache", False),
    ("notifications", True)
]

# Expected Output:
# user-db
# notifications

