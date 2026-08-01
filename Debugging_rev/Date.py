# while True:
# date = input("Enter the date (DD-MM-YYYY): ")
#     test = date
#     if len(test)= 10 and test[2]=="-" and test[5]=="-":
#         day = int(test[0:2])
#         month = int(test[3:])
#         year = int(test[6:])
#         check_year = year>1900 and year<=2000
#         check_month = month>=1 or month<=12
#         check_day_31 = day<=31 and (month in [1,3,5,7,8,10,12])
#         check_day_30 = day<=31 and (month in [4,6,9,11])
#         check_day_Feb = month == 0 and ((day<=29 and year%4==0) or day<=28)
#         if check year:
#             if check_month:
#                 if check_day_31 or check_day_30 or check_day_Feb
#                     break
#                 else:
#                     print("Error in day")
#             else:
#                 print("Error in year")
#         else:
#             print("Error in month")
#     else:
#         print(Error in format")
# print("Date accepted")

while True:
    date = input("Enter the date (DD-MM-YYYY): ") #1 indentation
    test = date
    if len(test)== 10 and test[2]=="-" and test[5]=="-": #2 == not = 
        day = int(test[0:2])
        month = int(test[3:5]) #7 check the 2 digits in the month section
        year = int(test[6:])
        check_year = year>1900 and year<=2026 #3 2026 as current year not 2000
        check_month = month>=1 and month<=12 #11 must satisfy these 2 conditions between 1 and 12
        check_day_31 = day<=31 and (month in [1,3,5,7,8,10,12])
        check_day_30 = day<=30 and (month in [4,6,9,11]) #12 30 not 31
        check_day_Feb = month == 2 and ((day<=29 and year%4==0) or day<=28) #10 february is 2 not 0
        if check_year: #4 check year is not an appropriate variable
            if check_month:
                if check_day_31 or check_day_30 or check_day_Feb: #5 colon needed
                    break
                else:
                    print("Error in day") 
            else:
                print("Error in month") #8 should be month instead
        else:
            print("Error in year") #9 should be year instead
    else:
        print("Error in format") #6 Open inverted commas needed to print the string
print("Date accepted")
