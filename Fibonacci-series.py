#The Fibonacci sequence is a type series where each number is the sum of the two that precede it. 
# It starts from 0 and 1 usually. The Fibonacci sequence is given by 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, and so on.
# The numbers in the Fibonacci sequence are also called Fibonacci numbers.#

n = int(input("Enter Number till which you want to print Fibonacci sequence : "))
sum = 0
a = 0
b = 1
alist = [a,b]

while sum<=n:
    sum = a+b
    alist.append(sum)
    a=b
    b=sum
    
print(alist)
