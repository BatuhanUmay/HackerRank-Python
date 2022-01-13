from itertools import product

# a = list()
# b = list()

# secim1 = int(input("Kaç eleman eklemek istiyorsunuz:"))
# secim2 = int(input("Kaç eleman eklemek istiyorsunuz:"))

# for i in range(secim1):
#     sayi = int(input("A listesi için Eklenecek sayı:"))
#     a.append(sayi)

# for i in range(secim2):
#     sayi = int(input("B listesi için Eklenecek sayı:"))
#     b.append(sayi)

# c = [a,b]

# c = list(product(*c))
# print(c)

#############################################################

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(*product(a,b))


