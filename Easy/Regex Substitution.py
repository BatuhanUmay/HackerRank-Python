# Transformation of Strings
#
# Code
#
# import re
#
# #Squaring numbers
# def square(match):
#     number = int(match.group(0))
#     return str(number**2)
#
# print re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9")
# Output
#
# 1 4 9 16 25 36 49 64 81
#
# Replacements in Strings
#
# Code
#
# import re
#
# html = """
# <head>
# <title>HTML</title>
# </head>
# <object type="application/x-flash"
#   data="your-file.swf"
#   width="0" height="0">
#   <!-- <param name="movie"  value="your-file.swf" /> -->
#   <param name="quality" value="high"/>
# </object>
# """
#
# print re.sub("(<!--.*?-->)", "", html) #remove comment

####################################################################################

for _ in range(int(input())):
    line = input()

    while ' && ' in line or ' || ' in line:
        line = line.replace(" && ", " and ").replace(" || ", " or ")

    print(line)
####################################################################################
# import re
#
# N = int(input())
#
# for i in range(N):
#     print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))

####################################################################################

# import re
# S=int(input())
# for i in range(S):
#       pattern1=re.compile(r'(?<= )(&&)(?= )')
#       pattern2=re.compile(r'(?<= )(\|\|)(?= )')
#       print(pattern2.sub('or', pattern1.sub('and', input())))