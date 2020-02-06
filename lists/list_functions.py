numbers=[2,3,4,5,6]
numbers.append(20)
print(numbers)

numbers.insert(2,10)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.index(3))
print(3 in numbers)
print(numbers.count(6))

numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers_2=numbers.copy()
print(numbers_2)