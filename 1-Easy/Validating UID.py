import re

for _ in range(int(input())):
    s = ''.join(sorted(input()))

    try:
        assert re.search(r'[A-Z]{2}', s)
        assert re.search(r'\d\d\d', s)
        assert re.search(r'[a-zA-Z0-9]{10}', s)
        assert not re.search(r'(.)\1', s)
    except:
        print("Invalid")
    else:
        print("Valid")

####################################################################################
# import re
#
# checks = {
#   "alpha"     : lambda uid: re.match(r".*[A-Z].*[A-Z].*", uid),
#   "num"       : lambda uid: re.match(r".*[0-9].*[0-9].*[0-9].*", uid),
#   "alpha_num" : lambda uid: re.match(r"[A-Za-z0-9]{10}", uid),
#   "repeat"    : lambda uid: not re.match(r".*(.).*\1.*", uid)
# }
#
# def main():
#   for _ in range(int(input())):
#     uid = input()
#     print("Valid" if all(checks[check](uid) for check in checks.keys()) else "Invalid")
#
# if __name__ == "__main__":
#   main()

####################################################################################
# import re
# for _ in range(int(input())):
#     s = input()
#     print('Valid' if all([re.search(r, s) for r in [r'[A-Za-z0-9]{10}',r'([A-Z].*){2}',r'([0-9].*){3}']]) and not re.search(r'.*(.).*\1', s) else 'Invalid')