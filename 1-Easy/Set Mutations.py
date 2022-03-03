# .update() or |=
# Update the set by adding elements from an iterable/another set.

# >>> H = set("Hacker")
# >>> R = set("Rank")
# >>> H.update(R)
# >>> print H
# set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
# .intersection_update() or &=
# Update the set by keeping only the elements found in it and an iterable/another set.

# >>> H = set("Hacker")
# >>> R = set("Rank")
# >>> H.intersection_update(R)
# >>> print H
# set(['a', 'k'])
# .difference_update() or -=
# Update the set by removing elements found in an iterable/another set.

# >>> H = set("Hacker")
# >>> R = set("Rank")
# >>> H.difference_update(R)
# >>> print H
# set(['c', 'e', 'H', 'r'])
# .symmetric_difference_update() or ^=
# Update the set by only keeping the elements found in either set, but not in both.

# >>> H = set("Hacker")
# >>> R = set("Rank")
# >>> H.symmetric_difference_update(R)
# >>> print H
# set(['c', 'e', 'H', 'n', 'r', 'R'])
#############################################################

_ = int(input())
s1 = set(map(int, input().split()))
N = int(input())

for _ in range(N):
    secim, _ = input().split() 
    s2 = set(map(int, input().split()))

    if(secim == "intersection_update"):
        s1.intersection_update(s2)
    elif(secim == "update"):
        s1.update(s2)
    elif(secim == "symmetric_difference_update"):
        s1.symmetric_difference_update(s2)
    elif(secim == "difference_update"):
        s1.difference_update(s2)

print(sum(s1))

