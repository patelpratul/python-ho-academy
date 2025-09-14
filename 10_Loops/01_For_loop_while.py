# For Loop Example
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("for loop : ", fruit)

# while loop example
count = 0
while count < 5:
    print("while loop  : ", count)
    count += 1

# break statement example
for i in range(10):
    if i == 5:
        break
    print("break statement : ", i)


# continue statement example
for i in range(10):
    if i == 5:
        continue
    print("continue statement : ", i)


# platform enginerring real time example
log_file = [
   "INFO: Operation successful",
   "ERROR: File not found",
   "DEBUG: Connection established",
   "ERROR: Database connection failed",
]

for line in log_file:
   if "ERROR" in line:
       print(line)
