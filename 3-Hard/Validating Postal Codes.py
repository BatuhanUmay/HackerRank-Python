regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=.\1)"

import re

P = input()

print(bool(re.match(regex_integer_in_range, P))
      and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
####################################################################################
# s = input()
# print(s.isdigit() and 100000 <= int(s) <= 999999 and
#       sum([s[i] == s[i+2] for i in range(0, 4)]) < 2)
#
####################################################################################
# Kendi Çözümüm
# P = input()
# result = None
# for i in range(len(P)):
#     if i+2 != int(len(P)):
#         if P[i] == P[i+1] or P[i] == P[i+2] or int(P) > 999999 or int(P) < 100000:
#             result = False
#             break
#     else:
#         result = True
#         break
# print("True" if result else "False")
