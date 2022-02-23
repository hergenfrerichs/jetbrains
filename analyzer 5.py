import ast
import argparse
import os
import re

# S001 Too long - Length of line max 79
def line_length(input_line):
    max_length = 79
    if len(input_line) > max_length:
        return 'S001 Too long'


# S002 Wrong Indentation - Indentation is not a multiple of four
def indent(input_line):
    if input_line.strip() != '':
        difference = len(input_line) - len(input_line.lstrip())
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


# S007 Too many spaces after construction_name (def or class)
def one_space(input_line):
    ind_class = input_line.find('class')
    if ind_class != -1:
        template = 'class \w'
        check_blanks = re.match(template, input_line)
        if check_blanks is None:
            return "S007 Too many spaces after 'class'"
    ind_def = input_line.find('def')
    if ind_def != -1:
        template = ' *def \w'
        check_blanks = re.match(template, input_line)
        if check_blanks is None:
            return "S007 Too many spaces after 'def'"


# S008 Class name class_name should be written in CamelCase
# \([A-Z][a-z0-9]+[A-Z]?[a-z0-9]+\):
def camel_case (input_line):
    ind_class = input_line.find('class')
    if ind_class != -1:
        template = r'class +[A-Z][a-z0-9]+[A-Z]?[a-z0-9]*\(?[A-Z]?[a-z0-9]*[A-Z]?[a-z0-9]*\)?:'
        check_camel_case = re.match(template, input_line)
        if check_camel_case is None:
            class_name = input_line.split()
            return f"S008 Class name '{class_name[-1][:-1]}' should use CamelCase"


# S009 Function name function_name should be written in snake_case
def snake_case (input_line):
    ind_def = input_line.find('def')
    if ind_def != -1:
        template = r' *def +_{,2}[a-z][a-z0-9]*_?[a-z0-9]*_?[a-z0-9]*_{,2}'
        check_snake_case = re.match(template, input_line)
        if check_snake_case is None:
            def_name = input_line.strip().split('(')
            # print(def_name)     
            return f"S009 Function name '{def_name[0][4:]}' should use snake_case"


# S010 S011 S012
def arg_snake_case (file_name):
    result_dict = {}
    result_mut = {}
    result_dict_2 = {}
    if os.path.isabs(file_name) == False:  # Checks absolute/relative file reference
        file_name_abs = f'{os.getcwd()}\\{file_name}'
    else:
        file_name_abs = file_name
    with open(file_name_abs, 'r') as my_file:
        script = my_file.read()
        try:
            tree = ast.parse(script) 
            for node in ast.walk(tree):
                list_var = []
                list_mut = []
                list_var_2 = []
                if isinstance(node, ast.FunctionDef):
                    function_name = node.name         
                    args = [a.arg for a in node.args.args]
                    defaults = [str(d) for d in node.args.defaults]                   
                    for arg in args:                    
                        template = r'_{,2}[a-z][a-z0-9]*_?[a-z0-9]*_?[a-z0-9]*_{,2}'
                        check_snake_case = re.match(template, arg)
                        if check_snake_case is None:                            
                            list_var.append(arg)
                            result_dict[function_name] = list_var                            
                    for a, d in zip(args, defaults):
                        ind_list = d.find('List')
                        if ind_list != -1:
                            list_mut.append(a)
                            result_mut[function_name] = list_mut                    
                    body_name = node.body
                    for node_2 in body_name:                        
                        if isinstance(node_2, ast.Assign):
                            target = node_2.targets
                            try:
                                var = [v.id for v in target]                                
                                for v in var:
                                    template = r'_{,2}[a-z][a-z0-9]*_?[a-z0-9]*_?[a-z0-9]*_{,2}'
                                    check_snake_case = re.match(template, v)
                                    if check_snake_case is None:                                    
                                        list_var_2.append(v)
                                        result_dict_2[function_name] = list_var_2
                            except:
                                pass
        except:
            pass
        return result_dict, result_mut, result_dict_2


# Print S010 and S012
def print_s010(file_name, input_line):
    print_list = []
    ind_def = input_line.find('def')
    if ind_def != -1:
        function_names = arg_snake_case(file_name)        
        for key, value in function_names[0].items():
            if input_line.find(key) != -1:
                for v in value:
                    print_list.append(f"S010 Argument name '{v}' should be snake_case")
    if ind_def == -1:
        function_names = arg_snake_case(file_name)
        for value in function_names[2].values():            
            if input_line.lstrip().startswith(f'{value[0]} '):
                print_list.append(f"S011 Variable '{value[0]}' in function should be snake_case")
    if ind_def != -1:
        function_names = arg_snake_case(file_name)        
        for key, value in function_names[1].items():
            if input_line.find(key) != -1:
                for v in value:
                    print_list.append(f"S012 Default argument value is mutable")
    return print_list
      
            
def one_file(file_name):
    line_counter = 1
    empty_line_counter = 0
    if os.path.isabs(file_name) == False:  # Checks absolute/relative file reference
        file_name_abs = f'{os.getcwd()}\\{file_name}'
    else:
        file_name_abs = file_name
    with open(file_name_abs, 'r') as my_file:
        for line in my_file:
            if line_length(line) is not None:
                print(f'{file_name}: Line {line_counter}: {line_length(line)}')
            if indent(line) is not None:
                print(f'{file_name}: Line {line_counter}: {indent(line)}')
            if semicolon(line) is not None:
                print(f'{file_name}: Line {line_counter}: {semicolon(line)}')
            if two_spaces(line) is not None:
                print(f'{file_name}: Line {line_counter}: {two_spaces(line)}')
            if to_do(line) is not None:
                print(f'{file_name}: Line {line_counter}: {to_do(line)}')
            if blank(line) == True:
                empty_line_counter +=1                
            else:
                if empty_line_counter > 2:
                    print(f'{file_name}: Line {line_counter}: S006 More than two blank lines used before this line')         
                    empty_line_counter = 0
                else:
                    empty_line_counter = 0
            if one_space(line) is not None:
                print(f'{file_name}: Line {line_counter}: {one_space(line)}')
            if camel_case(line) is not None:
                print(f'{file_name}: Line {line_counter}: {camel_case(line)}')
            if snake_case(line) is not None:
                print(f'{file_name}: Line {line_counter}: {snake_case(line)}')
            if print_s010(file_name, line) is not None:
                for i in print_s010(file_name, line):
                    print(f'{file_name}: Line {line_counter}: {i}')
            line_counter += 1           
                 

def files_in_dir(dir_name):
    if os.path.isabs(dir_name) == False:
        dir_name_abs = f'{os.getcwd()}\\{dir_name}'
    else:
        dir_name_abs = f'{dir_name}\\' 
    files_in_dir = os.listdir(dir_name_abs)
    for file in sorted(files_in_dir):
        one_file(f'{dir_name_abs}{file}')                  

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path_input")
    args = parser.parse_args()
    if os.path.isfile(args.path_input):
        one_file(args.path_input)
        # arg_snake_case(args.path_input)
    if os.path.isdir(args.path_input):
        files_in_dir(args.path_input)
            
    
main()
