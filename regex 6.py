import sys

sys.setrecursionlimit(10000)


def function(my_input):  # One character
    regex, inp = my_input.split('|')
    if regex == inp:
        return True
    elif regex == '.':
        return True
    elif regex == '':
        return True
    else:
        return False


# Function with no '$' ------------------

def function_2(my_input_2):
    regex, inp = my_input_2.split('|')
    # Standard Case
    if len(regex) == 0:
        return True
    # Special Case
    if not regex.endswith('\?') and not regex.endswith('\*') and not regex.endswith('\+'):
        if len(regex) == 2 and regex.endswith('?') and len(inp) >= 0:  # o?|re
            return True
        elif len(regex) == 2 and regex.endswith('*') and len(inp) >= 0:  # o*|re
            return True
        elif len(regex) == 2 and regex.endswith('.+') and len(inp) >= 0:  # .+|aaa
            return True
    if regex == '?' and len(inp) == 0:
        return True

        # Standard Case
    elif len(regex) > 0 and len(inp) == 0:
        # elif len(regex) > 0 or len(inp) >= 0:
        return False

    # Special Cases with ?*+ -> length regex min 3 and inp min 2
    elif len(regex) > 2 and len(inp) > 1 and regex[0] != '\\' and regex[1] in ['?', '*', '+']:
        if function(f'{regex[0]}|{inp[0]}') == True and regex[1] == '?':
            return function_2(f'{regex[2:]}|{inp[1:]}')
        if function(f'{regex[0]}|{inp[0]}') == True and regex[1] == '*' and regex[2] != inp[1]:  # a*r|aar
            return function_2(f'{regex[0:]}|{inp[1:]}')
        if function(f'{regex[0]}|{inp[0]}') == True and regex[1] == '*' and regex[2] == inp[1]:  # a*r|ar
            return function_2(f'{regex[2:]}|{inp[1:]}')
        if function(f'{regex[0]}|{inp[0]}') == True and regex[1] == '+' and regex[2] != inp[1]:  # a+r|aar
            return function_2(f'{regex[0]}*{regex[2:]}|{inp[1:]}')
        if function(f'{regex[0]}|{inp[0]}') == True and regex[1] == '+' and regex[2] == inp[1]:  # a+r|ar
            return function_2(f'{regex[2:]}|{inp[1:]}')

    # Special Cases with ?*+ -> length regex min 3 and inp min 1
    elif len(regex) > 2 and len(inp) > 0 and regex[0] != '\\' and regex[1] in ['?', '*']:
        if function(f'{regex[0]}|{inp[0]}') == True and regex[1] == '*' and regex[2] != inp[0]:  # .*r|s
            return function_2(f'{regex[0:]}|{inp[1:]}')
        if function(f'{regex[0]}|{inp[0]}') == True and regex[1] == '*' and regex[2] == inp[0]:  # .*r|r
            return function_2(f'{regex[2:]}|{inp[0:]}')

        if function(f'{regex[0]}|{inp[0]}') == False and regex[1] in ['?', '*']:  # u?r|r
            return function_2(f'{regex[2:]}|{inp[0:]}')

    # Special Cases with ?*+ -> length regex min 2 and inp min 1
    elif len(regex) > 1 and len(inp) > 0 and regex[1] in ['*', '+', '?', '\\\\']:
        if function(f'{regex[0]}|{inp[0]}') == True and regex[0] != '\\' and regex[1] == '*':  # a*|aa, la*|laa
            return function_2(f'{regex[0:]}|{inp[1:]}')
        if function(f'{regex[0]}|{inp[0]}') == True and regex[0] != '\\' and regex[1] == '+':  # .+|a, l.+|la
            return function_2(f'{regex[0]}*{regex[2:]}|{inp[1:]}')

        if function(f'{regex[0]}|{inp[0]}') == False and regex[0] == '\\' and regex[1] == '+':  # \+|+
            return function_2(f'{regex[1:]}|{inp[0:]}')
        if function(f'{regex[0]}|{inp[0]}') == False and regex[0] == '\\' and regex[1] == '*':  # \*|*
            return function_2(f'{regex[1:]}|{inp[0:]}')
        if function(f'{regex[0]}|{inp[0]}') == False and regex[0] == '\\' and regex[1] == '?':  # \?|?
            return function_2(f'{regex[1:]}|{inp[0:]}')
        if function(f'{regex[0]}|{inp[0]}') == False and regex[0] == '\\\\' and regex[1] == '\\':  # \\|\
            return function_2(f'{regex[1:]}|{inp[0:]}')

        if function(f'{regex[0]}|{inp[0]}') == False and regex[0] != '\\' and regex[1] in ['+']:
            return False

    elif len(regex) > 1 and len(inp) > 0 and regex[0] == '\\' and regex[1] in ['.']:
        if function(f'{regex[0]}|{inp[0]}') == False and regex[0] == '\\' and regex[1] == '.':  # \.|.
            return function_2(f'{regex[1:]}|{inp[0:]}')


    # Standard Case = length regex > 0 and length input > 0
    elif len(regex) > 0 and len(inp) > 0:
        # Standard Case
        if function(f'{regex[0]}|{inp[0]}') == True:
            return function_2(f'{regex[1:]}|{inp[1:]}')
        else:
            return False


def function_3(my_input_3):
    regex, inp = my_input_3.split('|')
    if len(inp) == 0:
        # Special Cases
        if len(regex) == 2 and regex.endswith('?') and len(inp) == 0:
            return True
        elif len(regex) == 2 and regex.endswith('*') and len(inp) == 0:
            return True
        return False
    elif function_2(f'{regex}|{inp}'):
        return True
    else:
        # Special Cases
        if len(regex) == 2 and regex.endswith('?') and len(inp) == 1:  # b?|a
            return False
        elif len(regex) == 2 and regex.endswith('*') and len(inp) == 1:  # b*|a
            return False
        return function_3(f'{regex}|{inp[1:]}')


# Function with '$' ---------------------------
def function_5(my_input_5):
    regex, inp = my_input_5.split('|')
    # Special Case
    if not regex.endswith('\?') and not regex.endswith('\*') and not regex.endswith('\+'):
        if len(regex) == 2 and regex.endswith('?') and len(inp) == 0:
            return True
        elif len(regex) == 2 and regex.endswith('*') and len(inp) == 0:
            return True
        elif len(regex) == 2 and regex.endswith('.+') and len(inp) == 0:
            return True

    # Standard Case
    if len(regex) == 0 and len(inp) == 0:
        return True

    elif regex == '?' and len(inp) == 0:
        return True

        # Standard Case
    elif len(regex) > 0 and len(inp) == 0:
        return False
    elif len(regex) == 0 and len(inp) > 0:
        return False

    # Special Cases with ?*+ -> length regex min 3 and inp min 2
    elif len(regex) > 2 and len(inp) > 1 and regex[0] != '\\' and regex[1] in ['?', '*', '+']:
        if function(f'{regex[0]}|{inp[0]}') == True and regex[1] == '?':
            return function_2(f'{regex[2:]}|{inp[1:]}')
        if function(f'{regex[0]}|{inp[0]}') == True and regex[1] == '*' and regex[2] != inp[1]:  # a*r|aar
            return function_2(f'{regex[0:]}|{inp[1:]}')
        if function(f'{regex[0]}|{inp[0]}') == True and regex[1] == '*' and regex[2] == inp[1]:  # a*r|ar
            return function_2(f'{regex[2:]}|{inp[1:]}')
        if function(f'{regex[0]}|{inp[0]}') == True and regex[1] == '+' and regex[2] != inp[1]:  # a+r|aar
            return function_2(f'{regex[0]}*{regex[2:]}|{inp[1:]}')
        if function(f'{regex[0]}|{inp[0]}') == True and regex[1] == '+' and regex[2] == inp[1]:  # a+r|ar
            return function_2(f'{regex[2:]}|{inp[1:]}')

    # Special Cases with ?*+ -> length regex min 3 and inp min 1
    elif len(regex) > 2 and len(inp) > 0 and regex[0] != '\\' and regex[1] in ['?', '*']:
        if function(f'{regex[0]}|{inp[0]}') == True and regex[1] == '*' and regex[2] != inp[0]:  # .*r|s
            return function_2(f'{regex[0:]}|{inp[1:]}')
        if function(f'{regex[0]}|{inp[0]}') == True and regex[1] == '*' and regex[2] == inp[0]:  # .*r|r
            return function_2(f'{regex[2:]}|{inp[0:]}')

        if function(f'{regex[0]}|{inp[0]}') == False and regex[1] in ['?', '*']:  # u?r|r
            return function_2(f'{regex[2:]}|{inp[0:]}')

    elif len(regex) > 1 and len(inp) > 1 and regex[0] != '\\' and regex[1] in ['*', '+']:
        if function(f'{regex[0]}|{inp[0]}') == True and regex[0] != inp[1]:  # o+|op
            return False

    # Special Cases with ?*+ -> length regex min 2 and inp min 1
    elif len(regex) > 1 and len(inp) > 0 and regex[1] in ['*', '+', '?']:
        if function(f'{regex[0]}|{inp[0]}') == True and regex[0] != '\\' and regex[1] == '*':  # a*|aa, la*|laa
            return function_2(f'{regex[0:]}|{inp[1:]}')
        if function(f'{regex[0]}|{inp[0]}') == True and regex[0] != '\\' and regex[1] == '+':  # .+|a, l.+|la
            return function_2(f'{regex[0]}*{regex[2:]}|{inp[1:]}')

        if function(f'{regex[0]}|{inp[0]}') == False and regex[0] == '\\' and regex[1] == '+':  # \+|+
            return function_2(f'{regex[1:]}|{inp[0:]}')
        if function(f'{regex[0]}|{inp[0]}') == False and regex[0] == '\\' and regex[1] == '*':  # \*|*
            return function_2(f'{regex[1:]}|{inp[0:]}')
        if function(f'{regex[0]}|{inp[0]}') == False and regex[0] == '\\' and regex[1] == '?':  # \?|?
            return function_2(f'{regex[1:]}|{inp[0:]}')

        if function(f'{regex[0]}|{inp[0]}') == False and regex[0] != '\\' and regex[1] in ['+']:
            return False

    elif len(regex) > 1 and len(inp) > 0 and regex[0] == '\\' and regex[1] in ['.']:
        if function(f'{regex[0]}|{inp[0]}') == False and regex[0] == '\\' and regex[1] == '.':  # \.|.
            return function_2(f'{regex[1:]}|{inp[0:]}')

    # Standard Case = length regex > 0 and length input > 0
    elif len(regex) > 0 and len(inp) > 0:
        # Standard Case
        if function(f'{regex[0]}|{inp[0]}') == True:
            return function_5(f'{regex[1:]}|{inp[1:]}')
        else:
            return False


def function_6(my_input_6):
    regex, inp = my_input_6.split('|')
    if len(inp) == 0:
        # Special Cases
        if len(regex) == 2 and regex.endswith('?') and len(inp) == 0:
            return True
        elif len(regex) == 2 and regex.endswith('*') and len(inp) == 0:
            return True
        return False
    elif function_5(f'{regex}|{inp}'):
        return True
    else:
        # Special Cases
        if len(regex) == 2 and regex.endswith('?') and len(inp) == 1:  # b?|a
            return False
        elif len(regex) == 2 and regex.endswith('*') and len(inp) == 1:  # b*|a
            return False
        return function_6(f'{regex}|{inp[1:]}')


def function_4(my_input_4):
    regex, inp = my_input_4.split('|')
    if regex == '' and inp == '':
        return True
    if regex == '\\\\' and inp == '\\':
        return True
    if regex == '?' and inp == '?':
        return False
    if regex == '*' and inp == '*':
        return False
    if regex == '+' and inp == '+':
        return False
    if len(regex) > 1 and len(inp) > 0 and regex[-1] == '$' and regex[-2] != '.' and regex[-2] != inp[
        -1]:  # Workaround!!!
        return False
    if regex.startswith('^') and not regex.endswith('$'):
        return function_2(f'{regex[1:]}|{inp}')
    if not regex.startswith('^') and not regex.endswith('$'):
        return function_3(f'{regex}|{inp}')
    if regex.startswith('^') and regex.endswith('$'):
        return (function_2(f'{regex[1:len(regex) - 1]}|{inp}') and function_6(f'{regex[1:len(regex) - 1]}|{inp}'))
    if not regex.startswith('^') and regex.endswith('$'):
        return function_6(f'{regex[0:len(regex) - 1]}|{inp}')

#print(function_4(input()))
print(function_4('\\\\|\\'))  # True
print(function_4('^n.+p|noooooooope'))  # True

print(function_4('apple$|apple pie'))  # True
print(function_4('3\+3|3+3=6'))  # True
print(function_4('\?|Is this working?'))  # True
print(function_4('\\|\\'))  # True
print(function_4('colou\?r|color'))  # False
print(function_4('colou\?r|colour'))  # False

print(function_4('^.*c|abcabc'))  # True
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
print(function_4('colou?r|color'))  # True
print(function_4('colou?r|colour'))  # True
print(function_4('colou?r|colouur'))  # False
print(function_4('colou*r|color'))  # True
print(function_4('colou*r|colour'))  # True
print(function_4('colou*r|colouur'))  # True
print(function_4('colou+r|color'))  # False
print(function_4('colou+r|colour'))  # True
print(function_4('colou+r|colouur'))  # True

print(function_4('col.*r|color'))  # True
print(function_4('col.*r|colour'))  # True
print(function_4('col.*r|colr'))  # True
print(function_4('col.*r|collar'))  # True
print(function_4('col.*r$|colors'))  # False
print(function_4('.*|aaa'))  # True
print(function_4('^no*p|nooope'))  # True






    
