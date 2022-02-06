def minion_game(string):
    stuart = 0
    kevin = 0
    consonants = "b,c,d,f,g,h,j,k,l,m,n,p,r,q,s,t,v,x,w,y,z,B,C,D,F,G,H,J,K,L,M,N,P,R,Q,S,T,V,X,W,Y,Z"
    vowels = "a,e,i,o,u,A,E,I,O,U"

    for i in range(len(string)):
        if string[i] in vowels.split(","):
            kevin += len(string) - i
        if string[i] in consonants.split(","):
            stuart += len(string) - i

    if stuart > kevin:
        print("Stuart " + str(stuart))
    elif kevin > stuart:
        print("Kevin " + str(kevin))
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

##################################################################################
# s = input()
#
# vowels = 'AEIOU'
#
# kevsc = 0
# stusc = 0
# for i in range(len(s)):
#     if s[i] in vowels:
#         kevsc += (len(s) - i)
#     else:
#         stusc += (len(s) - i)
#
# if kevsc > stusc:
#     print("Kevin", kevsc)
# elif kevsc < stusc:
#     print("Stuart", stusc)
# else:
#     print("Draw")
##################################################################################

# string = input()
# vowels = "AEIOU"
# strLen = len(string)
# substringsLen = int(strLen * (strLen + 1) / 2)
# k = sum(strLen - i for i in range(strLen) if string[i] in vowels)
# # k = 0
# # for i in range(strLen):
# #     if string[i] in vowels:
# #         k = sum(strLen - i)
# s = substringsLen - k
# if s > k: print(f"Stuart {s}")
# elif s < k: print(f"Kevin {k}")
# else: print("Draw")