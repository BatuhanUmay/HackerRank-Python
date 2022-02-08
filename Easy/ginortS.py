def control(str):
    upperCase = []
    lowerCase = []
    odds = []
    evens = []
    for i in sorted(str):
        if i.isalpha():
            if i.isupper():
                upperCase.append(i)
            else:
                lowerCase.append(i)
        else:
            if int(i) % 2 == 0:
                evens.append(i)
            elif int(i) % 2 == 1:
                odds.append(i)

    result = "".join(lowerCase + upperCase + odds + evens)
    return result

print(control(input()))
##################################################################################
# print(*(sorted(input(), key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))), sep='')
##################################################################################

# def getKey(x):
#     if x.islower():
#         return(1,x)
#     elif x.isupper():
#         return(2,x)
#     elif x.isdigit() :
#         if int(x)%2==1:
#             return(3,x)
#         else :
#             return(4,x)
#
# print(*sorted(input(),key=getKey),sep='')