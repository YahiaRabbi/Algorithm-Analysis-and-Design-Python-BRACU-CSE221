#F - Longest K-Distinct Subarray

import sys
input = sys.stdin.readline
def main():

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    freq = {}
    left = 0
    ans = 0
    
    for right in range(n):
        freq[a[right]] = freq.get(a[right], 0) + 1
        
        while len(freq) > k:
            freq[a[left]] -= 1
            
            if freq[a[left]] == 0:
                del freq[a[left]]
            left += 1
            
        ans = max(ans, right-left + 1)
    
    print(ans)


main()

"""
Sliding Window (Two Pointer) technique with a frequency map.

maintain a window [left, right] and a dictionary freq to track element counts inside the window.

- Expand the window by moving `right` and updating frequency of `a[right]`
- If the number of distinct elements (`len(freq)`) exceeds `k`, shrink the window from the left
- While shrinking, decrease frequency of `a[left]` and remove it from the map if its count becomes 0
- At each step, update the maximum window size where distinct elements ≤ `k`

## Complexity
- Time Complexity: O(n)
- Space Complexity: O(k)

"""