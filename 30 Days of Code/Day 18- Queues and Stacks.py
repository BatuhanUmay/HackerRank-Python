import sys

class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, chr):
        self.stack.append(chr)

    def popCharacter(self):
        return self.stack.pop(-1) #son elemanı kaldır

    def enqueueCharacter(self, chr):
        self.queue.append(chr)

    def dequeueCharacter(self):
        return self.queue.pop(0) #ilk elemanı kaldır

    # def pushCharacter(self, ch):
    #     self.stack.append(ch)
    #
    # def enqueueCharacter(self, ch):
    #     self.queue.insert(0, ch)
    #
    # def popCharacter(self):
    #     return self.stack.pop()
    #
    # def dequeueCharacter(self):
    #     return self.queue.pop

# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")

####################################################################################

# class Solution:
#     # Write your code here
#     stop = None
#     qfront = None
#     qrear = None
#
#     def pushCharacter(self, a):
#         sptr = Node(a)
#         if (self.stop == None):
#             self.stop = sptr
#         else:
#             sptr.next = self.stop
#             self.stop = sptr
#
#     def enqueueCharacter(self, a):
#         qptr = Node(a)
#         if (self.qfront == None):
#             self.qfront = self.qrear = qptr
#         else:
#             self.qrear.next = qptr
#             self.qrear = qptr
#
#     def popCharacter(self):
#         if (self.stop != None):
#             return (self.stop.data)
#             self.stop = self.stop.next
#
#     def dequeueCharacter(self):
#         if (self.qfront != None):
#             return (self.qfront.data)
#             self.qfront = self.qfront.next
#
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
