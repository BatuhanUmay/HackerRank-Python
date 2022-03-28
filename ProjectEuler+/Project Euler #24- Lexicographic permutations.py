string = "abcdefghijklm"


def find_fac(no):
    i = 1
    while no != 0:
        fac[13 - i] = no % i
        no = no // i
        i += 1

    return fac


def find_string(fac):
    arr = list(string)
    result = ""

    for i in range(len(fac)):
        result += arr.pop(fac[i])

    return result


t = int(input())

for i in range(t):
    fac = [0] * 13
    no = int(input())
    no = no - 1
    fac = find_fac(no)
    # print(fac)
    result = find_string(fac)
    print(result)
#########################################################################
# N = 13
#
# fac = [1] * 14
# for i in range(1, 14):
#     fac[i] = fac[i - 1] * i
#
#
# def solve(n):
#     s = list('abcdefghijklm')
#     ans = ''
#     cnt = 0
#     k = 1
#     while k < N + 1:
#         for i in range(len(s)):
#             if cnt + fac[N - k] >= n:
#                 ans += s[i]
#                 del (s[i])
#                 k += 1
#                 break
#             cnt += fac[N - k]
#     print(ans)
#
#
# for _ in range(int(input())):
#     solve(int(input()))
#
#########################################################################
# from math import factorial as f
#
#
# def Lexicographic_Permutations(word, n):
#     queue = list(word)
#     word_perm = ''
#     i = 1
#
#     while queue:
#         pos = n // f(len(word) - i)
#         word_perm += queue.pop(pos)
#         n -= pos * f(len(word) - i)
#         i += 1
#
#     return word_perm
#
#
# if __name__ == '__main__':
#     word = 'abcdefghijklm'
#
#     for _ in range(int(input())):
#         n = int(input())
#         print(Lexicographic_Permutations(word, n - 1))

#########################################################################
# string = list("abcdefghijklm")
# # Precompute Factorials of First 13 Numbers
# factorials = [1]
# for i in range(1, 14):
#     factorials.append(factorials[i - 1] * i)
#
#
# def nthPermutation(arr, k, n=13, ans=""):
#     # Base Case
#     if n == 1:
#         ans += arr.pop(0)
#         return ans
#     index = k // factorials[n - 1]
#     # Boundary Element
#     if not k % factorials[n - 1]:
#         index -= 1
#     ans += arr.pop(index)
#     k -= factorials[n - 1] * index
#     return nthPermutation(arr, k, n - 1, ans)
#
#
# for T in range(int(input())):
#     N = int(input())
#     answer = nthPermutation(string[:], N)
#     print(answer)
