playing=True
while playing == True:
    import msvcrt
    import random
    maze=[]
    row=10
    column=10
    playerpos = [1,1]
    playerposn = playerpos.copy()
    cplayerposn = playerpos.copy()
    keycollected = False
    invalid = False
    out = False
    B = False
    turns = 0
    row+=1
    column+=1
    for _ in range(row):
        line=[]
        for _ in range(column):
            line.append(".")
        maze.append(line)
    def printmaze():
        for row in maze:
            for number in row:
                print(number, end=" ")
            print()
    def spaces():
        maze[playerposn[0]][playerposn[1]] = "."
        maze[special[0]][special[1]] = "B"
        maze[special2[0]][special2[1]] = "B"
        maze[xray[0]][xray[1]] = "X"
        maze[exit[0]][exit[1]] = "E"
        maze[cplayerposn[0]][cplayerposn[1]] = "P"
        maze[0][0] = "  "
    def otherspaces():
        maze[special[0]][special[1]] = "B"
        maze[special2[0]][special2[1]] = "B"
        maze[xray[0]][xray[1]] = "X"
        maze[exit[0]][exit[1]] = "E"
        maze[cplayerposn[0]][cplayerposn[1]] = "P"
        maze[0][0] = "  "
    def flip(a):
        return[a[1],a[0]]
    def printflip(a):
        print(f"({chr(a[1]+64)}, {a[0]})")
    
    dot = 1
    top = 65
    left = 1
    while True:
        maze[0][dot] = chr(top)
        top = top+1
        dot = dot+1
        if dot == column:
            break
    dot = 1
    while True:
        if left<10:
            maze[dot][0] = " " + str(left)
        else:
            maze[dot][0] = left
        left = left+1
        dot = dot+1
        if dot == row:
            break
    if row>2 and column>2:
        keylocation = [random.randint(round(row/3),row-2),random.randint(round(column/3),column-2)]
    else:
        keylocation = [random.randint(1,row-2),random.randint(1,column-2)]
    while True:
        special = [random.randint(1,row-1), random.randint(1,column-1)]
        if special != exit:
            break
    while True:
        special2 = [random.randint(1,round(row/4)),random.randint(1,round(column/4))]
        if special2 != special:
            break
    while True:
        xray = [random.randint(round(row/4),row-1), random.randint(round(column/4),column-1)]
        if xray != exit and xray != special and xray != special2:
            break
    exit = [row-1,column-1]
    if column>20 or row>20:
        dice = 2
        die = "dice"
    else:
        dice = 1
        die = "die"
    spaces()
    printmaze()
    running = True
    while running:  
        while True:
            print(f"roll the {die}(enter/q): ")
            confirm = msvcrt.getch().decode()
            if confirm == "\r":
                turns += 1
                roll = 0
                for _ in range(dice):
                    rand = random.randint(1,6)
                    roll = rand+roll
                if B == True:
                    print(f"roll:{roll}+{6*dice}")
                    roll = roll+6*dice
                    B = False
                print(f"roll: {roll}")
                moves = roll
                moving = True
                break
            elif confirm == "q":
                playing = False
                running = False
                moving = False
                break
            else: print("invalid input")
        while moving:
            spaces()
            print("w/a/s/d/b/q: ")
            direction = msvcrt.getch().decode()
            if direction == "w":
                playerpos[0] -= 1
            elif direction == "s":
                playerpos[0] += 1
            elif direction == "d":
                playerpos[1] += 1
            elif direction == "a":
                playerpos[1] -= 1
            elif direction == "b":
                spaces()
                printmaze()
                printflip(playerposn)
                moves = roll
                print(f"moves left: {moves}")
                playerposn = cplayerposn.copy()
                playerpos = cplayerposn.copy()
            elif direction == "q":
                moving = False
                playing = False
                running = False
            else:
                invalid = True
                moves +=1
            
            if 0<playerpos[0]<row and 0<playerpos[1]<column:
                playerposn = playerpos.copy()
            else:
                out = True
                playerpos=playerposn.copy()
                moves +=1
            if direction != "b":
                maze[playerposn[0]][playerposn[1]] = "p"
                printmaze()
                printflip(playerposn)
                if invalid == True:
                    print("invalid input")
                    invalid = False
                if out == True:
                    print("out of bounds")
                    out = False
                moves -= 1
                print(f"moves left: {moves}")
            if moves == 0:
                while True:
                    print("confirm move(enter/b/q)")
                    confirm = msvcrt.getch().decode()
                    if confirm == "\r":
                        maze[cplayerposn[0]][cplayerposn[1]] = "."
                        cplayerposn = playerposn.copy()
                        otherspaces()
                        moving = False
                        break
                    elif confirm =="b":
                        spaces()
                        printmaze()
                        moves = roll
                        print(f"moves left: {moves}")
                        playerposn = cplayerposn.copy()
                        playerpos = cplayerposn.copy()
                        break
                    elif confirm == "q":
                        running = False
                        moving = False
                        playing = False
                        break
                    else:print("invalid input")

        printmaze()
        printflip(cplayerposn)
        if cplayerposn == keylocation and keycollected == False:
            print("you got the key!\nHead to the exit")
            keycollected=True
        if cplayerposn == special:
            print(f"add {6*dice} moves to your next move")
            B = True
            special = [0,0]
        if cplayerposn == special2:
            print(f"add {6*dice} moves to your next move")
            B = True
            special2 = [0,0]
        if cplayerposn == xray:
            print("key is at",end=" ")
            printflip(keylocation)
            xray = [0,0]
            
        if cplayerposn[0] == row-1 and cplayerposn[1] == column-1:
            if keycollected == True:
                print("You win!!")
                print(f"turns taken: {turns}")
                while True:
                    print("play again? enter/q: ")
                    g = msvcrt.getch().decode()
                    if g == "\r":
                        running = False
                        break
                    elif g == "q":
                        running = False
                        playing = False
                        break
                    else:
                        print("invalid input")
            else: print("You haven't found the key yet")
