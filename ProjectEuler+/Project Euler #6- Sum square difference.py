t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    TheSumOfTheSquares = n * (n + 1) * (2 * n + 1) // 6
    TheSquareOfTheSum = (n * (n + 1) // 2) ** 2
    print(TheSquareOfTheSum - TheSumOfTheSquares)
