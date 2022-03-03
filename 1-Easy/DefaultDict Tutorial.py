# from collections import defaultdict
# d = defaultdict(list)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print i

# This prints:

# ('python', ['awesome', 'language'])
# ('something-else', ['not relevant'])

#############################################################

"""
defaultdict(<class 'list'>, {'sozluk0': ['a'], 'sozluk1': ['a'], 'sozluk2': ['b'], 
'sozluk3': ['a'], 'sozluk4': ['b']})
defaultdict(<class 'list'>, {'Digersozluk0': ['a'], 'Digersozluk1': ['b']})  
"""

from collections import defaultdict
d = defaultdict(list)
list1=[]

n, m = map(int,input().split())

for i in range(0,n):
    d[input()].append(i+1) 

for i in range(0,m):
    list1=list1+[input()]  

for i in list1: 
    if i in d:
        # print(" ".join( map(str,d[i]) ))
        print(*d[i], sep = " ")
    else:
        print(-1)