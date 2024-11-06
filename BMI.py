# Take Input about the user's height in Meter if in Centimeter divide it with 100 so it can be in meters
# Inout weight in kg
# tell the user thier BMI category:
    # Underweight: BMI < 18.5
    # Normal weight: 18.5 ≤ BMI < 24.9
    # Overweight: 25 ≤ BMI < 29.9
    # Obese: BMI ≥ 30

print("Welcome to BMI Calculator!/n" "Enter You detail Below; ")

weight = int(input("Enter Your Weight in KG: "))
height = float(input("Enter you height:"))

bmi = weight / height **2

print(int(bmi))



print("Your BMI Category: ")
if (bmi<18.5):
    print("underWeight")

if (18.5 <=bmi < 24.9):
    print("Normal Weight")

if (24.9 <=bmi <29.9 ):
    print("Over Weight")

if (bmi>29.9):
    print("Obese")