n = int(input())
# nameAndNumbers = [input().split() for _ in range(n)]
# phoneBook = {key: value for key, value in nameAndNumbers}
phoneBook = dict(input().split() for _ in range(n))
while True:
    try:
        name = input()
        if name in phoneBook:
            print("{}={}".format(name, phoneBook[name]))
        else:
            print("Not found")
    except:
        break

####################################################################################

# n = int(input())
# phonebook = {}
#
# for i in range(n):
#     line = input()
#     pair = line.split()
#     phonebook[pair[0]] = pair[1]
#
# while True:
#     try:
#         name = input()
#     except EOFError as e:
#         break
#     if name not in phonebook.keys():
#         print("Not found")
#     else:
#         print(f"{name}={phonebook[name]}")