print(1 > 0)
print('hi' == 'hai')


number = 1000


if(number > 1):
    print('1')
    if(number > 10 and number < 100):
        print('2')
        if(number):
            print('stignax')
    elif(number < 10):
        print('po malko')
    else:
        print('svurshix')


seq = [1, 22, 3, 4, 5, 6, 7, 8]
objects = {'k1': 'd1', 'k2': 'd2'}
print(seq)

for item in seq:
    print(item)
for obj in objects:
    print(objects[obj])


ccc = list(range(0, 20))
print(ccc)


i = 0
while(i < 10):
    i += 1
    j = 0
    while(j < 10):
        print('{i}{j}'.format(i=i, j=j))
        j += 1


def faktoriel(number):
    if(number < 2):
        return number
    else:
        return number * faktoriel(number-1)


# result = faktoriel(25)
# print(result)
