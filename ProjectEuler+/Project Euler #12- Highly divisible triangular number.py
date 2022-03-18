def All_Factors(n):
    factors = []

    for div in range(1, int(n ** 0.5) + 1):
        if n % div == 0:
            factors.append(div)

            other = n // div
            if other != div:
                factors.append(other)

    return factors


# Main function
# Time complexity = O(n^1.5))
def Divisible_Triangular_Number(n):
    i = 1

    while True:
        # Triangle number is the sum of consecutive numbers
        sum = i * (i + 1) // 2

        '''
        _____Previous version: O(sum^0.5) = O(i)_____
    
        factors_number = len(All_Factors(sum))
    
        _____Optimized version: O(i^0.5)_____
    
        if i%2 == 0:
          factors_number = len(All_Factors(i//2))*len(All_Factors(i+1))
        else:
          factors_number = len(All_Factors(i))*len(All_Factors((i+1)//2))
    
        _____Why?_____
    
        We break "sum" into 2 parts to reduce time complexity:
        NumberOfDivisors(a.b) = NumberOfDivisors(a).NumberOfDivisors(b)
        '''

        if i % 2 == 0:
            factors_number = len(All_Factors(i // 2)) * len(All_Factors(i + 1))
        else:
            factors_number = len(All_Factors(i)) * len(All_Factors((i + 1) // 2))

        if factors_number > n:
            return sum
        else:
            i += 1


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        print(Divisible_Triangular_Number(n))

############################################################################

# import math
#
#
# def div(p):
#     dic = {}
#     for j in range(p, 1, -1):
#         if pn(j) == 0:
#             while p % j == 0:
#                 if j in dic:
#                     dic[j] += 1
#                 else:
#                     dic[j] = 1
#                 p = p // j
#     ans = 1
#     for k, v in dic.items():
#         ans = ans * (dic[k] + 1)
#     return ans
#
#
# def pn(p):
#     # if flag = 0, it is prime, else composite
#     flag = 0
#     for k in range(2, int(math.sqrt(p)) + 1):
#         if p % k == 0:
#             flag = 1
#             break
#     return flag
#
#
# t = int(input())
# for i in range(t):
#     n = int(input())
#     i = 0
#     ans = 0
#     while i >= 0:
#         x = i * (i + 1) // 2
#         if div(x) > n:
#             ans = x
#             break
#         i += 1
#
#     print(ans)

