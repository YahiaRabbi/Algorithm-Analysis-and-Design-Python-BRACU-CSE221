#D - A Beautiful Sorted List
import sys
input = sys.stdin.readline
def main():

    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    
    result = []
    i, j = 0, 0
    
    while i < n and j < m:
        if a[i] <= b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
            
    while i < n:
        result.append(a[i])
        i += 1
        
    while j < m:
        result.append(b[j])
        j += 1
    
    print(*result)  # * for = [1, 2, 3, 4] to 1 2 3 4


main()


"""
## Complexity
- Time Complexity: O(n + m)
- Space Complexity: O(n + m)

## Approach
This problem uses the Merge Technique (Two Pointers on Sorted Arrays).

"""