score = int(input())
maximum = int(input())
grade = "F"
low_a = 0.9
low_b = 0.8
low_c = 0.7
low_d = 0.6

if score / maximum >= low_d:
    grade = "D"
if score / maximum >= low_c:
    grade = "C"
if score / maximum >= low_b:
    grade = "B"
if score / maximum >= low_a:
    grade = "A"

print(grade)
