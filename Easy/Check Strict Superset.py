# kume = set(map(int, input().split()))
# print(all( [ kume.issuperset(set(map(int, input().split()))) for i in range(int(input())) ] ))

#############################################################

kume = set(map(int, input().split()))
counter = 0
n = int(input())

for _ in range(n):
    k = set(map(int, input().split()))
    if kume.issuperset(k):
        counter += 1

print(counter == n)