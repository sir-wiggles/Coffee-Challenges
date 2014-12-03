
numbers = range(1, 10001)
numbers = ' '.join(map(str, numbers))
numbers = numbers.replace('0', ' ')
numbers = numbers.split(' ')
numbers = filter(lambda x: x, numbers)
sum = 0
for number in numbers:
    try:
        sum += int(number)
    except:
        pass
assert 37359001 == sum
print sum 
