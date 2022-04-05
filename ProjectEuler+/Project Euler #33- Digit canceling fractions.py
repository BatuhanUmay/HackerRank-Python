#Test Case 1 / 5

N, K = map(int, input().split())


def compute():
    pay = 0
    payda = 0

    for i in range(1, 10):
        # d is remaining digit in denominator
        for d in range(1, i):
            # n is remaining digit in numerator
            for n in range(1, d):
                if 10 * n * d + i * d == 10 * i * n + d * n:
                    pay += 10 * n + i
                    payda += 10 * i + d

    return str(pay) +  " " + str(payda)


if __name__ == "__main__":
    print(compute())
