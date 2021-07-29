# using recursive 

def fibonacci(n):
    if(n<0):
        return "sorry"
    if(n == 0):
        return n
    if(n == 1):
        return n        
    else:
        return fibonacci(n -1) + fibonacci(n-2)

print(fibonacci(7))


def fibonacci(n):
    num1 = 0
    num2 = 1
    for i in range(0, n):
        temp = num1
        num1 = num2
        num2 = temp + num2
    return num1
        

print(fibonacci(7))      