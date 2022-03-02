# l = list(range(10))
# l = list(map(lambda x: x*x, l))
# l = list(filter(lambda x: x > 10 and x < 80, l))
# print(l)

####################################################################################
# import re
#
# def fun(s):
#   pattern = re.compile("^[\\w-]+@[0-9a-zA-Z]+\\.[a-z]{1,3}$")
#   return pattern.match(s)

####################################################################################
# def fun(s):
#     a = re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',s)
#     return(a)

####################################################################################

# def fun(s):
#     if ('@' not in s) or ('.' not in s) or (' ' in s):
#         return False
#
#     if s.count('@') > 1:
#         return False
#
#     if s.count('.') > 1:
#         return False
#
#     s = s.replace('@', ' ')
#     s = s.replace('.', ' ')
#
#     l = list(map(str, s.split()))
#
#     if len(l) < 3:
#         return False
#
#     for j in l[0]:
#         if j.isalnum() == False and j != '_' and j != '-':
#             return False
#
#     for j in l[1]:
#         if j.isalnum() == False:
#             return False
#
#     if len(l[2]) > 3 or len(l[2]) == 0:
#         return False
#
#     return True
#
#
# def filter_mail(emails):
#     return list(filter(fun, emails))
#
#
# if __name__ == '__main__':
#     n = int(input())
#     emails = []
#     for _ in range(n):
#         emails.append(input())
#
# filtered_emails = filter_mail(emails)
# filtered_emails.sort()
# print(filtered_emails)

####################################################################################
def check_valid(email):
    try:
        username, url = email.split("@")
        website, extension = url.split(".")
    except ValueError:
        return False

    if not username.replace("-", "").replace("_", "").isalnum():
        return False
    if not website.isalnum():
        return False
    if len(extension) > 3:
        return False
    return True

n = int(input())
emails = [input() for email in range(n)]

valid = list(filter(check_valid, emails))
print(sorted(valid))

####################################################################################

"""
isalpha = The Python isalpha() method returns the Boolean value True
if every character in a string is a letter; 
otherwise, it returns the Boolean value False.

isnumeric = The Python isnumeric() method checks whether all the characters
in a string are numbers. If each character is a number, isnumeric() returns
the value True. Otherwise, the method returns the value False.

isalnum = isalnum() checks whether a string contains only letters or numbers or both.
"""
