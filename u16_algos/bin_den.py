#------------------------------------------------------------
# For Loops through List
#------------------------------------------------------------

# Exercise 1: Printing Items (Method 1)
# Given fruits = ["apple", "banana", "cherry"]
# Use a for loop to print each fruit directly.
# Output example:
# I like to eat apple.
# I like to eat banana.
# I like to eat cherry.
given_fruits = ["apple","banana","cherry"]
for a in given_fruits:
    print(f"I like to eat {a}.")

print("------------------------------------------------------------")
# Exercise 2: Printing Items (Method 2)
# Given the same fruits list
# Use for i in range(len(fruits)) to print the items.
# Output example:
# Fruit 1: apple
# Fruit 2: banana
# Fruit 3: cherry
for i in range(len(given_fruits)):
    print(f"I like to eat {given_fruits[i]}.")


print("------------------------------------------------------------")
# Exercise 3: Numbers Greater than 50
# Given numbers = [12, 67, 45, 89, 23]
# Use a for loop to print only numbers greater than 50.
# Expected Output:
# 67
# 89
given_numbers = [12,67,45,89,23]
for a in given_numbers:
    if a > 50:
        print(a)
print("------------------------------------------------------------")
# Exercise 4: Mapping Students to Scores
# students = ["Ali", "Bala", "Cindy"]
# marks = [55, 80, 62]
# Use a for loop to combine them into a dictionary.
# Expected Output:
# {"Ali": 55, "Bala": 80, "Cindy": 62}
students = ["Ali", "Bala", "Cindy"]
marks = [55, 80, 62]
students_marks = {}
for i in range(len(students)):
    current_student = students[i]
    current_marks = marks[i]
    students_marks[current_student] = current_marks
print(students_marks)
print("------------------------------------------------------------")
# While Loop Validation
#------------------------------------------------------------

# Exercise 5: Length Check
# Keep asking user for a username until it has at least 5 characters.
# check to ensure that username is all alphabets
while True:
    word = input("Enter a 5-letter word: ")
    if len(word) >= 5 and word.isalpha():
        print(f"The word {word} is a valid 5-letter word.")
        break
print("----------------------------------------------------------------")
# Exercise 6: Numbers Only
# Keep asking user to enter age until input contains digits only.
while True:
    num = input("Enter only numbers: ")
    if num.isdigit():
        print(f"{num} is valid.")
        break
print("----------------------------------------------------------------")
# Exercise 7: Uppercase Only
# Keep asking until user enters a code in uppercase letters only.
while True:
    user = input("Enter an uppercase word: ")
    if user.isupper():
        print(f"{user} is valid.")
        break
print("----------------------------------------------------------------")
# Exercise 8: Lowercase Only
# Keep asking until user enters an email in lowercase only.
while True:
    email = input("Enter your email: ")
    if email.islower() and "@gmail.com" in email:
        print(f"{email} is valid.")
        break
print("----------------------------------------------------------------")
# Exercise 9: Password Validation
# Keep asking until user enters a password with length >= 8.
while True:
    password = input("Enter a valid password: ")
    if len(password) >= 8:
        print(f"The password {password} is accepted.")
        break
# (a) Input and validation [5 marks]
# Write a function get_valid_number(base) that:
# •	Accepts a parameter base which can be 2 or 10.
# •	Repeatedly asks the user to enter a number in that base until a valid number is provided.
# •	Checks that:
# o	For base 2: input only contains characters 0 and 1.
# o	For base 10: input only contains digits 0–9 (treat the value as a non-negative integer).
# •	Returns the number string (no leading/trailing spaces).
# Hint: Use .strip() and validate all characters before returning.

    

# (b) Denary → Binary [6 marks] 
# Write a function den_to_bin(den_num) that: 
# Uses repeated division by 2, taking the remainder each time, 
# Builds the binary string by prepending each remainder, 
# Returns "0" if the input is 0, 

# Assumes den_num is a non-negative integer 
# (you may convert the validated string to int before calling this). 
# Example: den_to_bin(251) should return "11111011". 


