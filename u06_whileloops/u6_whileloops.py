#------------------------------------------------------------
# Exercise 1: Count Up
# Print numbers from 1 to 5 using a while loop.
# Example Output: 1 2 3 4 5
#------------------------------------------------------------
num = 1
while num <= 5:
    print(num, end=" ")
    num += 1
print('\n')
#------------------------------------------------------------
# Exercise 2: Count Down
# Print numbers from 10 down to 1 using a while loop.
# Example Output: 10 9 8 ... 1
#------------------------------------------------------------
num = 10 
while num >= 1:
    print(num, end=" ")
    num -= 1
print('\n')
#------------------------------------------------------------
# Exercise 3: Even Numbers Until N
# Ask for an integer N. Print all even numbers from 2 up to N inclusive.
# Sample Input: 12
# Example Output: 2 4 6 8 10 12
#------------------------------------------------------------
num = 2
while num <= 12:
    print(num, end=" ")
    num += 2
print('\n')
#------------------------------------------------------------
# Exercise 4: Summation with While
# Calculate the sum of numbers 1 to 100.
# Example Output: 5050
#------------------------------------------------------------
total = 0
num = 1
while num <= 100:
    total += num 
    num += 1
print(total)
print('\n')
#------------------------------------------------------------
# Exercise 5: Multiplication Table
# Ask for an integer x. Print its first 10 multiples in "x * i = value" format.
# Sample Input: 7
# Example Output:
# 7 * 1 = 7
# 7 * 2 = 14
# 7 * 3 = 21
#------------------------------------------------------------
count = 1
x = input("Enter an integer in the multiplication table: ")
while count <= 10:
    print(f"{x} x {count} = {int(x) * count}")
    count += 1
print('\n')
#------------------------------------------------------------
# Exercise 6: While True + break 
# Repeatedly ask for integers and add them to a total.
# Stop when user enters "END" (case-insensitive).
# Print total after stopping.
# Sample Inputs: 10, 20, 5, END
# Example Output: Total = 35
#------------------------------------------------------------
total = 0
while True:
    user = input("Keep entering integers, enter END to stop: ")
    if user == "END":
        break
    else:
        total += int(user)
print(f"Total = {total}")
print('\n')
#------------------------------------------------------------
# Exercise 7: While True  (Skip Negatives)
# Repeatedly accept integers. If number is negative, skip and ignore it.
# Stop on 0. Print count of valid positives and their sum.
# Sample Inputs: -3, 5, 12, -1, 4, 0
# Example Output: Count = 3, Sum = 21
#------------------------------------------------------------
sum = 0
counter = 0
while True:
    user = int(input("Keep entering integers, enter 0 to end: "))
    if user == 0:
        break
    elif user > 0:
        sum += user
        counter += 1
print(f"Count = {counter}, Sum = {sum}")
print('\n')
#------------------------------------------------------------
# Exercise 8: Presence Check (Non-Empty String)
# Ask for a name. Keep asking until a non-empty name is entered.
# Then greet the user.
# Sample Input: "" -> "   " -> "Alex"
# Example Output: Hello, Alex!
#------------------------------------------------------------
name = ""
while name.strip() == "":
    name = input("Enter your name: ")
print(f"Hello, {name}!")
print('\n')
#------------------------------------------------------------
# Exercise 9: Length Check (Username)
# Ask for a username that must be 5 to 12 characters long.
# Keep prompting until valid, then print "Username accepted".
# Sample Inputs: "ab" (invalid), "student01" (valid)
#------------------------------------------------------------
name = ""
while True:
    name = input("Enter username: ")
    if len(name) >= 5 and len(name) <= 12:
        break
    else:
        print("Invalid username.")
print(f"{name} accepted.")
print('\n')
#------------------------------------------------------------
# Exercise 10: Range Check (Quiz Score)
# Ask for an integer score between 0 and 100 inclusive.
# Keep prompting until valid, then print "Score recorded: ".
# Sample Inputs: 120 (invalid), -5 (invalid), 85 (valid)
#------------------------------------------------------------
while True:
    score = int(input("Enter integer score between 0 and 100: "))
    if score >= 0 and score <= 100:
        break
    else:
        print("Invalid score.")
print(f"Score recorded: {score}")
print('\n')
#------------------------------------------------------------
# Exercise 11: Format Check (Positive Integer Only)
# Ask for an input that must be a positive integer that is more than 0 (e.g., "42", "85").
# If letters or symbols appear, ask again.
# Sample Inputs: "abc" -> "-4" -> "12" (valid)
#------------------------------------------------------------
while True:
    number = input("Enter a positive integer: ")
    if number.isdigit() and int(number) > 0:
        break
    else:
        print("Invalid positive integer.")
print(f"{number} is valid.")
print('\n')
#------------------------------------------------------------
# Exercise 12: Format Check (Email)
# Ask for an email that must contain exactly one '@' and at least one '.' after it.
# No spaces allowed. Keep asking until valid, then print "Email accepted".
# Sample Inputs: "userexample.com" (invalid), "user@site.com" (valid)
#------------------------------------------------------------






#------------------------------------------------------------
# Exercise 13: Existence Check (Course Code)
# Given list: valid_codes = ["7155", "8640", "9421", "3562"]
# Ask user for a course code. Repeat until code exists in list.
# Print "Code found" when valid.
# Sample Inputs: "2026" (prints invalid), "9421" (prints valid)
#------------------------------------------------------------






#------------------------------------------------------------
# Exercise 14: Combined Checks (Password Policy)
# Requirements:
# - Non-empty
# - Length between 8 and 16
# - Must contain at least one digit 0-9
# - No spaces
# Keep prompting until valid, then print "Password set".
# Sample Inputs: "abc" (invalid), "abcd efgh1" (invalid), "GoodPass1" (valid)
#------------------------------------------------------------






#------------------------------------------------------------
# Exercise 15: Menu Loop
# Menu:
# (1) Add number
# (2) Show total
# (3) Reset total
# (4) Exit
# Handle invalid choice with "Invalid choice" and continue.
# For (1), ask integer & add to total. For (2), show total. For (3), reset.
# For (4), break loop and print "Goodbye".
#------------------------------------------------------------






#------------------------------------------------------------
# Exercise 16: Bounded Attempts (PIN Validation)
# Correct PIN = "2468"
# User has up to 3 attempts.
# Checks:
# - Non-empty
# - Exactly 4 digits
# - Digits only
# If correct, print "Access granted" and stop.
# if incorrect, print out incorrect reason
# If all attempts used, print "Access denied".
#------------------------------------------------------------






#------------------------------------------------------------
# Exercise 17: Clean List Input
# Ask user to enter positive integers separated by commas, e.g. "3,5,10".
# Validation:
# - Not empty
# - Each item integer only (no letters, decimals)
# - Each integer between 1 and 100 inclusive
# Repeat until valid, then print list length and sum.
# Sample Inputs: "3,5,200" (invalid), "3,five" (invalid), "2,10,8" (valid)
#------------------------------------------------------------






#------------------------------------------------------------
# Exercise 18: Date String Format Check (DD-MM)
# Ask for a date in "DD-MM" format:
# - Exactly 5 characters
# - '-' at position 3
# - DD between 01 to 31
# - MM between 01 to 12
# Repeat until valid, then print "Date accepted: ".
#------------------------------------------------------------






#------------------------------------------------------------
# Exercise 19: Unique Username
# Existing list: taken = ["amy", "bala", "charlie", "debin", "eliza"]
# Ask for username:
# - Not empty
# - Length 3 to 12
# - Not already in 'taken' (case-sensitive)
# Keep asking until valid, add it to taken list, then print "Registered: ".
#------------------------------------------------------------







#------------------------------------------------------------
# Exercise 20: SKU Validation
# Valid SKUs: ["A-1001", "B-2400", "C-0350", "Z-9999"]
# Input rules:
# - Not empty
# - Format: Letter '-' followed by 4 digits
# - Must exist in valid_skus
# Keep asking until valid, then print "SKU verified".
#------------------------------------------------------------






#------------------------------------------------------------
# Exercise 21: Password Confirmation
# Ask for password:
# - Non-empty
# - Length 8 to 16
# - Must include at least one uppercase and one digit
# If pass validation above, ask again to confirm. If mismatch, print "Mismatch" and restart.
# When valid and confirmed, print "Password confirmed".
#------------------------------------------------------------





#------------------------------------------------------------
# Exercise 22: Bounded Range Collector
# Collect 5 valid integers between 1 and 50 inclusive.
# If invalid (format/range), print "Invalid" and retry without counting.
# After 5 valid numbers, print min and max.
# Sample Inputs: 10, 50, 1, 33, 25
# Output: Min=1, Max=50
#------------------------------------------------------------
