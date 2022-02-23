# S001 Too long - Length of line max 79
def line_length(input_line):
    max_length = 79
    if len(input_line) > max_length:
        return 'S001 Too long'


# S002 Wrong Indentation - Indentation is not a multiple of four
def indent(input_line):
    if input_line.strip() != '':
        difference = len(list(input_line)) - len(list(input_line.lstrip()))
        if difference != 0 and difference % 4 != 0:
            return 'S002 Wrong Indentation'


# S003 Unnecessary semicolon - After a statement, if not in a comment
def semicolon(input_line):
    ls_sw = [-1, -1, -1]  # Switches for ' " #
    for letter in input_line:
        if letter == "'":
            ls_sw[0] *= -1
        elif letter == '"':
            ls_sw[1] *= -1
        elif letter == "#":
            ls_sw[2] *= -1
        elif letter == ';':
            if ls_sw[0] == -1 and ls_sw[1] == -1 and ls_sw[2] == -1:
                return 'S003 Unnecessary semicolon'


# S004 At least two spaces required before inline comments
def two_spaces(input_line):
    ind_com = input_line.find('#')
    if ind_com != -1 and ind_com != 0:
        if input_line[ind_com - 1] != ' ' or input_line[ind_com - 2] != ' ': 
            return 'S004 At least two spaces required before inline comments'


# S005 TODO found - (in comments only and case-insensitive)
def to_do(input_line):
    ind_com = input_line.find('#')
    ind_td = input_line.lower().find('todo')
    if ind_com != -1 and ind_com < ind_td:
        return 'S005 TODO found'


# S006 More than two blank lines used before this line
def blank(input_line):
    if input_line.strip() == '':
        return True
    else:
        return False
       
                  

def main(path_input):
    line_counter = 1
    empty_line_counter = 0
    with open(path_input, 'r') as my_file:
        for line in my_file:
            if line_length(line) is not None:
                print(f'Line {line_counter}: {line_length(line)}')
            if indent(line) is not None:
                print(f'Line {line_counter}: {indent(line)}')
            if semicolon(line) is not None:
                print(f'Line {line_counter}: {semicolon(line)}')
            if two_spaces(line) is not None:
                print(f'Line {line_counter}: {two_spaces(line)}')
            if to_do(line) is not None:
                print(f'Line {line_counter}: {to_do(line)}')
            if blank(line) == True:
                empty_line_counter +=1                
            else:
                if empty_line_counter > 2:
                    print(f'Line {line_counter}: S006 More than two blank lines used before this line')         
                    empty_line_counter = 0
                else:
                    empty_line_counter = 0
            line_counter += 1
    

main(input())
