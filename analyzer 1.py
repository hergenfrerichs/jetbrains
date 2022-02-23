path_input = input()
max_length = 79
line_counter = 1
Code = {'S001': 'Too long'}

with open(path_input, 'r') as my_file:
    for line in my_file:
        if len(line) > max_length:
            print(f"Line {line_counter}: S001 {Code['S001']}")
        line_counter += 1
