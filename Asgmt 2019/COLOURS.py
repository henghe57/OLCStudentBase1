# This is a backup of original buggy code.

# colour_list = ['red','green', 'blue','orange', 'purple','yellow']
# colour_to_find = input("Which colour would you like to search for? ")
# items = len(colour_to_find)
# item_number = 0
# colour_found = False
# while colour_found == True:
#     while item_number > items:
#         if colour_list[item_number] = colour_to_find
#             print("There are " + str(item) + " colours in the list, " + colour_to_find + " is item " + str(iten_number - 1) + " in the list.")
#             colour_found = True
#             item_number = item_number
#         elif item_number == items - 1:
#             print("The colour is not in the list. ")
#             colour_found = False
#             item_number = items
#         else:
#             item_number = items

colour_list = ['red','green', 'blue','orange', 'purple','yellow']
colour_to_find = input("Which colour would you like to search for? ")
items = len(colour_list) #4, Should be length of list
item_number = 0
colour_found = False 
while colour_found == False: #3. Set false first to start loop
    while item_number < items: #5. Should be less items cuz 0 can't be more than 6 in that list
        if colour_list[item_number] == colour_to_find: #1. Missing colon + #2. == not = 
            print("There are " + str(items) + " colours in the list, " + colour_to_find + " is item " + str(item_number + 1) + " in the list.") #8. iten_number is wrong + #9. items not item + #11. +1 not -1
            colour_found = True
            item_number += items #6. should set to the length to exit the loop 
        elif item_number == items - 1:
            print("The colour is not in the list. ")
            colour_found = True #7. set to true to exit the loop
            item_number = items
        else:
            item_number += 1 #10. increment by 1
# Total: 11 errors