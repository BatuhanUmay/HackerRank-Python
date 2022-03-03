if __name__ == '__main__':
    n = int(input())
    integer_list = input().split()

    for i in range(len(integer_list)):
        integer_list[i] = int(integer_list[i])

    t = tuple(integer_list)
    print(hash(t))
