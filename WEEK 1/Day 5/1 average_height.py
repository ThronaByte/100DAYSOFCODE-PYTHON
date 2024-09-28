student_height = input("Input a list of student heights: ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)

sum_of_list = 0
lenght = 0
for student in student_height:
    lenght += 1 #lenght of list
    sum_of_list += student # sum of the list 
    # divide the (sum_of_list) by the (lenght )
result = round(sum_of_list / lenght)
print(f"The average height rounded to the nearest whole number = {result}")
# 127 123 125 321 456
