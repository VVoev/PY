

def arrayCheck(nums):
    for i in range(len(nums)-2):
        if(nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3):
            return True
    return False


print(arrayCheck([1, 1, 2, 3, 1]))
print(arrayCheck([1, 1, 2, 4, 1]))
print(arrayCheck([1, 1, 2, 1, 2, 3]))


def stringBits(randomStr):
    result = ""

    for i in range(len(randomStr)):
        if i % 2 == 0:
            result += randomStr[i]
    return result


print(stringBits('Hello'))
print(stringBits('Hi'))
print(stringBits('Heeololeo'))


def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return a[-(len(b)):] == b or a == b[-len(a):]


print(end_other('Hiabc', 'abc'))
print(end_other('Abc', 'HiaBc'))
print(end_other('abc', 'abXabc'))
print(end_other('xaxa', 'abXabc'))


def doubleChar(mystring):
    result = ''
    for char in mystring:
        result += char*2
    return result


print(doubleChar('The'))
print(doubleChar('AAbb'))
print(doubleChar('Pranil'))


def check_if_teen(number):
    if number >= 13 and number <= 19:
        if(number == 15 or number == 16):
            return number
        else:
            return 0
    return number


def no_teen_sum(a, b, c):
    a = check_if_teen(a)
    b = check_if_teen(b)
    c = check_if_teen(c)
    return a+b+c


print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))
print(no_teen_sum(2, 15, 14))


def count_evens(nums):
    total = 0
    for element in nums:
        if element % 2 == 0:
            total += 1
    return total


print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([1, 3, 5]))
