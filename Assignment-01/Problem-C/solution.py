#C. Fast Sum

T = int(input())

for _ in range(T):
    N = int(input())
    sum_result = N * (N + 1) // 2
    
    print(sum_result)