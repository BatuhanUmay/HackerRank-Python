# import email.utils
# print(email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>'))
# print(email.utils.formataddr(('DOSHI', 'DOSHI@hackerrank.com')))

# ('DOSHI', 'DOSHI@hackerrank.com')
# DOSHI <DOSHI@hackerrank.com>

####################################################################################
import re

pattern = re.compile(r"^[a-zA-Z][\w\-.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$")
for _ in range(int(input())):
    name, emailParse = email.utils.parseaddr(input())
    if pattern.match(emailParse):
        print(email.utils.formataddr((name, emailParse)))


####################################################################################
# import email.utils
#
# def isValid(address):
#     if ('@' in address) and ('.' in address):
#         username = address[:address.index('@')]
#         firstLetterUser = username[0].isalpha()
#
#         username = username.replace("_", "")
#         username = username.replace("-", "")
#         username = username.replace(".", "")
#
#         address = address[address.index('@') + 1:]
#         domain = address[:address.index('.')]
#         extension = address[address.index('.') + 1:]
#
#         result = firstLetterUser and username.isalnum() and domain.isalpha() and extension.isalpha() and len(
#             extension) <= 3
#         return result
#
#     return False
#
# for _ in range(int(input())):
#     address = input()
#     if isValid(email.utils.parseaddr(address)[1]):
#         print(address)