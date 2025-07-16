# Challenge: Advanced Grade Analysis

# Scenario: A teacher needs detailed analysis of class performance.
# students = {"Alice": 85, "Bob": 78, "Charlie": 92, "Diana": 88, "Eve": 76}

# Task 1: Find and print the names of students who scored below the average grade.



# average = sum(students.values()) / len(students)
# print(average)

# for student, score in students.items():
#     # print(student)
#     # check score of every student vs the average score
#   if score < average:
#       print(f"{student} scored less than {average}")


#------------------------------------------------------------
# Task 2: Create a new dictionary with students categorized as "Pass" or "Fail".
# Assume a passing grade is 80 or above.
# print a message warning students who fail e.g. Bob failed! You need to work harder.

# category = {} # empty dictionary

# for name, score in students.items():
#     if score >= 80:
#         category[name] = "pass"
#     else:
#         category[name] = "fail"
# print(category)

#------------------------------------------------------------

# Scenario: A warehouse manager needs to identify items for reordering.
inventory = {"Apples": 50, "Bananas": 10, "Oranges": 20, "Grapes": 5, "Pineapples": 40}

# Task 1: Identify and print items with stock below 15 for reordering.

for item, amount in inventory.items():
    if amount <= 15:
        print(item)

#------------------------------------------------------------
# Task 2: Calculate and print the percentage of total stock for each item.
