#C - Triple The Trouble

import sys

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))  #sys.stdin.buffer.read() is used for faster input handling.
    n, x = data[0], data[1]
    a = data[2:2 + n]

    if n < 3:
        print(-1)
        return

    arr  = sorted((a[i], i + 1) for i in range(n))
    vals = [p[0] for p in arr]
    ids  = [p[1] for p in arr]

    for i in range(n - 2):
        v = vals[i]
        if v + vals[i+1] + vals[i+2] > x: break
        if v + vals[n-2] + vals[n-1] < x: continue

        l, r = i+1, n-1
        while l < r:
            s = vals[l]+vals[r]
            if   s == x - v: print(ids[i], ids[l], ids[r]); return
            elif s  < x - v: l += 1
            else:             r -= 1

    print(-1)
    

main()


"""
#Approach
First, the array is sorted while keeping track of the original indices.
For each element:
- fix one value
- use the Two Pointer Technique on the remaining part of the array

One pointer starts from the left side, and another starts from the right side.
    - If the current sum is smaller than the target,
    move the left pointer forward.

    - If the current sum is larger,
    move the right pointer backward.
    
    - If the target sum is found,
    print the original.

"""