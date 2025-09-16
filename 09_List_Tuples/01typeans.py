# Exercise 1: Identify Offline Nodes

# # Given a list of tuples representing (node_name, status), print the names of nodes that are offline.

# nodes = [
#     ("node-1", "online"),
#     ("node-2", "offline"),
#     ("node-3", "online"),
#     ("node-4", "offline")
# ]

# Expected Output:
# node-2
# node-4


nodes = [
    ("node-1", "online"),
    ("node-2", "offline"),
    ("node-3", "online"),
    ("node-4", "offline")
]
for node_name, status in nodes:
    if status == "offline":
        print(node_name)
