import random


def prime_test(N, k):
    # This is main function, that is connected to the Test button. You don't need to touch it.
    return fermat(N, k), miller_rabin(N, k)


def mod_exp(x, y, N):
    # Time Complexity here is O(N^3)
    # because we keep diving y by 2 until we get to zero
    # so we keep bit shifting n time until Y is zero
    # so there are n function calls in each function call
    # we have a multiply which is N^2
    # so N^2 * N is N^3 and the time complexity is O(N^3)
    if y == 0:
        return 1
    z = mod_exp(x, y // 2, N)
    if y % 2 == 0:
        return (z ** 2) % N
    else:
        return x * ((z ** 2) % N)

def fprobability(k):
    # You will need to implement this function and change the return value.
    # my comment "will probably just return 1 - 1/2^k
    # Time Complexity here is constant
    return 1 - (1/(2**k))


def mprobability(k):
    # You will need to implement this function and change the return value.
    # should just end up being 1 - (1/(4^k))
    # Time Complexity Here is constant
    return 1 - (1/(4**k))


def fermat(N, k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    # The Time Complexity of fermat is going to be O(N^3)
    # because the mod_exp function time complexity is N^3
    # and we loop through it k amount of times so we get k * N^3
    # we can drop the k so we end up getting O(N^3)
    for i in range(0,k):
        a = random.randint(2, N - 1)
        if mod_exp(a, N - 1, N) != 1:
            return 'composite'
    return 'prime'


def miller_rabin(N, k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    # Time Complexity is O(N^4) because we are calling the mod_exp function
    # which is n^3 n amount of times which is (n^3)*(n) which is n^4
    # we will loop through K amount of times but we can drop the K because
    # it is constant
    numlist = []
    for i in range(k):
        a = random.randint(2, N - 1)
        n = N - 1
        numlist = []
        while (n % 2) == 0:
            if(mod_exp(a,n,N)) != 1:
             numlist.append(mod_exp(a, n,N))
            n = n // 2
        if numlist:
         if numlist[0] != N - 1:
          return 'composite'
    return 'prime'
