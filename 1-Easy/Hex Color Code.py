# import re
#
# if __name__ == "__main__":
#     # reg = re.compile(r"(#[abcdefABCDEF1234567890]{3}|#[abcdefABCDEF1234567890]{6})")
#     # reg = re.compile(r"#[abcdefABCDEF1234567890]{3,}")
#     reg = re.compile(r"(:|,| +)(#[abcdefABCDEF1234567890]{3}|#[abcdefABCDEF1234567890]{6})\b")
#
#     n = int(input())
#
#     for i in range(n):
#         line = input()
#         items = reg.findall(line)
#
#         if items:
#             # print(", ".join(str(s) for s in items ))
#             # for match in items:
#             #   print(items.group())
#             for item in items:
#                 print(item[1])
####################################################################################
import re

pattern = r'(#[0-9a-fA-F]{3,6}){1,2}[^\n ]'
for _ in range(int(input())):
    for x in re.findall(pattern, input()):
        print(x)
####################################################################################
# import re, sys
# [print(j) for i in sys.stdin for j in re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})', i, re.I)]