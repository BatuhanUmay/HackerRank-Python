# def Number_Spiral_Diagonals(n):
#     N = (n + 1) // 2
#
#     sum1 = n * (n + 1) * (n + 2) // 6 - 3 * N * (1 + n) // 2 + 3 * N
#     sum2 = n * (n + 1) * (n + 2) // 6 - 2 * N * (1 + n) // 2 + 2 * N
#     sum3 = n * (n + 1) * (n + 2) // 6 - 1 * N * (1 + n) // 2 + 1 * N
#     sum4 = n * (n + 1) * (n + 2) // 6
#     sum = sum1 + sum2 + sum3 + sum4 - 3
#
#     return sum % (10 ** 9 + 7)
#
#
# if __name__ == '__main__':
#     for _ in range(int(input())):
#         n = int(input())
#         print(Number_Spiral_Diagonals(n))

###############################################################################


t = int(input().strip())
for _ in range(t):
    N = int(input().strip())
    if N == 1:
        print(1)
    else:
        n = N // 2
        print((1 + 4 * (n * 6 + 9 * n * (n - 1) // 2 + 2 * (n - 1) * n * (2 * n - 1) // 3)) % 1000000007)
