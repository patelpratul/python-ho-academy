#Exercise 2: Count Services with High Latency
    
    # Each tuple contains (service_name, latency_ms). Count how many services have latency > 300ms.

# services = [
#     ("auth", 120),
#     ("billing", 450),
#     ("search", 310),
#     ("email", 290)
# ]

# Expected Output:
# 2


services = [
    ("auth", 120),
    ("billing", 450),
    ("search", 310),
    ("email", 290)
]
high_latency_count = 0
for service_name, latency in services:
    if latency > 300:
        high_latency_count += 1
print(high_latency_count)