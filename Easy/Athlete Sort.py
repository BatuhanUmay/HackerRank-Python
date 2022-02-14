# N, M = map(int, input().split())
# arr = [input() for _ in range(N)]
# K = int(input())
#
# print(arr)
# for i in sorted(arr, key = lambda x : int(x.split()[K])):
#     print(i)

#############################################################

n, m = map(int, input().split())
nums = [list(map(int, input().split())) for i in range(n)]
k = int(input())

nums.sort(key=lambda x: x[k])

for line in nums:
    print(*line, sep=' ')
#############################################################

# data, k = [list(map(int, input().split(' '))) for _ in range(int(input().split(' ')[0]))], int(input())
# [print(*row) for row in sorted(data, key=lambda lst: lst[k])]