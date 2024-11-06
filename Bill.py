# Goal: Calculate how much each person should pay, including a tip, when sharing a bill.

# Steps:
# Ask the user for the total bill amount.
# Ask for the tip percentage they’d like to give (e.g., 10%, 15%, 20%).
# Ask how many people are sharing the bill.
# Calculate:
# The tip amount by multiplying the bill by the tip percentage.
# The total bill including the tip.
# The amount each person needs to pay by dividing the total bill by the number of people.

print("Hello Sir! ")
bill = int(input("How much is the Bill? "))

tip = input("Would you like to give some Tip also? ")

if (tip == "Yes"):
    tip_amount = int(input("How Much: "))
    total = bill + (tip_amount / 100) * bill

elif (tip == "No"):
    (print("Ok No Problem!"))
    total = bill

print("Ok So Your Total is " , total, "If you want to Split it between 3 person It would be: ", int(total/3) ,"each" )


