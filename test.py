def function_4(my_input_4):
    regex, inp = my_input_4.split('|')
    if regex[0] == '\\' and regex[1] in ['*', '+', '?', '.']:
        print('Ja')
    if regex[0] == inp[0]:
        print('0gleich0')
    if regex[1] == inp[0]:
        print('1=0')
        
    print(regex[0], regex[1], inp)
    print(len(regex[0]))

print(function_4('\+|+'))  # True





