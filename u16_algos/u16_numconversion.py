conversion_factors = {
    "B": 1,
    "kB": 1000,
    "MB": 1000**2,
    "GB": 1000**3,
    "TB": 1000**4,
    "PB": 1000**5,
    "KiB": 1024,
    "MiB": 1024**2,
    "GiB": 1024**3,
    "TiB": 1024**4,
    "PiB": 1024**5
}

def is_valid_unit(unit):
    if unit not in conversion_factors:
        return False
    else:
        return True
    
# print(is_valid_unit("PiB")) # True
# print(is_valid_unit("XB"))  # False

# ________________________________________
# Task 4.3 – Conversion Function [7 marks]
# Write a function named convert_storage(value, from_unit, to_unit) that:
# •	Takes in three parameters:
# o	value (a numeric value to convert)
# o	from_unit (the current unit)
# o	to_unit (the target unit)
# •	Converts the value using the following steps:
# 1.	Multiply the value by the conversion factor of the source unit to get the number of bytes
# 2.	Divide the number of bytes by the conversion factor of the target unit to get the result
# •	Returns the final result as a float
# Use the conversion_factors dictionary for all conversions.
# Do not perform any user input or output in this function.
# Do not use if or elif statements to check unit names.
# This function must correctly handle:
# •	Conversion from a larger unit to a smaller unit (e.g. GB → MB)
# •	Conversion from a smaller unit to a larger unit (e.g. KiB → GiB)
# def convert_storage(value, from_unit, to_unit):
#     values = 1
#     from_unit = "PB"
#     to_unit = "TB"
#     conv_value = conversion_factors[from_unit] * values
#     conv_value2 = conversion_factors[to_unit] 
#     final_value = conv_value / conv_value2
#     return final_value
# print(convert_storage(1,"PB","TB")) # Method 1

def convert_storage(value, from_unit, to_unit):
    conv_value = conversion_factors[from_unit] * value
    # print(conv_value)
    final_value = conv_value / conversion_factors[to_unit]

    return final_value
print(convert_storage(1, "TB", "PB"))

# # ________________________________________
# # Task 4.4 – User Interaction [8 marks]
# # Write the main program that:
# # •	Repeatedly prompts the user to input:
# # o	A numeric value
# # o	A source unit
# # o	A target unit
# # •	Validates that:
# # o	The numeric value is positive. 
# # o	Both units are supported using the is_valid_unit() function
# # •	Calls the convert_storage() function to perform the conversion
# # •	Displays the result to 4 decimal places, e.g.:
# # •	10 MB is approximately 9.5367 MiB
# # •	Asks the user whether they want to convert another value
# # o	If the user enters "yes", repeat the process
# # o	If the user enters "no", end the program

while True:
    value_num = float(input("Enter a number to convert: "))

    # validate

    if value_num > 0:
        print(f"{value_num} is valid.")
        break
    else:
        print(f"{value_num} is not valid. You must enter a positive number.")
while True:
    from_unit = input("Enter a unit to convert from: ")
    if is_valid_unit(from_unit):
        print(f"{from_unit} is valid.")

        # ask for valid to unit
        to_unit = input("Enter a unit to convert to: ")

        if is_valid_unit(to_unit):
            output_val = convert_storage(value_num, from_unit, to_unit)
            output_val = round(output_val, 4) # round off to 4 decimal places. 

            # tell the answer
            # 1000 TB is 1PB
            print(f"{value_num} {from_unit} is {output_val} {to_unit}")
            break
        else:
            print(f"{to_unit} is not valid. Try again.")
    else:
        print(f"{from_unit} is not valid. Try again.")