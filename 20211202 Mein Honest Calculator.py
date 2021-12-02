msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)\n"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)\n"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)\n"
msg_index = (msg_10, msg_11, msg_12)

def is_one_digit(v):
    if -10 < float(v) < 10 and float(v) // 1 == float(v):
        output = True
        return output
    else:
        output = False
        return output

def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) == True and is_one_digit(v2) == True:
        msg = msg + msg_6
    if (float(v1) == 1 or float(v2) == 1) and v3 ==  "*":
        msg = msg + msg_7
    if (float(v1) ==  0 or float(v2) ==  0) and (v3 ==  "*" or v3 ==  "+" or v3 ==  "-"):
        msg = msg + msg_8
    if msg !="":
        msg = msg_9 + msg
        print(msg)

condition = False
result = float
memory = float
memory = 0
while condition == False:
    condition_2 = False
    condition_3 = False
    print(msg_0)
    calc = input()
    comp = calc.split()
    x = comp[0]
    oper = comp[1]
    y = comp[2]
    if x == "M":
        x = memory
    if y == "M":
        y = memory
    condition = True
    try:
        tmp_1 = float(x)
        tmp_2 = float(y)
    except:
        print(msg_1)
        condition = False
    if oper not in ("+", "-", "*", "/") and condition == True:
        print(msg_2)
        condition = False
    else:
        if condition == True:
            check(x, y, oper)
            if oper =="+":
                result = float(x) + float(y)
            elif oper == "-":
                result = float(x) - float(y)
            elif oper == "*":
                result = float(x) * float(y)
            elif oper == "/" and float(y) != 0:
                result = float(x) / float(y)
            elif float(y) == 0:
                print(msg_3)
                condition = False
    if condition == True:
        print(result)
        while condition_2 == False:
            print(msg_4)
            answer = input()
            if answer == "y":
                if is_one_digit(result) == True:
                    msg_counter = 0
                    while answer == "y" and msg_counter < 3:
                        answer = input(msg_index[msg_counter],)
                        msg_counter += 1
                    if answer == "y":
                        memory = result
                if is_one_digit(result) == False:
                    memory = result
                condition_2 = True
            elif answer == "n":
                memory = 0
                condition_2 = True
            elif answer != "y" and answer != "n":
                condition_2 = False
            if condition == True and condition_2 == True:
                while condition_3 == False:
                    print(msg_5)
                    answer = input()
                    if answer == "y":
                        condition = False
                        condition_3 = True
                    elif answer == "n":
                        condition_3 = True
                    elif answer != "y" and answer != "n":
                        condition_3 = False
