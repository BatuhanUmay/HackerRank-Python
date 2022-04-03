table = [1] + [0] * 100001
coin = [1, 2, 5, 10, 20, 50, 100, 200]

for i in range(8):
    for j in range(coin[i], len(table)):
        table[j] += table[j - coin[i]]

for x in range(int(input())):
    num = int(input())
    print(table[num] % 1000000007)

####################################################################

# from time import time
#
# GIVEN_COINS = [1, 2, 5, 10, 20, 50, 100, 200]
# N = len(GIVEN_COINS)
# MAX_AMOUNT = 10 ** 5
# MOD = (10 ** 9) + 7
#
#
# def using2dArray(userAmount):
#     START = time()
#     dp2 = [[0] * (MAX_AMOUNT + 1)] * (N + 1)
#     for i in range(N + 1):
#         dp2[i][0] = 1
#     for i in range(1, N + 1):
#         for j in range(MAX_AMOUNT + 1):
#             if j >= GIVEN_COINS[i - 1]:
#                 dp2[i][j] = dp2[i][j - GIVEN_COINS[i - 1]] + dp2[i - 1][j]
#             else:
#                 dp2[i][j] = dp2[i - 1][j]
#     answer = dp2[N][userAmount] % MOD
#     print("Using 2D Array, Ans: {}, Time: {} seconds".format(answer, time() - START))
#
#
# def using1dArray(userAmount):
#     START = time()
#     dp1 = [0] * (MAX_AMOUNT + 1)
#     dp1[0] = 1
#     for i in range(N):
#         for j in range(GIVEN_COINS[i], MAX_AMOUNT + 1):
#             dp1[j] += dp1[j - GIVEN_COINS[i]]
#     answer = dp1[userAmount] % MOD
#     print("Using 1D Array, Ans: {}, Time: {} seconds".format(answer, time() - START))
#
#
# def compare(userInput):
#     global caseNo
#     using2dArray(userInput)
#     using1dArray(userInput)
#     print("-------")
#
#
# compare(200)
# compare(1000)
# compare(10000)
# compare(100000)
