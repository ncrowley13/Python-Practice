## Problem 1.1: This function takes two integers, m & n. Return True if n is a multiple of m. Return False if not.
def is_multiple(n,m):
    if m%n == 0:
        return True
    elif m%n != 0:
        return False
    else:
        print ("Error.")

##Problem 1.2: This function determines whether a number, k, is even or odd without using multiplication, division, or modulo functions. (I used the exponent operator, **)
def is_even(k):
    if (-1)**k == 1:
        return True
    elif (-1)**k == -1:
        return False
    else:
        print ("Error.")
        
##Problem 1.3:takes a sequence of one or more numbers, and returns the smallest and largest numbers, in the form of a tuple of length two.
def minmax(data):
    biggest = smallest = data[0]
    for value in data:
        if value >= biggest:
            biggest = value
        elif value <= smallest:
            smallest = value
        else:
            pass
    print (biggest, smallest)

##Problem 1.4: Function takes a positive integer, n, and returns the sum of the squares for all positive integers less than n.
def sum_of_squares(n):
    l = 0
    for i in range(n):
        l += i**2
    print (l)

##Problem 1.5
sum(i**2 for i in range(n))

##Problem 1.6: Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n.
def sum_odd_squares(x):
    l = 0
    for i in range (x):
        if i%2 == 1:
            l += i**2
        else:
            pass
    print (l)

##Problem 1.9:
for i in range(50, 90, 10):

    print(i)


##Problem 1.11
S = [2**x for x in range(10)]

print (S)

##Problem 1.15
def unique(data):
    unique_values = set(data)
    if len(data) == len(unique_values):
        print ("This is a unique set of numbers")
    elif len(data) != len(unique_values):
        print ("This is NOT a unique set.")
    else:
        print ("Oops!")

##Problem 1.18
q = [x*(x + 1) for x in range(10)]
print(q)

##Fibonacci Sequence generator function, printed
def fibonacci():
    a = 0
    b = 1
    while True:
         yield a
         future = a + b
         a = b
         b = future

fib = fibonacci()
for i in range(1,150):
    print (next(fib))


##Problem 1.24
def vowel_count(string):
    x = 0
    for value in string:
        if value in "aeiou":
            x += 1
        elif value not in "aeiou":
            pass
    print ("The number of values in this string is ", x)

##Problem 1.25
import string

def punc_removal(x):
    punc = set(string.punctuation)
    for i in x:
        if i in punc:
            x = x.replace(i,"")
        elif i not in punc:
            pass
    print(x)

##Problem 1.26
##Write a short program that takes as input three integers, a, b, and c, from 
##the console and determines if they can be used in a correct arithmetic 
##formula (in the given order), like “a+b = c,” “a = b-c,” or “a * b = c.”

def integer_relations(a, b, c):
    if a + b == c:
        print (a, "+", b, "=", c)
    elif a == (b-c):
        print (a, "=", b, "-", c)
    elif (a*b) == c:
        print (a, "*", b, "=", c)
    else:
        print ("Your three integers are not related")

integer_relations(3,5,11)


