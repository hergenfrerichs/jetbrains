def fibonacci1(n):
    num = 0
    num_1 = 1
    result = []
    for i in range(n):
        if i == 0:
            result.append(num)            
        elif i == 1:
            result.append(num_1)
        else:
            num_2 = num + num_1
            result.append(num_2)
            num = num_1
            num_1 = num_2
    return result

#print(fibonacci1(10))

def fibonacci2(n):
    num = 0
    num_1 = 1
    for i in range(n):
        if i == 0:
            yield num            
        elif i == 1:
            yield num_1
        else:
            num_2 = num + num_1
            yield num_2
            num = num_1
            num_1 = num_2

fibo_func2 = fibonacci2(10)
print(next(fibo_func2))
print(next(fibo_func2))
print(next(fibo_func2))
