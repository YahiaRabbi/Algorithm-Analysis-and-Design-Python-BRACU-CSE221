#G - Sorting Again??

T = int(input())
 
for _ in range(T):
    N = int(input())
    ids = list(map(int, input().split()))
    marks = list(map(int, input().split()))
    
    #ID and marks
    students = []
    for i in range(N):
        students.append([ids[i], marks[i]])
 
    swaps = 0
    for i in range(N):
        best = i
        
        for j in range(i + 1, N):
            
            if students[j][1] > students[best][1]: #High marks
                best = j
            elif students[j][1] == students[best][1]: #Same marks
                if students[j][0] < students[best][0]: #Lower ID
                    best = j
        
        if best != i:
            students[i], students[best] = students[best], students[i]
            swaps += 1
    
    #Print
    print(f"Minimum swaps: {swaps}")
    for s in students:
        print(f"ID: {s[0]} Mark: {s[1]}")