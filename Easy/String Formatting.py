# def print_formatted(number):
    
#     for i in range(1,number+1):
#         print("{:}\t{:o}\t{:X}\t{:b}".format(i,i,i,i))
#         # print(i,"\t",oct(i),"\t",hex(i),"\t",bin(i))

def print_formatted(n):
    for i in range(1,n + 1):
        bosluk = n.bit_length()
        print(f"{i:{bosluk}d} {i:{bosluk}o} {i:{bosluk}X} {i:{bosluk}b}")



if __name__ == '__main__':
    n = int(input())
    print_formatted(n)