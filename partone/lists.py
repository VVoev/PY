# lists

mylist = [1, 2, 3]
mixedList = ['ivan', 1, True, [1, 2, 3]]
print(mixedList)

print(mylist[0])
print(mylist[1:])

mylist[0] = 'Petko'
print(mylist)

mylist.append('vlado')
print(mylist)

item = mylist.pop(2)
print(item)

numbers = [2, 3, 4, 1, 20, 10]
numbers.sort()
print(numbers)

anotherMix = [1, 2, ['x', 'y', 'z']]
print(anotherMix[2][1])


# LIST COMPREHENSION
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
first_col = [row[0] for row in matrix]

print(first_col)
