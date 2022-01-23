import itertools
import string

def hack(password):
    alphabet = [i for i in string.ascii_lowercase]
    numbers = [str(i) for i in range(10)]
    alphnumb = alphabet + numbers
    
    for j in alphnumb:
        if j == password:
            return f'Connection success!'
        if j != password and j == alphnumb[-1]:
            for h, k in itertools.product(alphnumb, alphnumb):                
                if h + k == password:
                    return f'Connection success!'
                if h + k != password and h + k == alphnumb[-1] + alphnumb[-1]:
                    for l, m, n in itertools.product(alphnumb, alphnumb, alphnumb):                
                        if l + m + n == password:
                            return f'Connection success!'
                        if l + m + n != password and l + m + n == alphnumb[-1] + alphnumb[-1] + alphnumb[-1]:
                            for o, p, q, r in itertools.product(alphnumb, alphnumb, alphnumb, alphnumb):                
                                if o + p + q + r == password:
                                    return f'Connection success!'
    else:
        return 'Too many attempts'

print(hack('99a99'))
    







   

