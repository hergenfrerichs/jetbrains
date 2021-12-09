import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')
parser.add_argument('--payment')

args = parser.parse_args()

input_par = [args.type, args.principal, args.periods, args.interest, args.payment]
checks = 0  # if zero parameters fine, else no calculation
count_1 = 0
count_2 = 0

for x in input_par:  # at least four parameters
    if x is None:
        count_1 += 1
if count_1 > 1:
    checks = 1

for x in input_par[1:]:  # no negative parameters
    if x is not None:
        if float(x) < 0:
            count_2 += 1
if count_2 > 0:
    checks = 1

if args.interest is None:  # no interest rate
    checks = 1

if checks == 1:
    print('Incorrect parameters')

# print(f"The input parameters you provided are: {input_par}")
if checks == 0:
    if args.type != "diff" and args.type != "annuity":
        print('Incorrect parameters')

    if args.type == "diff" and args.payment is None:
        p = int(args.principal)
        n = int(args.periods)
        yearly_i = float(args.interest)
        i = yearly_i / (12 * 100)
        d = float
        sum_d = 0
        for counter in range(1, n + 1):
            d = math.ceil(p / n + i * (p - p * (counter - 1) / n))
            sum_d += d
            print(f'Month {counter}: payment is {d}')
        print(f'\nOverpayment = {sum_d - p}')
    elif args.type == "diff" and args.payment is not None:
        print("Incorrect parameters")
    elif args.type == "annuity" and args.principal is None:
        a = int(args.payment)
        n = int(args.periods)
        yearly_i = float(args.interest)
        i = yearly_i / (12 * 100)
        p = a / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
        p = math.floor(p)
        print(f'Your loan principal = {p}!')
        print(f'Overpayment = {n * a - p}')
    elif args.type == "annuity" and args.periods is None:
        p = int(args.principal)
        a = int(args.payment)
        yearly_i = float(args.interest)
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
        print(f'Overpayment = {n * a - p}')
    elif args.type == "annuity" and args.payment is None:
        p = int(args.principal)
        n = int(args.periods)
        yearly_i = float(args.interest)
        i = yearly_i / (12 * 100)
        a = p * (i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)
        a = math.ceil(a)
        print(f'Your annuity payment = {a}!')
        print(f'Overpayment = {n * a - p}')
    else:
        print('Incorrect parameters')
