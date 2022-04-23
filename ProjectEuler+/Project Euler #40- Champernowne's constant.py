from bisect import bisect_left as bl

s = [0] * 21
p = 9
s[1] = 9
tavan = [1] * 21
tavan[1] = 10

for i in range(2, 21):
    tavan[i] = tavan[i - 1] * 10
    p *= 10
    s[i] = s[i - 1] + p * i

# for i in s:
#     if i > 10 ** 18:
#         print(s.index(i))


def solve(n):
    j = bl(s, n)
    i = j - 1
    n -= s[i]
    ans = tavan[i]
    ans = ans + (n // j)
    n = n % j
    if n == 0:
        ans -= 1
        return (ans % 10)
    return (int(str(ans)[n - 1]))


for _ in range(int(input())):
    q = list(map(int, input().split()))
    ans = 1
    for i in q:
        ans *= solve(i)
    print(ans)
