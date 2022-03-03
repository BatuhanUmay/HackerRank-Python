# testCases = int(input())

# for i in range(testCases):
#     number_of_elementsA = int(input())

#     A = set(map(int, input().split()))

#     number_of_elementsB = int(input())

#     B = set(map(int, input().split()))

#     if A.issubset(B):
#         print("True")
#     else:
#         print("False")
        
#############################################################

for _ in range(int(input())):
    x, a, z, b = input(), set(input().split()), input(), set(input().split())
print(a.issubset(b))

