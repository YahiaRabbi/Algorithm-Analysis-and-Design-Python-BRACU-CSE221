#G - Count the Numbers

import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right   #bisect is built in module of binary search, 
                                              # just remember this shortcut for lab
 
def main():

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    
    for _ in range(q):
        x, y = map(int, input().split())
        print(bisect_right(a, y) - bisect_left(a, x))
 
main()

"""
It works in O(log n) time.
## Complexity

- Time Complexity: O(q log n)
- Space Complexity: O(1) 

"""