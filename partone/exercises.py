s = 'django'

print(s[0])
print(s[-1])
print(s[:4])
print(s[4:])

nqkuvlist = [3, 7, [1, 4, 'Hello']]
print(nqkuvlist[2][2])

d1 = {'k1': 'hello'}
d2 = {'k2': {'k3': 'hello'}}
d3 = {'k1': [{'k2': ['deep', ['hello']]}]}

print('---------')

print(d1['k1'])
print(d2['k2']['k3'])
print(d3['k1'][0]['k2'][1][0])


numbers = [1, 1, 1, 1, 2, 3, 2, 2, 2, 3, 3, 4,  5, 5, 6, 6, 7]
unique = set(numbers)
print(unique)

name = 'Petko'
years = 22


print('Hello my name is {name} and im {years}'.format(name=name, years=years))
