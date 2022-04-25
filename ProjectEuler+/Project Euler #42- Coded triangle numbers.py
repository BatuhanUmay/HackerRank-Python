# def is_triangle(n):
#     formula = ((1 + 8 * n) ** 0.5 - 1) / 2
#
#     if formula == int(formula):
#         return int(formula)
#     else:
#         return -1
#
#
# for i in range(int(input())):
#     num = int(input())
#
#     print(is_triangle(num))

###################################################################

for i in range(int(input())):
    num = int(input())
    root = int((2 * num) ** 0.5)

    if root * (root + 1) == 2 * num:
        print(root)
    else:
        print(-1)
