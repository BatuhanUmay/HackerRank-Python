# def fibo(num):
#     fiboList = []
#     n1 = 1
#     n2 = 1
#     fiboList.append(n1)
#     fiboList.append(n2)
#
#     for i in range(2, num):
#         n3 = n1 + n2
#
#         if n3 > num:
#             break
#
#         n1, n2 = n2, n3
#         fiboList.append(n3)
#     return fiboList
#
#
# def checkEvenFibo(num):
#     allFibos = fibo(num)
#     evenFibos = []
#
#     for i in allFibos:
#         if i % 2 == 0:
#             evenFibos.append(i)
#
#     return sum(evenFibos)
#
#
# t = int(input().strip())
# for i in range(t):
#     n = int(input().strip())
#     print(checkEvenFibo(n))

##################################################################################
t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    total = 0
    a = 0
    b = 1
    while b < n:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    print(total)
##################################################################################

# n = int(input())
# for j in range(n):
#     x = int(input())
#     z = [1, 2];
#     s = 2
#     while (z[-1] + z[-2] <= x):
#         z.append(z[-2] + z[-1])
#         if (z[-1] % 2 == 0):
#             s += z[-1];
#     print(s)
