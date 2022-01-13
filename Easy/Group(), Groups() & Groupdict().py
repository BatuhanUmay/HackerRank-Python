# group()
# A group() expression returns one or more subgroups of the match.
# Code

# >>> import re
# >>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
# >>> m.group(0)       # The entire match 
# 'username@hackerrank.com'
# >>> m.group(1)       # The first parenthesized subgroup.
# 'username'
# >>> m.group(2)       # The second parenthesized subgroup.
# 'hackerrank'
# >>> m.group(3)       # The third parenthesized subgroup.
# 'com'
# >>> m.group(1,2,3)   # Multiple arguments give us a tuple.
# ('username', 'hackerrank', 'com')
# groups()
# A groups() expression returns a tuple containing all the subgroups of the match.
# Code

# >>> import re
# >>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
# >>> m.groups()
# ('username', 'hackerrank', 'com')
# groupdict()
# A groupdict() expression returns a dictionary containing all the named subgroups of the match, keyed by the subgroup name.
# Code

# >>> m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
# >>> m.groupdict()
# {'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}

#############################################################

import re

m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)

#############################################################

# a = list(input())
# j = 0
# for i in range(len(a)-1):
#     j += 1
#     if a[i] == a[i+1] and a[i].isalnum():
#         print(a[i])
#         break
# if j==len(a)-1:
#     print(-1)









