import math

N = int(input())
number = "".join(str(i) for i in range(1, N + 1))


def compute():
    ans = sum(i for i in range(1, 10000) if pandigital_product(i))
    return ans


def pandigital_product(n):
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            # 39 × 186 = 7254
            res = str(i) + str(n // i) + str(n)
            if "".join(sorted(res)) == number:
                return True
    return False


print(compute())
