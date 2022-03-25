# # primes is a list of primes
# # is_prime is a list of booleans where is_prime[i] is True if i is prime
#
# def fast_sum_of_proper_divisors(n, primes, is_prime):
#     """
#     input n, a list of primes, and a list of booleans
#     returns the sum of the proper divisors
#     """
#     if is_prime[n]:
#         return 1
#     n_copy = n
#     product = 1
#     for p in primes:
#         if is_prime[n]:
#             product *= (n ** (1 + 1) - 1) // (n - 1)
#             break
#         if p > n:
#             break
#         i = 0
#         while n % p == 0:
#             n //= p
#             i += 1
#         if i != 0:
#             product *= (p ** (i + 1) - 1) // (p - 1)
#     return product - n_copy
#

##############################################################

c = [220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368,
     10744, 10856, 12285, 14595, 17296, 18416, 63020, 66928,
     66992, 67095, 69615, 71145, 76084, 79750, 87633, 88730,
     100485, 122265, 122368, 123152, 124155, 139815, 141664,
     142310]
t = int(input())
for i in range(t):
    a = int(input())
    res = 0
    for j in c:
        if j <= a:
            res += j
    print(res)
