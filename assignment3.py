# BMI Calculator

weight = int(input("Enter your weight : "))
height = float(input("Enter your height : "))
bmi = weight / (height * height)

if bmi <18.5:
    print("Your BMI is : ", bmi)
    print("You are underweight")
elif bmi >= 18.5 and bmi <= 22.9:
    print("Your BMI is : ", bmi)
    print("You weight is normal")
elif bmi >= 23 and bmi <= 24.9:
    print("Your BMI is : ", bmi)
    print("You are overweight")
elif bmi >=25 and bmi <= 29.9:
    print("Your BMI is : ", bmi)
    print("You are pre-obese")
elif bmi >= 30 and bmi <= 34.9:
    print("Your BMI is : ", bmi)
    print("You are obese class 1")
elif bmi >= 35 and bmi <=39.9:
    print("Your BMI is : ", bmi)
    print("You are obese class 2")
elif bmi >=40:
    print("Your BMI is : ", bmi)
    print("You are obese class 3")
else:
    print("Invalid entry")
