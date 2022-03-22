for _ in range(int(input())):
    power = int(input())
    ans = 2 ** power
    digits = sum(int(i) for i in str(ans))
    print(digits)

#########################################################################

# if __name__ == '__main__':
#     t = int(input())
#     for i in range(t):
#         n = int(input())
#         num = 1 << n
#         s = 0
#         while num > 0:
#             s = s + num % 10
#             num = num // 10
#         print(s)
