#Exercise 3: Print Services Needing Restart
# Each tuple contains (service_name, is_crashed). Print names of services where is_crashed is True.

# services = [
#     ("api-gateway", False),
#     ("user-db", True),
#     ("cache", False),
#     ("notifications", True)
# ]

# Expected Output:
# user-db
# notifications

services = [
    ("api-gateway", False),
    ("user-db", True),
    ("cache", False),
    ("notifications", True)
]
for service_name, is_crashed in services:
    if is_crashed:
        print(service_name)
