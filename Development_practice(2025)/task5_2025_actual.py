# Task 5.1

def total_cost(cost):
    total = cost + (cost * 0.09) #add 9% tax back to origin price
    return total
# print(total_cost(100)) # Will give $109 because of 9% tax
#-----------------------------------------------------
# Task 5.2

def discount(cost):
    total = total_cost(cost)
    if total >= 50 and total < 100:
        total -= (total * 0.05) #5% discount
    elif total >= 100:
        total -= (total * 0.10) #10% discount
    return total

# print(discount(40)) # Will give 0% discount -> $43.60
# print(discount(50)) # Will give 5% discount -> $51.775
# print(discount(100)) # Will give 10% discount -> $98.10
#-----------------------------------------------------
# Task 5.3

def reward_points(total):
    # 3 reward points for each whole dollar spent
    points = int(total) * 3
    return points
# print(reward_points(51.775)) # Will reward 153 for every $1 spent 
#-----------------------------------------------------
# Task 5.4

def voucher(total, customer_name):
    total = discount(total)
    customer_name = ""
    v_code = ""
    if total > 25 and total <= 50: 
        v_code = customer_name[0:3] + "05PERCENT"
    elif total > 50:
        v_code = customer_name[0:3] + "10PERCENT"
    else:
        v_code = None
    return v_code
print(voucher(20, "henghyi")) # Will give no voucher code
print(voucher(40, "henghyi")) # Will give voucher code with 5 percent
print(voucher(100, "henghyi")) # Will give voucher code with 10 percent 
#-----------------------------------------------------
# Task 5.5

def main():
    print("Welcome to the Sales System\n")

    first_name = input("Enter your first name: ")
    cost = float(input("Enter the cost of your sale: "))
    # calculate totals using functions
    total_before_discount = total_cost(cost)
    total_after_discount = discount(cost)
    points = reward_points(total_after_discount)
    voucher_code = voucher(total_after_discount, first_name)

    # output the receipt
    print("\n========Receipt========")
    print(f"Customer: {first_name}")
    print(f"Total cost of the sale with tax: {total_before_discount}")
    print(f"Discounted price of the sale: {total_after_discount}")
    print(f"Reward points earned: {points}")

    if voucher_code:
        print(f"Voucher code: {voucher_code}")
        with open("vouchercode.txt", "w") as file:
            file.write(voucher_code)
    else:
        print("You need to spend over $25 for a voucher code.")
    
    print("======================")
    print("Thank you for your purchase!")
main()