prime_occurences = [0, 2, 3]


def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


t = int(input().strip())
for a0 in range(t):
    position = int(input().strip())
    try:
        if prime_occurences[position]:
            print(prime_occurences[position])
    except:
        ptr = len(prime_occurences)
        i = ptr - 1
        num = prime_occurences[i] + 1
        while ptr <= position:
            if isPrime(num):
                prime_occurences.append(num)
                ptr += 1
            num += 1
        print(prime_occurences[position])

#############################################################################################

# Use naive Sieve of Eratosthenes to create list of first (approx) 10000 primes
# p = {i for i in range(2, 105000)}
# for i in range(2, 325):
#     p = p.difference({i for i in range(i * 2, 200000, i)})
# p = list(sorted(p))
#
# for _ in range(int(input())):
#     n = int(input())
#     print(p[n - 1])
#############################################################################################

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
# def seive_of_e(n):
#     D = {}
#     q = 2
#     count = 0
#
#     while count < n:
#         if q not in D:
#             yield q
#             count += 1
#             D[q * q] = [q]
#         else:
#             for p in D[q]:
#                 D.setdefault(p + q, []).append(p)
#             del D[q]
#         q += 1
#
#
# t = int(input().strip())
# lin = []
# for a0 in range(t):
#     n = int(input().strip())
#     lin.append(n)
#
# primes = list(seive_of_e(max(lin)))
# for i in lin:
#     print(primes[i - 1])
