# We'll use isprime function from sympy lib
from sympy import isprime

# amount to add to actual number, for finding next diagonal number
addition = 0
# amount of odds, starting from 1 (number 1 in the center)
odds = 1
# amount of primes (number 1 does not count as prime)
primes = 0
# ratio (primes/odds)
ratio = 1
# current number
number = 1

# while ratio is not less than 10%
while ratio >= 0.1:
  # we must add this to the current number, to find the next diagonal number 
  addition += 2
  # we must find 4 diagonal numbers for each new square
  for i in range(4):
    # to find the new diagonal number:
    number += addition
    # then we have a new odd 
    odds += 1
    # and if that odd is a prime
    if isprime(number):
      # we add 1 to primes account
      primes += 1
  # when the square is complete, find the ratio
  ratio = primes / odds

# print the side lenght, this is the founded answer
print('side lenght: ',addition+1)
# print the ratio to check it is less than 10%
print('ratio: ', ratio)
