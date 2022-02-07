def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        unique = ""
        for char in string[i:i+k]:
            if char not in unique:
                unique += char
        print(unique)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

################################################################################

# S, N = input(), int(input())
# for part in zip(*[iter(S)] * N):
#     d = dict()
#     print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))