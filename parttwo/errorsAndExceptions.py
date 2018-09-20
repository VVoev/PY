try:
    f = open('sample.txt', 'r')
    res = f.read()
    print(res)
except IOError:
    print('Error:File not found')
else:
    print('Success')
    f.close()
