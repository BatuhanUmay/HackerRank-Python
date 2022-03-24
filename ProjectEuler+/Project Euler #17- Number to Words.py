ONES = ['', 'One ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ', 'Eight ', 'Nine ', 'Ten ',
        'Eleven ', 'Twelve ', 'Thirteen ', 'Fourteen ', 'Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ',
        'Nineteen ']
TENS = ['', '', 'Twenty ', 'Thirty ', 'Forty ', 'Fifty ', 'Sixty ', 'Seventy ', 'Eighty ', 'Ninety ']


def to_english(num):
    if 0 <= num < 20:
        return ONES[num]
    elif 20 <= num < 100:
        return TENS[num // 10] + (ONES[num % 10] if num % 10 != 0 else "")
    elif 100 <= num < 1000:
        return ONES[num // 100] + "Hundred " + (to_english(num % 100) if num % 100 != 0 else "")
    elif 1000 <= num < 1000000:
        return to_english(num // 1000) + "Thousand " + (to_english(num % 1000) if num % 1000 != 0 else "")
    elif 1000000 <= num < 1000000000:
        return to_english(num // 1000000) + "Million " + (to_english(num % 1000000) if num % 1000000 != 0 else "")
    elif 1000000000 <= num < 1000000000000:
        return to_english(num // 1000000000) + "Billion " + (
            to_english(num % 1000000000) if num % 1000000000 != 0 else "")
    elif 1000000000000 <= num < 1000000000000000:
        return to_english(num // 1000000000000) + "Trillion " + (
            to_english(num % 1000000000000) if num % 1000000000000 != 0 else "")


for _ in range(int(input())):
    num = int(input())
    print(to_english(num))

########################################################################

# one_digit = {'0': '', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
#              '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'}
# two_digit = {'10': 'Ten', '11': 'Eleven', '12': 'Twelve', '13': 'Thirteen', '14': 'Fourteen', '15': 'Fifteen', '16': 'Sixteen', '17': 'Seventeen', '18': 'Eighteen', '19': 'Nineteen',
#              '2': 'Twenty', '3': 'Thirty', '4': 'Forty', '5': 'Fifty', '6': 'Sixty', '7': 'Seventy', '8': 'Eighty', '9': 'Ninety'}
# arzesh = {0: '', 1: 'Thousand', 2: 'Million', 3: 'Billion', 4: "Trillion"}
#
#
# def give_three_digit(s):
#     # s = string containing 3 digits
#     ans = ''
#     if s[0] != '0':
#         ans += one_digit[s[0]] + ' ' + 'Hundred' + ' '
#     if s[1] != '0' and s[1] != '1':
#         ans += two_digit[s[1]] + ' '
#     if s[1] == '1':
#         ans += two_digit[s[1:]] + ' '
#     if s[1] != '1' and s[2] != '0':
#         ans += one_digit[s[2]] + ' '
#     if s[1] != '1' and s[2] == '0':
#         ans += one_digit[s[2]]
#     return (ans)
#
#
# def solve(n):
#     if n == '0':
#         print('Zero')
#         return
#     num = []
#     ans = ''
#     i = 0
#     num.append(n[:len(n) % 3])
#     i += (len(n) % 3)
#     while i < len(n):
#         num.append(n[i:i + 3])
#         i += 3
#     if num[0] == '':
#         del (num[0])
#     num[0] = '0' * (3 - len(num[0])) + num[0]
#
#     N = len(num)
#     for i in range(N):
#         if num[i] == '000':
#             continue
#         ans += give_three_digit(num[i])
#         ans += arzesh[N - i - 1] + ' '
#     print(ans[:len(ans) - 1])
#
#
# for _ in range(int(input())):
#     solve(input())

########################################################################

# digits = ['', 'One ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ', 'Eight ', 'Nine ', 'Ten ',
#           'Eleven ', 'Twelve ', 'Thirteen ', 'Fourteen ', 'Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ',
#           'Nineteen ']
# two_d = ['', '', 'Twenty ', 'Thirty ', 'Forty ', 'Fifty ', 'Sixty ', 'Seventy ', 'Eighty ', 'Ninety ']
# powers = ['', 'Thousand ', 'Million ', 'Billion ', 'Trillion ']
#
#
# def tens(n):
#     if n == 0: return ''
#     if n < 20: return digits[n]
#     return two_d[n // 10] + digits[n % 10]
#
#
# def hundered(n):
#     if n == 0: return ''
#     if n < 100: return tens(n % 100)
#     return digits[n // 100] + 'Hundred ' + tens(n % 100)
#
#
# def word(n):
#     if n == 0: return 'Zero'
#     c, wrd = 0, ''
#     while n > 0:
#         h = n % 1000
#         if h != 0: wrd = hundered(h) + powers[c] + wrd
#         n, c = n // 1000, c + 1
#     return wrd
#
#
# for c in range(int(input())): print(word(int(input())).rstrip())

########################################################################

# c = {0: "Thousand ", 1: "Million ", 2: "Billion ", 3: "Trillion "}
#
#
# def fun(n):
#     dic = {0: "", 1: "One ", 2: "Two ", 3: "Three ", 4: "Four ", 5: "Five ", 6: "Six ", 7: "Seven ", 8: "Eight ",
#            9: "Nine ", 10: "Ten ", 11: "Eleven ", 12: "Twelve ", 13: "Thirteen ", 14: "Fourteen ", 15: "Fifteen ",
#            16: "Sixteen ", 17: "Seventeen ", 18: "Eighteen ", 19: "Nineteen ", 20: "Twenty ", 30: "Thirty ",
#            40: "Forty ", 50: "Fifty ", 60: "Sixty ", 70: "Seventy ", 80: "Eighty ", 90: "Ninety "}
#     if n >= 100:
#         h = n // 100
#         r = n % 100
#         if (r <= 19):
#             return dic[h] + "Hundred " + dic[r]
#         else:
#             return dic[h] + "Hundred " + dic[r - (r % 10)] + dic[r % 10]
#     else:
#         if (n <= 19):
#             return dic[n]
#         else:
#             return dic[n - (n % 10)] + dic[n % 10]
#
#
# n = int(input().strip())
# for i in range(n):
#     m = int(input())
#     li = []
#     if (m == 0):
#         print("Zero")
#     else:
#         while (m > 100):
#             re = m % 1000
#             m = m // 1000
#             li.append(fun(re))
#         if (m > 0):
#             li.append(fun(m))
#         k = len(li)
#         s = li[0]
#         for i in range(1, k):
#             if (li[i] != ""):
#                 s = li[i] + c[i - 1] + s
#         print(s)

########################################################################

# ones = ["", "One ", "Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine "]
# elevens = ["Ten ", "Eleven ", "Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ",
#            "Nineteen "]
# tens = ["", "", "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety "]
# others = ["", "Thousand ", "Million ", "Billion ", "Trillion ", "Hundred "]
#
#
# def number_places(num, places=""):
#     n1 = int(num[0])
#     n2 = int(num[1])
#     n3 = int(num[2])
#     if n1 == 0:
#         if n2 == 1:
#             return f"{elevens[n3]}{places}"
#         elif n2 == 0 and n3 == 0:
#             return ""
#         else:
#             return f"{tens[n2]}{ones[n3]}{places}"
#     elif n2 == 1:
#         return f"{ones[n1]}{others[-1]}{elevens[n3]}{places}"
#     else:
#         return f"{ones[n1]}{others[-1]}{tens[n2]}{ones[n3]}{places}"
#
#
# t = int(input())
# for a0 in range(t):
#     number = input()
#
#     if int(number) > 0:
#         length = len(number)
#         if length % 3 == 1:
#             number = "00" + number
#         elif length % 3 == 2:
#             number = "0" + number
#         b = 0  # take starting position in others list
#         c = -1  # iterate the others list
#         result = ""  # final result after loop
#         length = len(number)
#         for i in range(length):
#             if (length - i) % 3 == 0:
#                 c += 1
#                 if length == 15:
#                     b = others[4 - c]
#                 elif length == 12:
#                     b = others[3 - c]
#                 elif length == 9:
#                     b = others[2 - c]
#                 elif length == 6:
#                     b = others[1 - c]
#                 elif length == 3:
#                     b = ""
#                 num1 = number[i] + number[i + 1] + number[i + 2]
#                 num_word = number_places(num=num1, places=b)
#                 result += num_word
#         print(result)
#     else:
#         print("Zero")
