# k,arr = int(input()),list(map(int, input().split()))

# myset = set(arr)

# print( ( (sum(myset)*k) - (sum(arr)) ) // (k-1) )

#############################################################
# 1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2

satir = input()
dizi = input().split()

tekNoluOdalar = set()# 1 2 3 6 5 4 8
cokNoluOdalar = set()# 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 4 3 1 5 6 2

for odaNo in dizi:
    if odaNo in tekNoluOdalar:
        cokNoluOdalar.add(odaNo)
    else:
        tekNoluOdalar.add(odaNo)

cevap = tekNoluOdalar.difference(cokNoluOdalar)
print(list(cevap)[0])

#############################################################

# K = int(input())
# rooms = input().split()

# rooms.sort()
# capt_room = (set(rooms[0::2]) ^ set(rooms[1::2]))

# print(capt_room.pop())

# I was able to do it using a list and sets. 
# What I did was sort the list of room numbers 
# and then split that list into two sets with one
# containing the even elements and the other the odd
# elements. Since the number of members in a group,
# K, will always be greater than 1 each set contained 
# the same room numbers except for the set that 
# contained the captain's room. From there I take 
# the symmetric difference of both sets to get the 
# captain's room.