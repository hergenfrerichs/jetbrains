result = []
while True:
    input_number = input()
    if input_number == '.':
        average = sum(result) / len(result)
        print(average)
        break
    else:
        result.append(int(input_number))

    
