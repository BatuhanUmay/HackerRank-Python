grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)


def left_right():
    largest_product = 0

    for i in range(20):
        for j in range(17):
            product = 1
            for k in range(4):
                product *= grid[i][j + k]
            if product > largest_product:
                largest_product = product

    return largest_product


def up_down():
    largest_product = 0

    for i in range(17):
        for j in range(20):
            product = 1
            for k in range(4):
                product *= grid[i + k][j]
            if product > largest_product:
                largest_product = product
    return largest_product


def diagonal_left_right():
    largest_product = 0

    for i in range(17):
        for j in range(17):
            product = 1
            for k in range(4):
                product *= grid[i + k][j + k]
            if product > largest_product:
                largest_product = product
    return largest_product


def diagonal_right_left():
    largest_product = 0

    for i in range(17):
        for j in range(17):
            product = 1
            for k in range(4):
                product *= grid[i + k][19 - (j + k)]
            if product > largest_product:
                largest_product = product
    return largest_product


results = []
results.append(left_right())
results.append(up_down())
results.append(diagonal_left_right())
results.append(diagonal_right_left())
print(max(results))
