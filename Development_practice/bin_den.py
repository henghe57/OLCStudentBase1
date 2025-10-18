# Task 4 — Number Base Conversion Utility (25 marks)
# You are to develop a small Python program to validate bases and numbers, 
# convert between binary and denary, and provide a menu-driven main program. 
# Write clear, user-friendly input/output messages. 
# Use meaningful identifiers, functions, and inline comments 
# to explain your logic where appropriate. (4 marks)





# ________________________________________
# (a) Validate number for a base (45 marks)
# Function to write: check_valid_num(num, base)

# Specification:
# Write a function that accepts num and base, and returns True 
# if every character in num is valid in that base, otherwise False.
# •	Support bases "2", "10", "16".
# •	Validation rules:
# o	Base 2: digits 0–1 only
# o	Base 10: digits 0–9 only
# o	Base 16: digits 0–9 and letters A–F (case-insensitive)
# •	You may assume num contains no leading +/- signs and no spaces.

# Examples:
# •	check_valid_num("10110", "2") → True
# •	check_valid_num("19A", "16") → True
# •	check_valid_num("19G", "16") → False
# •	check_valid_num("1201", "2") → False

def check_valid_num(num, base):
    # change to string for checking
    num = str(num).upper()
    base = str(base)

    for i in num:
        if base == "2" and i not in "01":
            return False
        elif base == "10" and i not in "0123456789":
            return False
        elif base == "16" and i not in "0123456789ABCDEF":
            return False
    
    return True





# ________________________________________
# (b) Binary → Denary conversion (6 marks)
# Function to write: bin_to_den(binstring)
# Specification:
# Write a function that accepts a binary string (e.g., "1101") and 
# returns the denary integer equivalent. 

# Implement the place-value algorithm:
# •	Process bits from least significant to most significant (you may reverse the string).
# •	Build a list of place values [2**0, 2**1, 2**2, ...] matching the length of the string.
# •	Accumulate the total by multiplying each bit by its corresponding place value.

# Examples:
# •	bin_to_den("0") → 0
# •	bin_to_den("1") → 1
# •	bin_to_den("1111") → 15


def bin_to_den(binstring):
    binstring = str(binstring)
    # Reverse the binary string to process least significant bit first
    flippedbin = binstring[::-1]

     # Generate the place-value list [2**0, 2**1, ...]
    place_values = []
    for i in range(len(binstring)):
        place_values.append(2**i)

    dennum = 0
    for i in range(len(flippedbin)):
        current_den = place_values[i] * int(flippedbin[i])
        dennum = dennum + current_den

    return dennum







# ________________________________________
# (c) Denary → Binary conversion (6 marks)
# Function to write: den_to_bin(den_num)
# Specification:
# Write a function that accepts a non-negative denary integer and 
# returns its binary string representation without using built-in 
# formatters (e.g., no bin(), no format() with base). 
# 
# Use repeated division by 2:
# •	Handle the special case 0 → "0".
# •	Otherwise, repeatedly divide by 2, prepend each remainder 
# to a string, and stop when the quotient becomes 0.

# Examples:
# •	den_to_bin(0) → "0"
# •	den_to_bin(6) → "110"
# •	den_to_bin(13) → "1101"



def den_to_bin(den_num):
    if den_num == 0:
        return "0"
    
    binary_string = "" # temporary value
    num = int(den_num)

    while num > 0 : # keep dividing by 2 until quotient is zero
        remainder = num % 2 # find the remainder after division by 2
        binary_string = str(remainder) + binary_string # add remainder to string at front
        num = num // 2 # update remainder to num

    return binary_string

# print(den_to_bin(231))






# ________________________________________
# (d) Main program (5 marks)
# Objective:
# Write a menu-driven main program that allows the user to 
# choose a conversion, validates inputs using your earlier functions, 
# performs the conversion, and displays clear results. Your program should:

# 1.	Display a menu with these options:
# 2.	(1) Binary → Denary
# 3.	(2) Denary → Binary
# 4.	(3) Exit
# 5.	Repeat until Exit is chosen.
# 6.	For each chosen conversion:
# o	Prompt for the appropriate base using your get_valid_base function to validate it.
# -	For option (1), the base expected is 2.
# -	For option (2), the base expected is 10.
# -	If the base is invalid, prompt again until a valid base is given.

# o	Prompt for the number to convert and validate it with check_valid_num.
# -	Re-prompt until a valid number for that base is provided.
# o	Call the relevant conversion function:
# -	Option (1): bin_to_den
# -	Option (2): den_to_bin
# o	Output in a clear format, e.g.:
# -	Binary 11111011 = Denary 251
# -	Denary 255 = Binary 11111111
# 7.	After each operation, continue to show the menu 
# until the user selects Exit, then print a closing message.
# ________________________________________

while True:
    # user = input("Choose a conversion: \n"
    # "Option (1): Denary to Binary\n" 
    # "Option (2): Binary to Denary\n"
    # "Option (3): Exit\n")
    print("Option (1): Denary to Binary")
    print("Option (2): Binary to Denary")
    print("Option (3): Exit")
    user = input("Choose a conversion: ")
    if user == "3":
        break
    elif user == "1":
            option1 = input("Enter a denary number: ")
            if check_valid_num(option1, "10"):
                den_to_bin(option1)
                print("Valid base.")
                converted1 = den_to_bin(option1)
                print(f"Denary {option1} = Binary {converted1}")
            else:
                print("Invalid base, please enter a valid denary number: ")
    elif user == "2":
            option2 = input("Enter a binary number: ")
            if check_valid_num(option2, "2"):
                bin_to_den(option2)
                print("Valid base.")
                converted2 = bin_to_den(option2)
                print(f"Binary {option2} = Denary {converted2}")
            else:
                print("Invalid base, please enter a valid binary number: ")