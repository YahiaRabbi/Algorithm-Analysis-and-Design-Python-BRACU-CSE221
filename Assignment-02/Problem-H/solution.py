#H - Searching is Fun

import sys
input = sys.stdin.readline
def main():

    t = int(input())
    for _ in range(t):
        k, x = map(int, input().split())
        
        low, high = 1, k * 2 
        high = k + k // (x - 1) + 2
        
        while low < high:
            mid = (low + high) // 2
            if mid - mid // x >= k:
                high = mid
            else:
                low = mid + 1
        
        print(low)


main()

"""
We search for the smallest number `low` such that 
we can reach at least `k` items considering the rule with `x`.

We maintain a search range:
- `low` = minimum possible answer
- `high` = maximum possible answer

For each `mid`:
- We check how many valid items can be formed: `mid - mid // x`
- If it is ≥ `k`, we move `high` left (try smaller answer)
- Otherwise, we move `low` right (need bigger answer)

Finally, `low` becomes the minimum valid value.


#Complexity
- Time Complexity: O(log n)
- Space Complexity: O(1)

"""