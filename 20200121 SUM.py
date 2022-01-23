def sq_sum(*args):
    result = 0
    for arg in args:
        result += arg ** 2
    return result

def sq_sum(*numbers):
    return sum([number ** 2 for number in numbers])
    

print(sq_sum(1, 2, 2, 4))  # 25.0
print(sq_sum(1.5))         # 2.25
print(sq_sum(1, 10, 10))   # 201.0
