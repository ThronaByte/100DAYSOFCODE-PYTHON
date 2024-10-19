names = ["Daniel", "Samson", "Victor", "Chidubem"]
import random
result = {name:random.randint(1,100) for name in names}
print(result)
pass_stud = {student:score for (student,score) in result.items() if score >= 60}
print(pass_stud)