#E. Reverse Sorting

N = int(input())
A = list(map(int, input().split()))
 
operations = []
for _ in range(1000):
    changed = False
    for i in range(N - 2):
        if A[i] > A[i + 2]:
            A[i], A[i + 2] = A[i + 2], A[i]
            operations.append((i + 1, i + 3))
            changed = True
    
    if not changed:
        break
 
sorted_check = True
for i in range(N - 1):
    if A[i] > A[i + 1]:
        sorted_check = False
        break
 
if sorted_check:
    print("YES")
    print(len(operations))
    for op in operations:
        print(op[0], op[1])
else:
    print("NO")