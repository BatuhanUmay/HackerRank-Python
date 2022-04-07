def taban_aritmetigi(sayi, taban):
    s = ''
    while sayi:
        sayi, kalan = divmod(sayi, taban)
        s += str(kalan)
    return s[::-1]


n, k = map(int, input().split())
# t = 0
# for i in range(1, n + 1):
#     if str(i) == str(i)[::-1]:
#         if taban_aritmetigi(i, k) == taban_aritmetigi(i, k)[::-1]:
#             t += i
# print(t)

ans = sum(i
          for i in range(1, n + 1)
          if str(i) == str(i)[::-1]
          if taban_aritmetigi(i, k) == taban_aritmetigi(i, k)[::-1]
          )
print(ans)
