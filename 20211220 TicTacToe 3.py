def print_grid():
    a = input("Enter cells: ")
    list_a = list(a)
    print("---------")
    print("|", list_a[0], list_a[1], list_a[2], "|")
    print("|", list_a[3], list_a[4], list_a[5], "|")
    print("|", list_a[6], list_a[7], list_a[8], "|")
    print("---------")
    return list_a

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

check_win(print_grid())
#check_win(print_grid("XXXOO__O_"))  # X wins
#check_win(print_grid("XOXOXOXXO"))  # X wins
#check_win(print_grid("XOOOXOXXO"))  # O wins
#check_win(print_grid("XOXOOXXXO"))  # Draw
#check_win(print_grid("XO_OOX_X_"))  # Game not finished
#check_win(print_grid("XO_XO_XOX"))  # Impossible
#check_win(print_grid("_O_X__X_X"))  # Impossible
#check_win(print_grid("_OOOO_X_X"))  # Impossible
