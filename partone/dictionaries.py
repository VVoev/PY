my_items = {
    'key1': 'value 1',
    'key2': 'value 2',
    'key3': {'123': [1, 2, 'grabMe']}
}

print(my_items['key3']['123'][2])

food = {
    'lunch': 'pizza',
    'bfast': 'eggs',
}

food['lunch'] = 'burger'
food['dinner'] = 'pasta'


print(food)
