# 5 / 15    5tane başarısız örnek

n, k = map(int, input().split())


def CheckFactors(N, K):
    factors = [0] * (N + K)
    factors[1] = 1
    limit = len(factors)
    count = 0

    for i in range(2, limit):

        if factors[i] == 0:
            xx = i
            while xx < limit:
                factors[xx] += 1
                xx = xx + i
            count = 0
        elif factors[i] == K:
            count += 1
        else:
            count = 0

        if count == K:
            print(i - K + 1)
            count = 1


CheckFactors(n, k)
