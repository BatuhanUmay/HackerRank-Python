set_eight = set("12345678")
set_nine = set("123456789")
pandigitals = []

n, k = map(int, input().split())

for i in range(2, 10 ** 4):
    digit = 1
    str_num = ""

    while True:
        num = i * digit
        str_num += str(num)

        if len(str_num) >= k:
            if len(str_num) > k:
                break
            else:
                if k == 8 and set(str_num) == set_eight:
                    pandigitals.append(int(i))
                elif k == 9 and set(str_num) == set_nine:
                    pandigitals.append(int(i))
        digit += 1

pandigitals.sort()
for i in pandigitals:
    if i < n:
        print(i)

##################################################################

# n, k = map(int, input().split())
# l = []
# for i in range(1, k + 1):
#     l.append(str(i))
# for i in range(2, n + 1):
#     s = ""
#     for j in range(1, k):
#         s += str(i * j)
#         r = list(s)
#         r = sorted(r)
#         if (r == l):
#             print(i)
#             break
