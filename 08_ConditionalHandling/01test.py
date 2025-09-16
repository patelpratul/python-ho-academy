# Given a list of service health statuses, print only the unhealthy ones.
#services = ["healthy", "unhealthy", "healthy", "degraded", "unhealthy"]
# Expected Output:
# unhealthy
# degraded
# unhealthy





# services = ["healthy", "unhealthy", "healthy", "degraded", "unhealthy"]
# for status in services:
#     if status != "healthy":
#         print(status)


# Given a list of CPU usages for nodes in a cluster, count how many are above 80%.
#cpu_usages = [45, 82, 77, 91, 60, 88]
# Expected Output:
# 3


# cpu_usages = [45, 82, 77, 91, 60, 88]
# high_usage_count = 0
# for usage in cpu_usages:
#     if usage > 80:
#         high_usage_count += 1
# print(high_usage_count)



# Given a list of service states, print the names of services that are "crashed".
#services = [
#    {"name": "auth-service", "state": "running"},
#    {"name": "payment-service", "state": "crashed"},
#    {"name": "user-service", "state": "running"},
#    {"name": "email-service", "state": "crashed"}
#]
# Expected Output:
# payment-service
# email-service


services = [
     {"name": "auth-service", "state": "running"},
     {"name": "payment-service", "state": "crashed"},
     {"name": "user-service", "state": "running"},
     {"name": "email-service", "state": "crashed"}
 ]
for service in services:
     if service["state"] == "crashed":
         print(service["name"])
