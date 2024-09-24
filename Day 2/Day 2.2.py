# BMI Exercise
weight = float(input("Type in your weight (kg): "))
height = float(input("Type in your height (m2): "))
# using diffrent method to round OR remove decimal point
bmi = int(weight // height **2)
bmi2 = int(weight / height **2)
bmi3 = round(weight / height **2)
# printing 
print("Your BMI is ", bmi)
print("Your BMI is ", bmi2)
print("Your BMI is ", bmi3)