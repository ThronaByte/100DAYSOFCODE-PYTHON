# " Welcome to the Tip Calculator!"
print("\nWelcome to the Tip Calculator!")

bill = float(input("What is the total bill? N"))
tip = float(input("How much Tip are you giving? N"))
person = int(input("How many people are splitting the bill? "))

tip_in_percent = tip / 100
print(f"Tip in percent = {tip_in_percent}%")

calculating_bill = bill * tip_in_percent
print("calculating the tip in percent & bill =",calculating_bill)

adding_bill = bill + calculating_bill
print(f"adding {bill} the bill + the calculated bill {calculating_bill}")

dividing_bill = adding_bill / person
print(f"Dividing {adding_bill} the bill by {person} number of person")
each_person_bill = round(dividing_bill)
print("rounded the bill to the nearest whole number")
print(f"Each person should pay: N{each_person_bill}")