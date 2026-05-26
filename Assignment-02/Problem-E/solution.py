#E - Longest Subarray Sum
import sys
input = sys.stdin.readline
def main():

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    left = 0
    curr = 0
    ans = 0
    
    for right in range(n):
        curr += a[right]
        
        while curr > k and left <= right:
            curr -= a[left]
            left += 1
            
        if curr <= k:
            ans = max(ans, right - left + 1)
    
    print(ans)

main()

"""
#Approach

Sliding Window (Two Pointer) technique. search yt for sliding window kinda 2 pointers..
maintain a window [left, right] and keep track of the current sum.

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(1)

"""