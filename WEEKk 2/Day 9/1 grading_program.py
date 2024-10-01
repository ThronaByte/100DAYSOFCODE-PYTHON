student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades= {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    student_grades[key] = student_scores[key]
    
for grad in student_grades:
    grade = student_grades[grad]
    if grade > 91 :
        student_grades[grad] = "Outstanding"
    elif grade <= 81:
        student_grades[grad] = "Exceeds Expectation"
    elif grade <= 71:
        student_grades[grad] = "Acceptable"

# 🚨 Don't change the code below 👇
print(student_grades)