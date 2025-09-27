## stores the function in computer memory
def hello():
  print("Hello, world.")

# call the function
hello()

print("----------------")

name = "Qistina"
def greeting(name):
  print(f"Hello, {name}")

greeting("Heng Hyi")
greeting(name)

print("----------------")

def add_numbers(num1, num2):
  ans = num1 + num2
  print(f"{num1} + {num2} = {ans}")

add_numbers(10, 20)

print("---------------------------------------")

list1 = [14, 17, 56, 78, 49, 89, 34, 81, 21, 45]

def iseven(number):
  if number % 2 == 0:
    return True
  else:
    return False

for i in list1:
  if iseven(i):
    print(f"{i} is an even number.")
  else:
    print(f"{i} is an odd number.")

print("---------------------------------------")

def greet_users(namelist):
  for name in namelist:
    print(f"Hello, {name}")

greet_users(["Alice", "Bob", "Charlie"])

print("---------------------------------------")

# with 1 variable
# def calculator(num1, num2, operator):
def calculator(num1, num2, operator):
  if operator == "+":
    total = num1 + num2
  elif operator == "-":
    total = num1 - num2
  elif operator == "*":
    total = num1 * num2
  elif operator == "/":
    total = num1 / num2
  return total
print(calculator(10,5,"/"))

print("---------------------------------------")

def is_palindrome(word):
  if word == word[::-1]:
    return True
  else:
    return False
  
print("Is 'radar' a palindrome? {}".format(is_palindrome("radar")))
print("Is 'hello' a palindrome? {}".format(is_palindrome("hello")))

print("---------------------------------------")

def area_rectangle(length, breadth):
  area = length * breadth 

  return area

area1 = area_rectangle(31,47)
area2 = area_rectangle(56,77)

print(f"The total area of area1 and area2 is {area1 + area2}")

# line of execution
# 71, 66, 67, 69, 71 # phase 1
# 72, 66, 67, 69, 72 # phase 2
