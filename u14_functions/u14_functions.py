## stores the function in computer memory
def hello():
  print("Hello, world.")

# call the function
hello()

print("----------------")

name = "Qis"
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
def calculator(x, y, z):
  if z == "+":
    total = x + y
  elif z == "-":
    total = x - y
  elif z == "*":
    total = x * y
  elif z == "/":
    total = x / y
  return total
print(calculator(10,5,"/"))