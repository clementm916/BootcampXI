


def genPrimes(n):
    """Function receives an integer n and returns all prime numbers betweem integer n and 0"""
    primes = []
    numbers = [x for x in range(2,n)]
    for i in numbers:
        if isPrime(i):
            primes.append(i)


    return primes









def isPrime(n):
    """Function checks whether a number is prime"""
    for i in range(2,n):
        if n%(i) ==0:
            return False
    else:
        return True



print genPrimes(10)

print isPrime(4)