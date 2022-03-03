# if __name__ == '__main__':    
#     sozluk = {}
#     for _ in range(0, int(input())):   
#         name = input()
#         score = float(input())
        
#         sozluk[name] = score
        
#     degerler = sozluk.values()
    
#     ikinci = sorted(list(set(degerler)))[1]

#     ikinciEnKucuk = []

#     for key, value in sozluk.items():
#         if value == ikinci:
#             ikinciEnKucuk.append(key)  

#     ikinciEnKucuk.sort()
        
#     for isim in ikinciEnKucuk:
#         print(isim)
        
####################################################

l = []
second_lowest_names = []
scores = set()

for _ in range(int(input())):
    name = input()
    score = float(input())
    l.append([name, score])
    scores.add(score)
        
second_lowest = sorted(scores)[1]

for name, score in l:
    if score == second_lowest:
        second_lowest_names.append(name)

for name in sorted(second_lowest_names):
    print(name, end='\n')