import ast
import re


def arg_snake_case (file_name_abs):
    result_dict = {}
    result_mut = {}
    result_dict_2 = {}
    with open(file_name_abs, 'r') as my_file:
        script = my_file.read()
        #print(script)
        try:
            tree = ast.parse(script)
            print(ast.dump(tree))
            for node in ast.walk(tree):
                list_var = []
                list_mut = []
                list_var_2 = []
                print(node)
                if isinstance(node, ast.FunctionDef):
                    function_name = node.name                    
                    print(function_name)
                    # check whether the function's name is written in camel_case
                    my_args = [a.arg for a in node.args.args]
                    defaults = [str(d) for d in node.args.defaults]
                    print(my_args)
                    print(defaults)
                    for each_arg in my_args:                    
                        print(each_arg)
                        template = r'_{,2}[a-z][a-z0-9]*_?[a-z0-9]*_?[a-z0-9]*_{,2}'
                        check_snake_case = re.match(template, each_arg)
                        if check_snake_case is None:
                            #print(arg)
                            list_var.append(each_arg)
                            result_dict[function_name] = list_var
                    for a, d in zip(my_args, defaults):
                        ind_list = d.find('List')
                        if ind_list != -1:
                            list_mut.append(a)
                            result_mut[function_name] = list_mut
                         # print(result_mut)
                    body_name = node.body
                    for node_2 in body_name:
                        # print(node_2)
                        if isinstance(node_2, ast.Assign):
                            target = node_2.targets
                            print('Target', target)
                        if isinstance(node_2, ast.Attribute):
                            for a in ast.Attribute:
                                print(a)

                            
                           
                            
                       
                            
                    

                                                               

        except:
            pass
        return result_dict, result_mut, result_dict_2

arg_snake_case(r'C:\Users\Hergen\PycharmProjects\Github\test\Code_5.py')
