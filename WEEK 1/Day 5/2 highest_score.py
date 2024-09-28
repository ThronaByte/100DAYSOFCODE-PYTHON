highest_score = input("Input a list of student score: ").split()
for n in range(0, len(highest_score)):
    highest_score[n] = int(highest_score[n])
print(highest_score)

high = 0
for x in highest_score:
    print(x)
    if high < x:
        high = x
print(f"The highest score is: {high}")