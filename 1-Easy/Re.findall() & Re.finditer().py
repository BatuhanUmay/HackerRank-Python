# re.findall()
# The expression re.findall() returns all the non-overlapping matches of patterns in a string as a list of strings.
# Code

# >>> import re
# >>> re.findall(r'\w','http://www.hackerrank.com/')
# ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
# re.finditer()
# The expression re.finditer() returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern in the string.
# Code

# >>> import re
# >>> re.finditer(r'\w','http://www.hackerrank.com/')
# <callable-iterator object at 0x0266C790>
# >>> map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
# ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

#############################################################

import re
sesli = "aeiou"
sessiz = "qwrtypsdfghjklzxcvbnm"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (sessiz, sesli, sessiz), input(), flags = re.I)
print('\n'.join(m or ['-1']))

#############################################################

# import re
# S=input()
# v='aeiou'
# pattern = re.compile('[^{0}][{0}][{0}]+[^{0}]'.format(v),re.I)
# r = pattern.search(S)
# if not r: print('-1')    
# while r:    
#     print(S[r.start()+1:r.end()-1]) #removing 1st & last consonant
#     r = pattern.search(S,r.start()+1)

#############################################################

# import re

# S = input()
# ptrn = r"[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm][AEIOUaeiou]{2,}[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]"
# founded_list = list(map(lambda x: x.group(1), re.finditer("(?=({}))".format(ptrn), S)))

# if founded_list:
#     for i in founded_list:
#         print(i[1:len(i)-1])
# else:
#     print(-1)
