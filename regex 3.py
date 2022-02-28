import sys


sys.setrecursionlimit(10000)


def function(my_input):  # One character
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


def function_2(my_input_2):  # Equal length
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


def function_3(my_input_3):  # String longer regex
    regex, inp = my_input_3.split('|')
    if len(inp) < len(regex):
        return function_2(my_input_3)
    elif len(inp) >= len(regex):
        if function_2(f'{regex}|{inp[0:len(regex)]}'):
            return True         
        else:
            # print(f'{regex}|{inp[1:len(regex) + 1]}')
            return function_3(f'{regex}|{inp[1:]}')


print(function_3(input()))


    
