import math
n = int(input())
is_prime = True


if n < 2:
    print('Not prime!')
else:
    end_i = int(math.sqrt(n))
    for num in range(2, end_i + 1):
        if n / num == n//num:
            is_prime = False

    if is_prime:
        print('Prime!')
    else:
        print('Not prime!')

