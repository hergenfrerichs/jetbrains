def print_grid():
    a = input("Enter cells: ")
    
    # Print original matrix
    list_a = list(a)
    list_a = [[list_a[0], list_a[1], list_a[2]], [list_a[3], list_a[4], list_a[5]], [list_a[6], list_a[7], list_a[8]]]
    print("---------")
    print("|", " ".join(list_a[0]), "|")
    print("|", " ".join(list_a[1]), "|")
    print("|", " ".join(list_a[2]), "|")
    print("---------")
    # Perform checks
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
                list_a[int(b)-1][int(c)-1] = "X"
                perform_checks = False
                print("---------")
                print("|", " ".join(list_a[0]), "|")
                print("|", " ".join(list_a[1]), "|")
                print("|", " ".join(list_a[2]), "|")
                print("---------")
                return list_a                
            else:
                print("This cell is occupied! Choose another one!")
                perform_checks = True
               
        else:
            print("Coordinates should be from 1 to 3!")
            perform_checks = True  
        

def check_win(list_to_check):    
    # Check if there are impossible constellations
    check_count = True
    count_x = len([x for x in list_to_check if x == "X"])
    count_o = len([x for x in list_to_check if x == "O"])
    count_ = len([x for x in list_to_check if x == "_"])
    if abs(count_x - count_o) > 1:
        check_count = False
        print("Impossible")

    # Check if one party won the game
    check_win = False
    win = []
    for m in ["X", "O"]:
        for n in range(0, 7, 3):  
            if list_to_check[n] == list_to_check[n + 1] == list_to_check[n + 2] == m:
                win.append(m)
        for n in range(0, 3):  
            if list_to_check[n] == list_to_check[n + 3] == list_to_check[n + 6] == m:
                win.append(m)
        if list_to_check[0] == list_to_check[4] == list_to_check[8] == m:
            win.append(m)
        elif list_to_check[2] == list_to_check[4] == list_to_check[6] == m:
            win.append(m)
            
    if "X" in win and "O" in win and check_count == True:
        print("Impossible")
    elif win != [] and check_count == True:
        check_win = True
        print(f"{win[0]} wins")
    elif win == [] and "_" in list_to_check and check_count == True:
        print("Game not finished")
    elif win == [] and "_" not in list_to_check and check_count == True:
        print("Draw")


print_grid()
# print_grid("_XXOO_OX_", 1, 1)
#print_grid("_XXOO_OX_")
#print_grid("_XXOO_OX_")
#print_grid("_XXOO_OX_")
#print_grid("_XXOO_OX_")
#print_grid("_XXOO_OX_")

#check_win(print_grid())
#check_win(print_grid("XXXOO__O_"))  # X wins
#check_win(print_grid("XOXOXOXXO"))  # X wins
#check_win(print_grid("XOOOXOXXO"))  # O wins
#check_win(print_grid("XOXOOXXXO"))  # Draw
#check_win(print_grid("XO_OOX_X_"))  # Game not finished
#check_win(print_grid("XO_XO_XOX"))  # Impossible
#check_win(print_grid("_O_X__X_X"))  # Impossible
#check_win(print_grid("_OOOO_X_X"))  # Impossible
