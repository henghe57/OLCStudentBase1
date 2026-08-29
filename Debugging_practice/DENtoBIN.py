# Task 3
# The following program should read a denary non-negative integer from the user. 
# The program will then convert the denary integer to its 
#    binary value and print it to the screen. 
# The “division by 2” method is employed to carry out the conversion. 
# There are several syntax errors and logical errors in the program.

# NEW_BASE == 3
# num = Input("Enter a non-negative integer: "
# num = float(num)
# result = ""
# q = num
# r = q % NEW_BASE
# result = str(r) + result
# q = q // NEW_BASE
# while q > 0
#     r = q % NEW_BASE
#     result = result + str(r)
#     q = q / NEW_BASE
#     print(result, "in Decimal is", num, "in Binary.")

# Open the file D2B.py
# Save the file as MYD2B___
# 
# Identify and correct the errors in the program so that it 
# works correctly according to the description above. Save your program.
#  [10] 

NEW_BASE = 2 #1 assigning of variable requires '=' + #6 % 2 as bin uses only 0 and 1 
num = input("Enter a non-negative integer: ") #2 missing ) + #9 input small letter case 
num = int(num) #3 int() only as bin doesnt contain decimals
result = ""
q = num
r = q % NEW_BASE 
result = str(r) + result
q = q // NEW_BASE
while q > 0: #4 colon needed
    r = q % NEW_BASE
    result = str(r) + result #10 should add r to the front
    q = q // NEW_BASE #7 floor divisor to attain quotient not / as that is divide 
print(num, "in Decimal is", result, "in Binary.") #5 print outside of loop + #8 reverse variables for num and result to match sentence