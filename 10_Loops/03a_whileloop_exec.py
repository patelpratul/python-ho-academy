

# Exercise 3: Retry Until Service is Healthy
# Simulate retrying a health check until the service becomes healthy.

#health_checks = ["unhealthy", "unhealthy", "healthy", "healthy"]
#index = 0

# Expected Output:
# Checking... unhealthy
# Checking... unhealthy
# Checking... healthy


# health_checks = ["unhealthy", "unhealthy", "healthy", "healthy"]
# index = 0
# while index < len(health_checks):
#     print("Checking...", health_checks[index])
#     if health_checks[index] == "healthy":
#         break
#     index += 1

#Exercise 4: Auto-Scaling Until CPU Normalizes

# Simulate scaling down until CPU usage drops below 70%.

#cpu_usages = [95, 90, 85, 75, 65]
#index = 0

# Expected Output:
# CPU too high: 95%
# CPU too high: 90%
# CPU too high: 85%
# CPU too high: 75%
# CPU normalized: 65%

cpu_usages = [95, 90, 85, 75, 65]
index = 0
while index < len(cpu_usages):
    usage = cpu_usages[index]
    if usage < 70:
        print(f"CPU normalized: {usage}%")
        break
    else:
        print(f"CPU too high: {usage}%")
    index += 1

