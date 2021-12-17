scores = input().split()
count_c = 0
count_i = 0
for i in scores:
    if i == "I":
        count_i += 1
        if count_i > 2:
            print("Game over")
            print(count_c)
            break
    else:
        count_c += 1
else:
    print("You won")
    print(count_c)
