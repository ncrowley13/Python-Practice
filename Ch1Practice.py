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

