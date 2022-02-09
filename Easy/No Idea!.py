n, m = map(int, input().split())
array = list(map(int,input().split()))

a = set(map(int, input().split()))
b = set(map(int, input().split()))

happiness = 0

for i in array:
    if i in a:
        happiness += 1
    if i in b:
        happiness -= 1

print(happiness)

###########################################################################################
# _ = input()
# array = input().split()
# like = set(input().split())
# dislike = set(input().split())
# print(sum((i in like) - (i in dislike) for i in array))