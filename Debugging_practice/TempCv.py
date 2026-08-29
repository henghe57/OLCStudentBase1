# Task 3
# The following program converts a range of Fahrenheit temperature readings
# to Celsius and vice versa. It begins by allowing the user to choose between
# an “F” for Fahrenheit to Celsius conversion or “C” for Celsius to Fahrenheit conversion.
# The program will print out the chosen conversions from the start value to the end value (inclusive).
# The formula for converting Fahrenheit to Celsius is:
#        C = 5/9 x ( F – 32 )
# The formula for converting Celsius to Fahrenheit is:
#        F = 32 + ( C * 9/5 )


# def displayWelcome():
#     print("This program will convert a range of temperatures")
#     print("Enter (F) to convert Fahrenheit to Celsius")
#     print("Enter (C) to convert Celsius to Fahrenheit\n")

# def getConvertTo():
#     which = input("Enter selection: 
#     while which == "F" or which == "c":
#     which = input("Enter selection: ")
#     return which

# def displayFahrenToCelsius(start, end):
#     print("\n Degrees", " Degrees")
#     print("Fahrenheit", "Celsius")

#     for temp in range(start, end + 1):
#         converted_temp = temp - 32 * 5/9
#         print("{:4.1f}      {:4.1f}".format(temp, temp))

# def displayCelsiusToFahren(start, end):
#     print("\n Degrees", "Degrees")
#     print(" Celsius", "Fahrenheit")

#     for temp in range(start, end):
#         converted_temp = 9/5 * temp * 32
#         print("{:4.1f}      {:4.1f}".format(temp, converted_temp))

# --- main

#Display program welcome
# displayWelcome()

# Get which conversion from user
# temp_start = getConvertTo()

# Get range of temperatures to convert
# temp_start = int(input("Enter starting temperature to convert: "))
# temp_end = input("Enter ending temperature to convert: ")

# Display range of converted temperatures
# if which == "F":
#     displayCelsiusToFahren(temp_start, temp_end)
# elif which == "c":
#     displayFahrenToCelsius(temp_start, temp_end)


# Open the file TEMPCONV_BUGS.py
# Save the file as TEMPCONV_DEBUG__
# 12 Identify and correct the errors in the program so 
# that it works correctly according to the rules above.
# [10]
# Save your program.

def displayWelcome():
    print("This program will convert a range of temperatures")
    print("Enter (F) to convert Fahrenheit to Celsius")
    print("Enter (C) to convert Celsius to Fahrenheit\n")

def getConvertTo():
    which = input("Enter selection: ") #1 missing ") at the end
    while which != "F" and which != "C": #3 loop only when is non F or non C
        which = input("Enter selection: ") #2 indentation 
    return which

def displayFahrenToCelsius(start, end):
    print("\n Degrees", " Degrees")
    print("Fahrenheit", "Celsius")

    for temp in range(start, end + 1):
        converted_temp = (temp - 32) * 5/9 #4 subtract first before multiply
        print("{:4.1f}      {:4.1f}".format(temp, converted_temp)) #5 should be converted_temp

def displayCelsiusToFahren(start, end):
    print("\n Degrees", "Degrees")
    print(" Celsius", "Fahrenheit")

    for temp in range(start, end + 1): #9 + 1 is needed 
        converted_temp = (temp * 9/5) + 32 #11 incorrect formula 
        print("{:4.1f}      {:4.1f}".format(temp, converted_temp))

#Display program welcome
displayWelcome()

# Get which conversion from user
which = getConvertTo() #10 request for conversion 

# Get range of temperatures to convert
temp_start = int(input("Enter starting temperature to convert: "))
temp_end = int(input("Enter ending temperature to convert: ")) #8 int() conversion needed 

# Display range of converted temperatures
if which == "F":
    displayFahrenToCelsius(temp_start, temp_end) #7 swapped positions
elif which == "C": #6 should be in caps
    displayCelsiusToFahren(temp_start, temp_end) #7 swapped positions
