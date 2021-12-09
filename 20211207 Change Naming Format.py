import string
str_input = input()
str_output = ""
for i in str_input:
    if i in string.ascii_uppercase:
        i = "_" + i.lower()
    str_output += i

if str_output[0] == "_":
    str_output = str_output[1:]

print(str_output)
