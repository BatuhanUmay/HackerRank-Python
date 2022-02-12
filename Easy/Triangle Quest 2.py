# for i in range(1, int(input())+1):
#     for j in range(1, i+1):
#         print(j, end='')
#     for k in range(i-1,0,-1):
#         print(k, end='')
#
#     print()

##Üstteki örnekte çıktı doğru ama hackerrank için geçerli değil
###########################################################################################

for i in range(1, int(input()) + 1):
    # More than 2 lines will result in 0 score. Do not leave a blank line also
    print(int(((10 ** i - 1) / 9) ** 2))
    #print((sum([10 ** j for j in range(0, i)])) ** 2)
