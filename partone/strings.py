# Basics

mystring = 'vlado'
'hello'
"hello"

# indexing
print(mystring[0])    # a
print(mystring[-1])   # o

print(mystring[2:])   # ado
print(mystring[2:4])  # ad
print(mystring[:4])   # vlad

upperCase = mystring.upper()
lowercase = mystring.lower()
splited = mystring.split('a')
print(upperCase)
print(lowercase)
print(splited)

# print formating
x = 'Insert another string here: {x} and one here {y}'.format(x='dog', y='cat')
print(x)
