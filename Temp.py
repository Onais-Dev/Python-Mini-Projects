
# User can Convert the Tempertaure between Celcius and fahrenheit
# Aksing for input about whcih operatio they want to perfrom
# And then Input the temperature
# program will convert it

# Input cel from the user
temp = int(input("Enter Temp: "))
print("You want to convert this to Celcius or Farhanheit? ")

opr = input()
if (opr == "Celcius"):
    print((temp*1.8) + 32)

else: print((temp-32)*5/9)