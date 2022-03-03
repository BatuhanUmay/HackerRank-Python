# >>> from collections import deque
# >>> d = deque()
# >>> d.append(1)
# >>> print d
# deque([1])
# >>> d.appendleft(2)
# >>> print d
# deque([2, 1])
# >>> d.clear()
# >>> print d
# deque([])
# >>> d.extend('1')
# >>> print d
# deque(['1'])
# >>> d.extendleft('234')
# >>> print d
# deque(['4', '3', '2', '1'])
# >>> d.count('1')
# 1
# >>> d.pop()
# '1'
# >>> print d
# deque(['4', '3', '2'])
# >>> d.popleft()
# '4'
# >>> print d
# deque(['3', '2'])
# >>> d.extend('7896')
# >>> print d
# deque(['3', '2', '7', '8', '9', '6'])
# >>> d.remove('2')
# >>> print d
# deque(['3', '7', '8', '9', '6'])
# >>> d.reverse()
# >>> print d
# deque(['6', '9', '8', '7', '3'])
# >>> d.rotate(3)
# >>> print d
# deque(['8', '7', '3', '6', '9'])

#############################################################

from collections import deque
d = deque()

n = int(input())

for i in range(n):
    secim = input().split()
    
    if secim[0] == "append":
        d.append(int(secim[1]))

    if secim[0] == "appendleft":
        d.appendleft(int(secim[1]))
        
    if secim[0] == "pop":
        d.pop()
        
    if secim[0] == "popleft":
        d.popleft()

print(*d)

#############################################################

# from collections import deque
# d = deque()
# for _ in range(int(input())):
#     inp = input().split()
#     getattr(d, inp[0])(*[inp[1]] if len(inp) > 1 else [])
    
#     # if len(inp) > 1:
#     #     getattr(d, inp[0])(inp[1])
#     # else:
#     #     getattr(d, inp[0])

# print(*[item for item in d])







