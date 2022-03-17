def nprime():
    limit = 1000001
    sieve = [True] * limit

    for i in range(3, int(pow(limit, 0.5)) + 1, 2):
        if sieve[i]:
            for j in range(i ** 2, limit, i):
                sieve[j] = False

    primes = [2] + [i for i in range(3, limit, 2) if sieve[i]]
    return primes


def sumprimes(primes):
    sumVal = 0
    out = []
    j = 0
    for i in range(1000001):
        if primes[j] <= i:
            sumVal += primes[j]

            if j + 1 < len(primes):
                j += 1
        out.append(sumVal)
    return out


primes = nprime()
sums = sumprimes(primes)

for i in range(int(input())):
    num = int(input())
    print(sums[num])

#############################################################################
# import sys
#
# limit = 1000000
# suml = [0] * limit
# a = [True] * limit
# a[0] = a[1] = False
# for i, isprime in enumerate(a):
#     if isprime:
#         suml[i] = suml[i - 1] + i
#         for n in range(i * i, limit, i):
#             a[n] = False
#     else:
#         suml[i] = suml[i - 1]
#
# t = int(input().strip())
# for a0 in range(t):
#     n = int(input().strip())
#     print(suml[n])
