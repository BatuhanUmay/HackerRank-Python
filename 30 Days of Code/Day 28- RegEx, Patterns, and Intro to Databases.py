import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())
    names = list()

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]

        if emailID.endswith('@gmail.com'):
            names.append(firstName)

    print(*sorted(names), sep='\n')

####################################################################################

# import re
#
# lst=[]
# for a0 in range(int(input())):
#     firstName, emailID = [str(s) for s in input().split()]
#     if re.search('@gmail\.com$', emailID):
#    	    lst.append(firstName)
# print(*sorted(lst), sep='\n')
####################################################################################

# import sys
# import re
#
# N = int(input().strip())
# db = [input().split() for _ in range(N)]
# gmails = re.compile(r'@gmail\.com')
# names = sorted([entry[0] for entry in db if re.search(gmails, entry[1])])
# print(*names, sep='\n')
