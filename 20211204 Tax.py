income = int(input())
upper_threshold_1 = 15527
upper_threshold_2 = 42707
upper_threshold_3 = 132406
tax_1 = 0
tax_2 = 15
tax_3 = 25
tax_4 = 28
if income > upper_threshold_3:
    calculated_tax = income * tax_4 / 100
    percent = tax_4
if income <= upper_threshold_3:
    calculated_tax = income * tax_3 / 100
    percent = tax_3
if income <= upper_threshold_2:
    calculated_tax = income * tax_2 / 100
    percent = tax_2
if income <= upper_threshold_1:
    calculated_tax = 0
    percent = tax_1

print(f'The tax for {income} is {percent}%. That is {calculated_tax:.0f} dollars!')
