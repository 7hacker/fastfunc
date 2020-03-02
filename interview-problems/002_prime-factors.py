'''
https://www.fastfunc.com/sieve-of-eratosthenes/
'''

import argparse

# initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("--naive", action="store_true")
parser.add_argument("--eratosthenes", action="store_true")
parser.add_argument("-n")
args = parser.parse_args()

class SieveOfEratosthenes:
    def __init__(self, howmany):
        self.n = howmany
        self.primeArray = [True] * (howmany+1)
        self.primeList = []

        # 0 and 1 are not prime numbers
        self.primeArray[0] = False
        self.primeArray[1] = False
        # for each number in the bit array, their multiples can be set to False
        for i in range(2, howmany+1):
            for j in range(i*2, howmany+1, i):
                self.primeArray[j] = False
        # now you have all prime numbers in the bit array
        for i in range(self.n):
            if self.primeArray[i]:
                self.primeList.append(i)

    def getPrimeList(self):
        return self.primeList


def naive_primeCheck(k):
    # check if k is prime using basic math
    if k == 1 or k == 0:
        return False
    for i in range(2, k):
        if k % i == 0:
            return False
    return True


def naive_primeFactorize(n):
    res = []
    while n != 1:
        for i in range(1, n+1):
            if naive_primeCheck(i) and n % i == 0:
                n = int(n/i)
                res.append(i)
    return res


def SieveOfEratosthenes_primeFactorize(n):
    res = []
    s = SieveOfEratosthenes(n)
    primes = s.getPrimeList()
    while n != 1:
        for i in range(1, n+1):
            if i in primes and n % i == 0:
                n = int(n/i)
                res.append(i)
    return res


def main():
    if args.naive:
        print(naive_primeFactorize(int(args.n)))
    elif args.eratosthenes:
        print(SieveOfEratosthenes_primeFactorize(int(args.n)))


if __name__ == "__main__":
    main()
