#Exercise 1: Identify Unique Error Codes
# Given a list of error codes from logs, print the unique error codes.

error_codes = ["500", "404", "500", "403", "404", "502"]

# Expected Output:
# {'500', '404', '403', '502'}

#Exercise 2: Find Services Missing in Production

# Compare services deployed in staging vs production and print the ones missing in production.

staging_services = {"auth", "billing", "search", "email"}
production_services = {"auth", "billing", "search"}

# Expected Output:
# {'email'}


#Exercise 3: Detect Common Misconfigured Services
# Given two sets of misconfigured services from two regions, find the common ones.

region_a_issues = {"auth", "email", "cache"}
region_b_issues = {"email", "search", "cache"}

# Expected Output:
# {'email', 'cache'}

