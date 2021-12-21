prime_numbers = []
lower_limit = 2
upper_limit = 1000

for n in range(lower_limit, upper_limit + 1):
    if all([n % x for x in range(lower_limit, n - 1)]):        
        prime_numbers.append(n)
   
print(prime_numbers)
