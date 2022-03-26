NAMES = []
for _ in range(int(input())):
    NAMES.append(input())

NAMES = sorted(NAMES)

def compute(NAMES, position):
    ans = sum((ord(i) - ord('A') + 1) * (position + 1)
              for i in NAMES
              )
    return ans


for _ in range(int(input())):
    name = input()
    res = compute(NAMES[NAMES.index(name)], NAMES.index(name))
    print(res)

######################################################################

# names = sorted(input() for _ in range(int(input())))
# for _ in range(int(input())):
#     s = input()
#     print(sum(ord(i) - 64 for i in s)*(names.index(s)+1))
