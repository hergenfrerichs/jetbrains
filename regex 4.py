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


def function_3(my_input_3, mark_hat, mark_dollar):  # String longer regex
    regex, inp = my_input_3.split('|')
    # print(regex)
    if len(inp) < len(regex):
        return function_2(my_input_3)
    elif len(inp) == len(regex):  # if end is equal no matter if $ or not
        if function_2(f'{regex}|{inp[0:len(regex)]}'):  
            return True
        return False
    elif len(inp) > len(regex):
        if function_2(f'{regex}|{inp[0:len(regex)]}') and mark_dollar == False:  # if equal in between
            return True         
        else:
            if mark_hat:  # False beginning (so we never enter the recursion)
                return False            
            else:
                return function_3(f'{regex}|{inp[1:]}', mark_hat, mark_dollar)
    

def function_4(my_input_4):  # Regex starts with '^' or ends with '$'
    regex, inp = my_input_4.split('|')
    if regex.rstrip('$').lstrip('^') == inp:  # Immediate end if regex fully equal to string
        return True
    elif regex.startswith('^') and regex.endswith('$'):        
        regex_check = regex.rstrip('$').lstrip('^')        
        if inp.startswith(regex_check) and inp.endswith(regex_check):
            return True  # immediate end if string starts with and ends with same string
        else:
            return function_3(f'{regex[1:len(regex)-1]}|{inp}', True, True)
    elif regex.startswith('^') and not regex.endswith('$'):
        return function_3(f'{regex[1:]}|{inp}', True, False)
    elif not regex.startswith('^') and regex.endswith('$'):
        return function_3(f'{regex[:len(regex)-1]}|{inp}', False, True)
    return function_3(f'{regex}|{inp}', False, False)


# print(function_4(input()))

print(function_4('^app|apple'))  # True
print(function_4('le$|apple'))  # True
print(function_4('^a|apple'))  # True
print(function_4('.$|apple'))  # True
print(function_4('apple$|tasty apple'))  # True
print(function_4('^apple|apple pie'))  # True
print(function_4('^apple$|apple'))  # True
print(function_4('^apple$|tasty apple'))  # False
print(function_4('^apple$|apple pie'))  # False
print(function_4('app$|apple'))  # False
print(function_4('^le|apple'))  # False
print(function_4('^apple$|applepeachapple'))  # True


    
