def print_grid():
    a = "_________"
    
    # Print original matrix
    list_a = list(a)
    list_a = [[list_a[0], list_a[1], list_a[2]], [list_a[3], list_a[4], list_a[5]], [list_a[6], list_a[7], list_a[8]]]
    print("---------")
    print("|", " ".join(list_a[0]), "|")
    print("|", " ".join(list_a[1]), "|")
    print("|", " ".join(list_a[2]), "|")
    print("---------")

    game = True
    round = 1
    while game == True:
        if round % 2:
            player = "X"
        else:
            player = "O"
        # Perform checks on input data
        perform_checks = True
        while perform_checks == True:            
            input_data = input("Enter the coordinates: ")
            try:
                b, c = input_data.split()  
                b = int(b)
                c = int(c)
            except:
                print("You should enter numbers!")
                perform_checks = True
                continue
            if 0 < int(b) < 4 and 0 < int(c) < 4:
                if list_a[int(b)-1][int(c)-1] == "_":
                    list_a[int(b)-1][int(c)-1] = player
                    perform_checks = False
                    round +=1
                    print("---------")
                    print("|", " ".join(list_a[0]), "|")
                    print("|", " ".join(list_a[1]), "|")
                    print("|", " ".join(list_a[2]), "|")
                    print("---------")
                    if check_win(list_a):
                        game = False
                    else:
                        game = True
                else:
                    print("This cell is occupied! Choose another one!")
                    perform_checks = True
            else:
                print("Coordinates should be from 1 to 3!")
                perform_checks = True  
        

def check_win(list_to_check):
    # Check if one party won the game
    check_win = False
    win = []
    for m in ["X", "O"]:
        for n in range(0, 3):  
            if list_to_check[n][0] == list_to_check[n][1] == list_to_check[n][2] == m:
                win.append(m)
        for n in range(0, 3):  
            if list_to_check[0][n] == list_to_check[1][n] == list_to_check[2][n] == m:
                win.append(m)
        if list_to_check[0][0] == list_to_check[1][1] == list_to_check[2][2] == m:
            win.append(m)
        elif list_to_check[0][2] == list_to_check[1][1] == list_to_check[2][0] == m:
            win.append(m)

    if win != []:
        check_win = True
        print(f"{win[0]} wins")
        return check_win
    elif win == []:
        count_ = len([x for rows in list_to_check for x in rows if x == "_"])
        if count_:
            check_win = False
            return check_win
        else:
            check_win = True
            print("Draw")
            return check_win      
          

print_grid()
