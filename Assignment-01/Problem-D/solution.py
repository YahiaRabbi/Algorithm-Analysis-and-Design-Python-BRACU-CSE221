#D. Is Sorted?
T = int(input())
 
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    non_decreasing = True
    
    for i in range(N - 1):
        if arr[i] > arr[i + 1]:
            non_decreasing = False
            break
    
    if non_decreasing:
        print("YES")
    else:
        print("NO")