#writing a program to find the largest number in a list
numbers=[0,1,2,3,4,5]
max=numbers[0]
for number in numbers:
    if number>max:
        max=number
print(max)