n = int(input('Enter even number: '))

while not n % 2 == 0:
    print('The number is not even!')
    n = int(input('Enter even number: '))
print('Even number entered: ' + str(n))
