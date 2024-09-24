# life in day, week and month (Target)

age = int(input("Enter your age: "))
days = 365
weeks = 52
months = 12

age_target = int(input("Enter your target year: "))

years_remaining = age_target - age
days_remaining = years_remaining * days
weeks_remaining = years_remaining * weeks
months_remaining = years_remaining * months

spend_your_days_wisely = f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months left"
print(spend_your_days_wisely)