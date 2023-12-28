import sympy

addition = 0
odds = 1
primes = 0
ratio = 1
number = 1

while ratio >= 0.1:
  addition += 2
  for i in range(4):
    number += addition
    odds += 1
    if sympy.isprime(number):
      primes += 1
  ratio = primes / odds

print('side lenght: ',addition+1)
print('ratio: ', ratio)