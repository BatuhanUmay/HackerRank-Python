# import itertools
#
# N = int(input())
#
#
# def compute():
#     ans = max(([a, b] for a in range(-N + 1, N) for b in range(2, N)), key=count_consecutive_primes)
#     return str(ans[0]) + " " + str(ans[1])
#
#
# def count_consecutive_primes(ab):
#     a, b = ab
#
#     for i in itertools.count():
#         n = i * i + i * a + b
#         if not is_prime(n):
#             return i
#
#
# def is_prime(num):
#     if num <= 1:
#         return False
#     elif num == 2:
#         return True
#     elif num % 2 == 0:
#         return False
#     else:
#         for i in range(3, int(pow(num, 0.5) + 1), 2):
#             if num % i == 0:
#                 return False
#         return True
#
#
# def list_primality(n):
#     result = [True] * (n + 1)
#     result[0] = result[1] = False
#     for i in range(int(pow(n, 0.5) + 1)):
#         if result[i]:
#             for j in range(i * i, len(result), i):
#                 result[j] = False
#     return result
#
#
# isPrimeCache = list_primality(N)
#
#
# def isPrime(n):
#     if n < 0:
#         return False
#     elif n < len(isPrimeCache):
#         return isPrimeCache[n]
#     else:
#         return is_prime(n)
#
#
# print(compute())

##############################################################################

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(pow(num, 0.5) + 1), 2):
            if num % i == 0:
                return False
        return True


N = int(input())
a_max = 0
b_max = 0
count = 0

for a in range(-N + 1, N):
    for b in range(2, N):
        n = 0
        while is_prime(n ** 2 + a * n + b):
            n += 1

        if n > count:
            a_max, b_max = a, b
            count = n
print(a_max, b_max)
