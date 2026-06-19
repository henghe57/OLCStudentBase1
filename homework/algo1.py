###############################################################
# Scenario: Employee Performance Review

# Finding Maximum, Minimum, and Average Performance Scores 
# Without Built-in Functions
# YOU CANNOT USE ANY PYTHON INBUILT FUNCTIONS TO DO THIS.

# A company conducts annual performance reviews for employees. 
# Each employee is given a performance score out of 100. 
# The HR department wants to:

# - Identify the top-performing employee (highest score).
# - Identify the lowest-performing employee (lowest score).
# - Calculate the average performance score, rounded to 2 decimal places.
# - Identify underperforming employees (those with scores below 50) 
#    -> save them into another dictionary called non_performers.
#   and print a performance warning message to all of these employees.

performance_scores = {
    'Alice': 88, 'Benny': 75, 'Charlie': 92, 'David': 85,
    'Emma': 78, 'Farah': 81, 'George': 66, 'Hassan': 94,
    'Ivy': 71, 'Jack': 88, 'Liam': 45, 'Jessica': 98,
    'Samir': 23, 'Jimmy': 5, 'Bryan': 78, 'Estelle': 9}

# write your code here

first = True
total = 0
counter = 0
highest_score = 0
lowest_score = 0
top_employee = ""
low_employee = ""
non_performers = {}

for employee in performance_scores:
    score = performance_scores[employee]
    # print(score)
    
    if score > highest_score:
        highest_score = score
        top_employee = employee
    if score < lowest_score:
        lowest_score = score
        low_employee = employee
    if score < 50:
        non_performers[employee] = score
        print(f"{employee}, performance warning!")
    
    total += score
    counter += 1

average = round(total / counter,2)

print(f"The top_performing employee: {top_employee}")
print(f"The low_performing employee: {low_employee}")
print(f"Average score: {average}")
print(f"Non-performers: {non_performers}")
