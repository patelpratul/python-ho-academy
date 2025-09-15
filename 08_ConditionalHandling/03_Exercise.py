# Exercise 1 Service Health Check

# on the base of below service status and response time, determine if the service is healthy.

service_status = "running"  # could be "stopped", "degraded", or "running"
response_time_ms = 180      # in milliseconds
# Write an if statement to print:
# - "Service is healthy" if status is "running" and response time is under 200ms
# - "Service is slow" if status is "running" but response time is 200ms or more
# - "Service is not healthy" for any other status


# Exercise 2  Canary Deployment Decision

# Decide whether to proceed with a canary deployment based on error rate and traffic.

error_rate = 0.01  # 1% error rate
traffic_percentage = 10  # percentage of total traffic
# Write an if statement to:
# - Print "Proceed with canary" if error_rate < 0.02 and traffic_percentage <= 10
# - Print "Hold canary" if error_rate >= 0.02
# - Print "Increase traffic gradually" if error_rate < 0.02 and traffic_percentage > 10

# Exercise 3  Infrastructure Scaling
# Determine whether to scale up or down based on CPU usage.

cpu_usage = 85  # in percent
# Write an if statement to:
# - Print "Scale up" if CPU usage is above 80%
# - Print "Scale down" if CPU usage is below 30%
# - Print "Maintain current capacity" otherwise


