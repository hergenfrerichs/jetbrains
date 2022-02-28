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


print(function(input()))


    
