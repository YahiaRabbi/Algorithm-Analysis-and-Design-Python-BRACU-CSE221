#B - Two Sum Revisited
import sys
input = sys.stdin.readline

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    l, r = 0, m - 1
    best_diff = float('inf')
    best_i, best_j = 0, 0
    
    while l < n and r >= 0:
        total = a[l] + b[r]
        diff = abs(total - k)
        
        
        if diff < best_diff:
            best_diff = diff
            best_i, best_j = l, r
            
        if total < k:
            l += 1
            
        elif total > k:
            r -= 1
            
        else:
            break
    
    print(best_i + 1, best_j + 1)

main()


"""
#Approach
Used the Two Pointer Technique on two sorted arrays.

 - One pointer starts from the beginning of array A,
 - and another starts from the end of array B.

At each step:
- calculate the current sum
- update the best pair if needed
- move pointers depending on whether the sum is smaller or larger than k

"""

"""
#Complexity
- Time Complexity: O(n+m)
- Space Complexity: O(1)
"""