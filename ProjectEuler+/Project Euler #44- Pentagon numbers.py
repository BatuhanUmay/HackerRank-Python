import math

n, k = map(int, input().split())

for i in range(k + 1, n + 1):
    minus = ((i * (3 * i - 1)) / 2) - (((i - k) * (3 * (i - k) - 1)) / 2)
    plus = ((i * (3 * i - 1)) / 2) + (((i - k) * (3 * (i - k) - 1)) / 2)
    if (1 + math.sqrt(1 - 4 * 3 * -minus * 2)) / 6 == int((1 + math.sqrt(1 - 4 * 3 * -minus * 2)) / 6) or (
            1 + math.sqrt(1 - 4 * 3 * -plus * 2)) / 6 == int((1 + math.sqrt(1 - 4 * 3 * -plus * 2)) / 6):
        print((i * (3 * i - 1)) // 2)
