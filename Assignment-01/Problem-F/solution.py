#F - An Ancient Sorting Algorithm

N = int(input())
A = list(map(int, input().split()))
 
keep_going = True
 
while keep_going:
    keep_going = False 
    
    for i in range(N - 1):
        left = A[i]
        right = A[i + 1]
        
        both_even = (left % 2 == 0) and (right % 2 == 0)
        both_odd = (left % 2 == 1) and (right % 2 == 1)
        
        if (both_even or both_odd) and (left > right):
            A[i] = right
            A[i + 1] = left
            keep_going = True  
 
#Print 
for num in A:
    print(num, end=' ')
print()