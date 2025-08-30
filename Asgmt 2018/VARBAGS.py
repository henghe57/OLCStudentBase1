# Qn 8
bags_rice = int(input("Enter how many bags of rice: "))
upper_bound = 5.1
lower_bound = 4.9
counter_under = 0
counter_over = 0
for count in range(bags_rice):
 bag_weight = float(input("Enter the weight of the bag of rice "))
 if bag_weight > upper_bound:
  print("The bag of rice is overweight")
  counter_over += 1
 if bag_weight < lower_bound:
  print("The bag of rice is underweight")
  counter_under += 1
 if bag_weight >= lower_bound:
  if bag_weight <= upper_bound:
    print("The bag of rice is the correct weight.")
print(counter_over, "bags are overweight")
print(counter_under, "bags are underweight")