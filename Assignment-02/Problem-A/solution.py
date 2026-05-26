#A. Two Sum Trouble

import sys
input = sys.stdin.readline

def main():

    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    left, right = 0, n - 1   #two pointer method (one from left one right)

    while left < right:
        total = a[left] + a[right]

        if total == s:
            print(left + 1, right + 1)
            return

        elif total < s:
            left += 1

        else:
            right -= 1


    print(-1)

main()

"""
## Complexity
    - Time Complexity: O(n)
    - Space Complexity: O(1)

"""