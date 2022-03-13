import sys

t = int(input().strip())
for i in range(t):
    num = int(input())

    number_of_multiple_3 = (num - 1) // 3
    number_of_multiple_5 = (num - 1) // 5
    number_of_multiple_15 = (num - 1) // 15
    """
    total number of multiples of n in the given number
    example :-

        input = 100
        (100-1)//3 = 33
        so there are 33 multiples of 3 in 100

        input = 100
        (100-1)//5 = 19
        so there are 19 multiples of 5 in 100

    """

    number_of_multiple_3 = 3 * (number_of_multiple_3 * (number_of_multiple_3 + 1)) // 2
    number_of_multiple_5 = 5 * (number_of_multiple_5 * (number_of_multiple_5 + 1)) // 2
    number_of_multiple_15 = 15 * (number_of_multiple_15 * (number_of_multiple_15 + 1)) // 2
    """
    sum of n terms = half of multiplication of n and n+1
    sum of n terms of any specific number =  that specific number * (half of multiplication of n and n+1)
    example :-

        sum of n terms of 3  = 3 * (half of multiplication of n and n+1)
        sum of 33 terms of 3 = 3 *(33 * (33 + 1)//2)
                             = 3 *(33 * 34 //2)
                             = 3 *(1122//2)
                             = 3 *(561)
                             = 1683

        sum of n terms of 5 = 5 * (half of multiplication of n and n+1)

    """
    print(number_of_multiple_3 + number_of_multiple_5 - number_of_multiple_15)

##################################################################################
# t = int(input())
#
# def ar(x):
#     return x * (x + 1);
#
#
# for i in range(t):
#     n = int(input())
#     n -= 1;
#     a = int(n / 3);
#     b = int(n / 5);
#     c = int(n / 15);
#     print(int(int(3 * ar(a) + 5 * ar(b) - 15 * ar(c)) >> 1));
