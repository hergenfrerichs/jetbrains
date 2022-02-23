import ast
script = open('import.py').read()
tree = ast.parse(script)

for i in tree.body:
    if ast.dump(i).startswith('Import') == True:
        for a in i.names:
            print(a.name)



