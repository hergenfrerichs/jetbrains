import math

print('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:''')
calc_type = input()
if calc_type == "n":
    p = float(input('Enter the loan principal:\n'))
    a = float(input('Enter the monthly payment:\n'))
    yearly_i = float(input('Enter the loan interest:\n'))
    i = yearly_i / (12 * 100)
    n = math.log(a / (a - i * p), 1 + i)
    n = math.ceil(n)
    years = n // 12
    months = n % 12
    if years != 0 and months != 0:
        print(f'It will take {years} years and {months} months to repay this loan!')
    elif years == 0 and months != 0:
        print(f'It will take {months} months to repay this loan!')
    elif years != 0 and months == 0:
        print(f'It will take {years} years to repay this loan!')
elif calc_type == "a":
    p = float(input('Enter the loan principal:\n'))
    n = int(input("Enter the number of periods:\n"))
    yearly_i = float(input('Enter the loan interest:\n'))
    i = yearly_i / (12 * 100)
    a = p * (i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)
    a = math.ceil(a)
    print(f'Your monthly payment =  {a}!')
elif calc_type == "p":
    a = float(input('Enter the annuity payment:\n'))
    n = int(input("Enter the number of periods:\n"))
    yearly_i = float(input('Enter the loan interest:\n'))
    i = yearly_i / (12 * 100)
    p = a / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
    p = round(p)
    print(f'Your loan principal = {p}!')

