import itertools
import string

password = 'yg'

def hack():
    alphabet = [i for i in string.ascii_lowercase]
    numbers = [i for i in string.digits]
    alphnumb = alphabet + numbers

    for j in alphnumb:
        level = 1
        if j != alphnumb[-1]:
            yield j
        if j == alphnumb[-1]:
            level = 2
            yield j
        if level == 2:
            for h, k in itertools.product(alphnumb, alphnumb):                
                if h + k != alphnumb[-1] + alphnumb[-1]:                        
                    yield h + k
                if h + k == alphnumb[-1] + alphnumb[-1]:
                    level = 3
                    yield h + k
                if level == 3:
                    for l, m, n in itertools.product(alphnumb, alphnumb, alphnumb):                
                        if l + m + n != alphnumb[-1] + alphnumb[-1] + alphnumb[-1]:
                            yield l + m + n
                        if l + m + n == alphnumb[-1] + alphnumb[-1] + alphnumb[-1]:
                            level = 4
                        if level == 4:
                            for o, p, q, r in itertools.product(alphnumb, alphnumb, alphnumb, alphnumb):
                                yield o + p + q + r
      

hack_generator = hack()

for i in range(1000000):
    attempt = next(hack_generator)
    # print(attempt)
    if attempt == password:
        print(f'Connection success!')
        break
else:
    print('Too many attempts!')
        
    




   

