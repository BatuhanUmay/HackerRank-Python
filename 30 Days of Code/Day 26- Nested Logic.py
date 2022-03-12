# liste = list()
#
#
# def solution(date):
#     date = date.split()
#     day = int(date[0])
#     month = int(date[1])
#     year = int(date[2])
#     liste.append([month, day, year])
#
#
# for _ in range(2):
#     solution(input())
#
# for i in range(1):
#     if liste[1][2] > liste[0][2]:  # returned date < due date
#         print(0)
#     elif liste[1][2] < liste[0][2]:  # returned date > due date
#         print(10000)
#     else:  # returned date = due date
#         if liste[0][1] != liste[1][1]:  # returned month != due month
#             if liste[0][1] > liste[1][1]:  # returned month > due month
#                 if liste[0][0] > liste[1][0]:  # returned day > due day
#                     print(500 * (liste[0][0] - liste[1][0]))
#                 else:  # returned day < due day
#                     print(15 * (liste[0][1] - liste[1][1]))
#             else:  # returned month < due month
#                 print(0)
#
#         else:  # returned month == due month
#             if liste[0][0] > liste[1][0]:  # returned day > due day
#                 print(500 * (liste[0][0] - liste[1][0]))
#             else:  # returned day < due day
#                 print(0)

####################################################################################

rd, rm, ry = [int(x) for x in input().split(' ')]
ed, em, ey = [int(x) for x in input().split(' ')]

if (ry, rm, rd) <= (ey, em, ed):
    print(0)
elif (ry, rm) == (ey, em):
    print(15 * (rd - ed))
elif ry == ey:
    print(500 * (rm - em))
else:
    print(10000)
