# Using Python 2.7.7 :: Anaconda 2.0.1 (64-bit)

'''
Problem 1 - Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def main():
    # Option 1 - straightforward and understandable
    total = 0
    for i in xrange(1, 1001):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    print 'Option 1:', total

    # Option 2 - For a bit more "pythonic" flair using generators
    nums = (i for i in xrange(1, 1001) if i % 3 == 0 or i % 5 == 0)
    ans = reduce(lambda x,y: x+y, nums)
    print 'Option 2:', ans

if __name__ == '__main__':
    main()
