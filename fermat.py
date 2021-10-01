from random import *

def fermat_test(n, k):
    if n == 2:
        return "El numero {} es primo".format(n)

    if n % 2 == 0:
        return "El numero {} es compuesto".format(n) 

    for i in range(k):
        a = randint(1, n-1)

        if pow(a, n-1) % n != 1:
            return "El numero {} es compuesto".format(n) 

    
    return "El numero {} es primo".format(n)


print(fermat_test(8, 5))
print(fermat_test(12, 5))
print(fermat_test(1317, 5))
print(fermat_test(2709, 5))
print(fermat_test(3257, 5))
print(fermat_test(3911, 5))
print(fermat_test(4279, 5))
print(fermat_test(5497, 5))
print(fermat_test(6311, 5))
print(fermat_test(7223, 5))
print(fermat_test(8431, 5))
print(fermat_test(9203, 5))