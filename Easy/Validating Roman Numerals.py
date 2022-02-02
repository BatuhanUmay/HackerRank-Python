thousand = 'M{0,3}'
hundred = '(C(D|M)|D?C{0,3})'
ten = '(X(L|C)|L?X{0,3})'
unit = '(I(X|V)|(X|V)?I{0,3})'
regex_pattern = r'^' + thousand + hundred + ten + unit + '$'

# regex_pattern =r'^M{,3}(C(D|M)|D?C{,3})(X(L|C)|L?X{,3})(I(X|V)|(X|V)?I{,3})$'

import re

print(str(bool(re.match(regex_pattern, input()))))

####################################################################################
# from roman import fromRoman
#
# try:
#     if 0<fromRoman(input())<4000:
#         print(True)
#     else:
#         print(False)
# except:
#     print(False)