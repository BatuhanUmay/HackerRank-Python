def isPrime(num):
    prime = True
    for i in range(2, int(pow(num, 0.5)) + 1):
        if num % i == 0:
            prime = False
            break
    return prime


maxi = 0
for _ in range(int(input())):
    num = int(input())
    for i in range(1, int(pow(num, 0.5)) + 1):
        if num % i == 0:
            if isPrime(num // i):
                maxi = num // i
                break
            elif isPrime(i):
                maxi = i
    print(maxi)

#############################################################################################
# T = int(input())
# for z in range(T):
#     N = int(input())
#     i = 2
#     largest_prime = 2
#     while i * i <= N:
#         while N % i == 0:
#             largest_prime = i
#             N //= i
#         i += 1
#     if N > largest_prime:
#         largest_prime = N;
#     print(largest_prime)
