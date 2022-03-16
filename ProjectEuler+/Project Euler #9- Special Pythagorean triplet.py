def controlPythagoreanTriplet(N):
    m = -1
    for a in range(3, N // 3 + 1):
        b = (N ** 2 - 2 * a * N) // (2 * N - 2 * a)
        c = N - (a + b)
        if c ** 2 == a ** 2 + b ** 2:
            if a * b * c > m:
                m = a * b * c
    print(m)


t = int(input().strip())
for i in range(t):
    n = int(input().strip())

    controlPythagoreanTriplet(n)

#############################################################################
# import math
#
# for _ in range(int(input())):
#     n = int(input())
#     if n % 2 == 1:
#         print(-1)
#     else:
#         maxprod = -1
#         s = int(math.sqrt(n))  # math.isqrt(n) is not available here. Also you can start from 3, this improvement is minor.
#         for a in range(s, n // 3 + 1):  # a is the smallest of the three and is larger than int(sqrt(n))
#             # proof: if c-b>1, this is clear. If c-b=1, then int(sqrt(n))=a.
#             if a ** 2 % (n - a) == 0:  # b+c=n-a should divides c^2-b^2=a^2. Much more effecient in reducing calculation.
#                 k = a ** 2 // (n - a)
#                 if (n - a - k) % 2 == 0:  # c-b and c+b are of same parity
#                     b = (n - a - k) // 2  # b is half the difference between those two number
#                     t = a * b * (n - b - a)
#                     if t > maxprod:
#                         maxprod = t
#         print(maxprod)
