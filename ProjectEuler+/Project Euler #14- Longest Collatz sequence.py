# from time import time
# from array import array

MAX = int(5 * 1e6)
ans = [0]
# steps = array('i',[0])*(MAX+1)
steps = [0] * (MAX + 1)


# t0 = time()
# finding the number of steps required to reach 1 for number N while saving every intermediate result in steps(list)
# for faster computation it uses recursion and memoization
def solve(N):
    if N < MAX + 1:
        if steps[N] != 0:
            return steps[N]
    if N == 1:
        return 0
    else:
        if N % 2 != 0:
            result = 1 + solve(3 * N + 1)  # This is recursion
        else:
            result = 1 + solve(N >> 1)  # This is recursion
        if N < MAX + 1:
            steps[N] = result  # This is memoization
        return result


# Taking inputs as list and finding maximum value from inputs
inputs = [int(input()) for _ in range(int(input()))]
largest = max(inputs)
# finding answers for only largest input from list of inputs.
# why? because this way you will calculate answers for all smaller inputs as well in o(largest+1)
mx = 0
collatz = 1
for i in range(1, largest + 1):
    curr_count = solve(i)
    if curr_count >= mx:  # This is comparing steps required for current value of i and mx
        mx = curr_count
        collatz = i
    ans.append(collatz)
# printing answers from ans(list of answers) lookup.
for _ in inputs:
    print(ans[_])
# elapsed = time()-t0
# print('[%0.8fs]'%elapsed)
