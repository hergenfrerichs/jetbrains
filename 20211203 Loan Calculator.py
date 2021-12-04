import math

loan_principal = float(input('Enter the loan principal:\n'))
print('''What do you want to calculate?
type "m" - for number of monthly payments,
type "p" - for the monthly payment:''')
payment_type = input()
if payment_type == "m":
    monthly_payment = float(input('Enter the monthly payment:\n'))
    if math.ceil(loan_principal / monthly_payment) == 1:
        print("\nIt will take 1 month to repay the loan")
    else:
        print("\nIt will take", math.ceil(loan_principal / monthly_payment), "months to repay the loan")
elif payment_type == "p":
    number_months = int(input("Enter the number of months:\n"))
    monthly_payment = math.ceil(loan_principal / number_months)
    if number_months * monthly_payment > loan_principal:
        last_payment = loan_principal - (number_months - 1) * monthly_payment
        print("\nYour monthly payment =", monthly_payment, "and the last payment = {}.".format(last_payment))
    else:
        print("\nYour monthly payment =", monthly_payment)
