# Project-Euler-58---Python
Solution for Project Euler problem 58 in Python 
___
## Description
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7  is formed.
  
**37**&nbsp;&nbsp;36&nbsp;&nbsp;35&nbsp;&nbsp;34&nbsp;&nbsp;33&nbsp;&nbsp;32&nbsp;&nbsp;**31**  
38&nbsp;&nbsp;**17**&nbsp;&nbsp;16&nbsp;&nbsp;15&nbsp;&nbsp;14&nbsp;&nbsp;**13**&nbsp;&nbsp;30  
39&nbsp;&nbsp;18&nbsp;&nbsp;**05**&nbsp;&nbsp;04&nbsp;&nbsp;**03**&nbsp;&nbsp;12&nbsp;&nbsp;29  
40&nbsp;&nbsp;19&nbsp;&nbsp;06&nbsp;&nbsp;01&nbsp;&nbsp;02&nbsp;&nbsp;11&nbsp;&nbsp;28  
41&nbsp;&nbsp;20&nbsp;&nbsp;**07**&nbsp;&nbsp;08&nbsp;&nbsp;09&nbsp;&nbsp;10&nbsp;&nbsp;27  
42&nbsp;&nbsp;21&nbsp;&nbsp;22&nbsp;&nbsp;23&nbsp;&nbsp;24&nbsp;&nbsp;25&nbsp;&nbsp;26  
**43**&nbsp;&nbsp;44&nbsp;&nbsp;45&nbsp;&nbsp;46&nbsp;&nbsp;47&nbsp;&nbsp;48&nbsp;&nbsp;49  
  
It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ~ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
___
## Content
Readme.me    details about project  

start.py     code to solve the problem proposed in the description.  
___
## Explained solution
Starting with number 1, for each new square arond it, we have 4 new odd numbers on each vertex of this square.  
Again, starting with number 1, we can find the next vertex adding 2, thus, therefore the 4 vertices will be 3,5,7,9.  
We check for each vertex if it's prime and keep track of the amount of primes.  
Once we complete the square, the next square will have a side length equal to the side length of the previous square plus 2,  
that is the ammount of numbers between one vertex and the next.  
so to find the next vertex, instead of adding 2, we will have to add 4 (2+2), 
again, 4 will be the amount of numbers between vertices in this new square.  
For the next square we will be adding 6 (4+2), and so on.  
We repeat all this process until the ratio prime/odds is below 10% (or 0.1).  




