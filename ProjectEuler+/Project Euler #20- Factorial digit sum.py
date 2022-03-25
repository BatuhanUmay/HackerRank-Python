import math

for _ in range(int(input())):
    num = int(input())
    r = math.factorial(num)
    ans = sum(int(i) for i in str(r))
    print(ans)

################################################################

# import math
#
# for _ in range(int(input())):
#     print(sum(list(map(int, str(math.factorial(int(input())))))))
