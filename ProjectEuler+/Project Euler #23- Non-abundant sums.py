import math


def bolen_toplami(x):
    toplam = 1
    n = 2
    while n < math.ceil(math.sqrt(x)):
        if x % n == 0:
            toplam += n
            toplam += x // n
        n += 1

        if n * n == x:
            toplam += n

    return toplam


def kontrolEbundant(x):
    return True if bolen_toplami(x) > x else False


abundants = list()
toplam = 0
sum_of_abundants = list()

for i in range(1, 28124):
    if kontrolEbundant(i):
        abundants.append(i)

sum_of_abundants = [0] * 28124

for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        if abundants[i] + abundants[j] <= 28123:
            sum_of_abundants[abundants[i] + abundants[j]] = abundants[i] + abundants[j]

for _ in range(int(input())):
    num = int(input())

    if num > 28123:
        print("YES")
    else:
        if num in sum_of_abundants:
            print("YES")
        else:
            print("NO")

#############################################################################
# import math
#
#
# def sumi(n):
#     s = 0
#     for i in range(2, int(math.sqrt(n) + 1)):
#         if n % i == 0:
#             s += i
#             y = n / i
#             if i != y:
#                 s += y
#     return s + 1
#
#
# l = [0, 0]
# for i in range(2, 28123):
#     if i < sumi(i):
#         l.append(1)
#     else:
#         l.append(0)
# for _ in range(int(input())):
#     m = int(input())
#     if m > 28122:
#         print("YES")
#     else:
#         for i in range(1, m // 2 + 1):
#             if l[m - i] and l[i]:
#                 print("YES")
#                 break
#         else:
#             print("NO")


#############################################################################

# def abundant(n):
#     n1 = int(n ** (1 / 2)) + 1
#     tot = 0
#     for i in range(2, n1):
#
#         if (n % i == 0):
#
#             if (i != n / i):
#                 tot += i + (n / i)
#             else:
#                 tot += i
#
#     if (n < tot + 1):
#         return (True)
#     else:
#         return (False)
#
#
# num = int(input())
# for i in range(num):
#     n = int(input())
#     mid = int(n / 2)
#     flag = 0
#     for i in range(2, mid + 1):
#
#         if (abundant(i) and abundant(n - i)):
#             print("YES")
#             flag = 1
#             break
#     if (flag == 0):
#         print("NO")
