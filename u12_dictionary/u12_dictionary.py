#key and value pair 
'''
#define a dictionary 
countries = {"malaysia":"kuala lumpur","china":"beijing","indonesia":"jakarta"}
cap1 = countries["malaysia"]
print(cap1)

#add to dictionary 
countries["japan"] = "tokyo" # if the key does not exist, it will add it 
print(countries)

#change a value in dictionary 
countries["japan"] = "osaka" # if the key does exist, it will change the value 
print(countries)

#delete a key / value pair from dictionary 
del countries["malaysia"]
print(countries)

#check whether a particular key exist in dictionary # existance check
if "malaysia" in countries:
    print("malaysia exists")
else:
    print("malaysia does not exist")

# how to loop through all the key / value pairs in dictionary 
for country, capital in countries.items():
    print(country)
    print(capital)
    print(f"The capital of {country} is {capital}")

'''

#### Code a Restaurant Ordering Program

# Task 1: Create a dictionary containing 3 food items and their prices

# Task 2: Ask customer what they want to eat?

# Task 3: Check if order is available
            # if available, print the price
            # else, tell customer not available

foods = {"burger":"$5.00","fries":"$2.00","sushi":"$10.00"}

print("Menu Items")
for food, price in foods.items():
        # print(f"The price of the {food} is {price}")
        print(food)

questioning = input("what would you want to order? ")

if questioning in foods: # if this is true, means customer ordered something in the menu
    print(f"The price of the {questioning} is {price}")
else:
    print("State what you want to order according to the food menu.")




