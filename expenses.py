
#for loop
""" 
expenses = [10.50, 8, 5, 15, 20, 5, 3]

sum = 0

for x in expenses:
    sum = sum + x

print("You spent $", sum, sep = '')


#using sum method

expenses = [10.50, 8, 5, 15, 20, 5, 3]

total = sum(expenses)

print("You spent $", total, sep = '')


expenses = [10.50, 8.50, 5.30, 15.05, 20.00, 5.00, 3.00]

user_new_spent = expenses.append(float(input("How much did you spent?\n")))

total = sum(expenses)

print("You spent $", total, sep = '')

#range

total = 0
expenses = []

for i in range(7):
    expenses.append(float(input("How much did you spent?\n")))

total = sum(expenses)

print("You spent $", total, sep = "")


total = 0
expenses = []
num_expenses = int(input("Enter # of expenses:\n"))

for i in range(num_expenses):
    expenses.append(float(input("How much did you spent?\n")))

total = sum(expenses)
print("You spent $", total, sep = "")
"""

expenses = [10.50, 8.50, 5.30, 15.05, 20.00, 5.00, 3.00]

user_new_spent = expenses.append(float(input("How much did you spent?\n")))

total = sum(expenses)

print("You spent $%.2f"% round(total, 2))