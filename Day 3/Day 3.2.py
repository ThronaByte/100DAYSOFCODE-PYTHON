# Body Mass Index (BMI) Excercise
weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in m: "))

bmi = round(weight / height ** 2)
print(f"Your bmi is {bmi}")
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese")
else:
    print("You are cliniccally obese")