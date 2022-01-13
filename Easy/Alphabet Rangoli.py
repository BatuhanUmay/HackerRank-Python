# ing = "abcdefghijklmnopqrstuvwxyz"

import string


# def print_rangoli(size):

#     alpha = string.ascii_lowercase

#     n = int(input())
#     L = []
    
#     for i in range(n):
#         s = "-".join(alpha[i:n])
#         L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
        
#     print('\n'.join(L[:0:-1]+L))


# def print_rangoli(size):
#     alp = 'abcdefghijklmnopqrstuvwxyz'
#     for i in range(size-1,-size,-1):
#         temp = '-'.join(alp[size-1:abs(i):-1]+alp[abs(i):size])
#         print(temp.center(4*size-3,'-'))

"""
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""

def print_rangoli(size):
    satir_uzunluk = 4 * size - 3
    karakter = string.ascii_lowercase

    for i in list(range(size))[::-1] + list(range(1, size)):
        print("-".join(karakter[size-1:i:-1] + karakter[i:size]).center(satir_uzunluk,"-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)





