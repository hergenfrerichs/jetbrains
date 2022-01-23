n = int(input())

def squares(size):
    num = 1
    while num < size + 1:
        yield num * num
        num += 1

inf_func = squares(n)


for _ in range(n):
    print(next(inf_func))

