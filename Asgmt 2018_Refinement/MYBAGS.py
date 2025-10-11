# The following program allows the weights of 15 bags of rice to be input. The correct weight for each bag of rice must be between 4.9 kg and 5.1 kg inclusive.

# bags_rice = 15
# upper_bound = 5.1
# lower_bound = 4.9
# for count in range(bags_rice):
#     bag_weight = float(input("Enter the weight of the bag of rice "))
#     if bag_weight > upper_bound:
#         print("The bag of rice is overweight")
#     if bag_weight < lower_bound:
#         print("The bag of rice is underweight")

# Qn 7A
# bags_rice = 10
# upper_bound = 5.1
# lower_bound = 4.9
# for count in range(bags_rice):
#     bag_weight = float(input("Enter the weight of the bag of rice "))
#     if bag_weight > upper_bound:
#         print("The bag of rice is overweight")
#     if bag_weight < lower_bound:
#         print("The bag of rice is underweight")

# Qn 7B
# bags_rice = 10  #change from 15 to 10
# upper_bound = 5.1
# lower_bound = 4.9
# for count in range(bags_rice):
#  bag_weight = float(input("Enter the weight of the bag of rice "))
#  if bag_weight > upper_bound:
#   print("The bag of rice is overweight")
#  if bag_weight < lower_bound:
#   print("The bag of rice is underweight")
#  if bag_weight >= lower_bound and bag_weight <= upper_bound:
#   print("The bag of rice is the correct weight.")

# Qn 7C
# bags_rice = 10  #change from 15 to 10
# upper_bound = 5.1
# lower_bound = 4.9
# counter_under = 0
# counter_over = 0
# for count in range(bags_rice):
#  bag_weight = float(input("Enter the weight of the bag of rice "))
#  if bag_weight > upper_bound:
#   print("The bag of rice is overweight")
#   counter_over += 1
#  if bag_weight < lower_bound:
#   print("The bag of rice is underweight")
#   counter_under += 1
#  if bag_weight >= lower_bound:
#   if bag_weight <= upper_bound:
#     print("The bag of rice is the correct weight.")
# print(counter_over, "bags are overweight")
# print(counter_under, "bags are underweight")
