def function(my_input):
    regex, inp = my_input.split('|')
    # print(regex, input)
    if regex == inp:
        return True
    elif regex == '.':
        return True
    elif regex == '':
        return True
    else:
        return False


def function_2(my_input_2):
    regex, inp = my_input_2.split('|')
    if len(regex) == 0:
        return True
    elif len(regex) > 0 and len(inp) == 0:
        return False
    elif len(regex) > 0 and len(inp) > 0:
        if function(f'{regex[0]}|{inp[0]}') == True:
            return function_2(f'{regex[1:]}|{inp[1:]}')
        else:
            return False


print(function_2(input()))


    
