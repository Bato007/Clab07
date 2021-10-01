import random

# Primer inciso
def gcd(a, b):
  if (a == 0): return b
  else: return gcd(b % a, a)

# Segundo inciso
def gcdExtended(a, b):
  if (a == 0):
    return b, 0, 1
  
  d, x1, y1 = gcdExtended(b % a, a)
  x = y1 - (b//a)*x1
  y = x1
  return d, x, y

# Tercer inciso
def inverseMod(a, n):
  d, x, y = gcdExtended(a, n)
  if (d == 1):
    return x % n
  return 'No tiene inverso'

# Quinto inciso
# n = 10, k = 5
def primeGenerator(n, k):
  primes = []
  flag = 0
  lowerLimit = 10**(n-1)
  upperLimit = 10**(n)-1

  while len(primes) < k:
    numb = random.randint(lowerLimit, upperLimit)
    if numb == 2:
      primes.append(numb)
    if numb % 2 == 0:
      pass
    for i in range(k):
      a = random.randint(1, numb-1)
      if pow(a, numb-1) % numb != 1:
        pass
      else:
        flag += 1        

    if flag == k:
      primes.append(numb)
    flag = 0
  
  return primes

def main():
  lab1 = [
    (1036, 240),
    (22896, 192),
    (689161, 378851)
  ]

  lab2 = [
    (1036, 240),
    (8753, 3354),
    (2021, 43)
  ]

  lab3 = [
    (47, 2020),
    (31, 1234),
    (65, 17316)
  ]

  print('=====INCISO 1=====')
  for i in lab1:
    print('gcd(a = %i, b = %i) = %i' %(*i, gcd(*i)))
  
  print('=====INCISO 2=====')
  for i in lab2:
    print('gcd(a = %i, b = %i) = %i,\n\tx = %i, y = %i' %(*i, *gcdExtended(*i)))

  print('=====INCISO 3=====')
  for i in lab3:
    print('inverseMod(a = %i, n = %i) = %s' %(*i, str(inverseMod(*i))))

  print('=====INCISO 5=====')
  print(primeGenerator(7, 5))

if (__name__ == '__main__'):
  main()
