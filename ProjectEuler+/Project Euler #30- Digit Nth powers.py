N = int(input())


def compute():
    ans = sum(i
              for i in range(2, 1000000)
              if i == nTh_digit_power(i)
              )
    return ans


def nTh_digit_power(num):
    ans = sum(int(i) ** N for i in str(num))
    return ans


print(compute())
