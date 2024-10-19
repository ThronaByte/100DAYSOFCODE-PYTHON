with open('file1.txt') as file1:
    read_1= file1.readlines()

with open('file2.txt') as file2:
    read_2= file2.readlines()

result = [int(num) for num in read_1 if num in read_2]
print(result)