palindromelist = []
for i in range(100, 1000):
    for j in range(100, 1000):
        num = i * j
        if str(num) == str(num)[::-1]:
            palindromelist.append(num)
palindromelist.sort()
length = len(palindromelist)

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        a = int(input())
        for i in range(length - 1, 0, -1):
            if palindromelist[i] < a:
                print(palindromelist[i])
                break
