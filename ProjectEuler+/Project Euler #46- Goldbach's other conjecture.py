def SieveOfEratosthenes(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    for i in range(2, n + 1):
        if prime[i]:
            for j in range(i * 2, n + 1, i):
                prime[j] = False
    return prime


primes = SieveOfEratosthenes(500000)
squares = [2 * i * i for i in range(500)]

t = int(input())

for _ in range(t):
    num = int(input())
    ways = 0

    for x in squares:

        if primes[num - x]:
            ways += 1

    print(ways)

####################################################################

# # FUNCTION THAT RETURNS PRIMES UP TO N
# # Note: in a set not a list. for quick access
# # cause list must be iterated. So for example:
# # primes up to 500.000 are about 40.000. But in
# # a set we can search through 40.000 numbers in
# # O(1)
# def SieveOfEratosthenes(n):
#     result = set()
#
#     prime = [True for i in range(n + 1)]
#     p = 2
#     # search up to sqrt(n)
#     while (p * p <= n):
#
#         if (prime[p] == True):
#
#             # if prime found, make multiples->false
#             for i in range(p * 2, n + 1, p):
#                 prime[i] = False
#         p += 1
#
#     # once done store primes in Set
#     for p in range(2, n):
#         if prime[p]:
#             result.add(p)
#
#     return result
#
#
# # primes and squares for worst case
# primes = SieveOfEratosthenes(500000)  # set for O(1) access
# squares = [2 * x * x for x in range(500)]
#
# t = int(input())
#
# for i in range(t):
#
#     # take number
#     num = int(input())
#
#     # ways it can be written as
#     ways = 0
#     for a in squares:
#         # dont search too high on squares
#         # cause this costs. its a 500 elem' list
#         if a > num:
#             break
#
#         # solve equation num = prime + 2*square
#         # ==> prime = num-2*square
#         # so if there is a prime we increase counter
#         if (num - a) in primes:
#             ways += 1
#
#     # print total ways
#     print(ways)
