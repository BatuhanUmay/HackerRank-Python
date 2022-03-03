for t in range(int(input())):
    n = int(input())
    liste = [int(i) for i in input().split()]
    min_list = liste.index(min(liste))
    left = liste[:min_list]
    right = liste[min_list + 1:]
    if left == sorted(left, reverse=True) and right == sorted(right):
        print("Yes")
    else:
        print("No")

####################################################################################

# for t in range(input()):
#     input()
#     lst = map(int, input().split())
#     l = len(lst)
#     i = 0
#     while i < l - 1 and lst[i] >= lst[i+1]:
#         i += 1
#     while i < l - 1 and lst[i] <= lst[i+1]:
#         i += 1
#     print("Yes" if i == l - 1 else "No")
