#B. Can you solve Arithmetic Expressions?
T = int(input())

for _ in range(T):
    line = input().split()
    
    num1 = int(line[1])
    operator = line[2]
    num2 = int(line[3])
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    
    print(f"{result:.6f}")