from random import randrange
board = {1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}
move = ()
def display_board():
    print(f"     |     |    ")
    print(f"     |     |     ")
    print(f"  " + board[1] + "  |  " + board[2] + "  |  " + board[3] + "  ")
    print(f"     |     |     ")
    print(f"_____|_____|_____")
    print(f"     |     |     ")
    print(f"     |     |     ")
    print(f"  " + board[4] + "  |  " + board[5]  +"  |  " + board[6] + "  ")
    print(f"     |     |     ")
    print(f"_____|_____|_____")
    print(f"     |     |     ")
    print(f"     |     |     ")
    print(f"  " + board[7] + "  |  " + board[8] + "  |  " + board[9] + "  ")
    print(f"     |     |     ")
    print(f"     |     |     ")
#global control
control = True


        
def draw_move():
    for i in range(1):
        cmove = int(randrange(1, 9))
        if board[cmove] != "x" and board[cmove] != "o":
            board[cmove] = "o"
            display_board()
            enter_move()
        else:
            draw_move()
        
def draw():
    global control
    for value in board:
        if value == str():
            print("It's a draw!")
            control = False
            return control
        
            
def loss_dis():
    global control
    print("You Lost this round.")
    control = False
    return control
     

def loss():
    if board[1] == "o" and board[2] == "o" and board[3] == "o":
        loss_dis()
    elif board[4] == "o" and board[5] == "o" and board[6] == "o":
        loss_dis()
    elif board[7] == "o" and board[8] == "o" and board[9] == "o":
        loss_dis()
    elif board[7] == "o" and board[5] == "o" and board[3] == "o":
        loss_dis()
    elif board[1] == "o" and board[5] == "o" and board[9] == "o":
        loss_dis()
    elif board[1] == "o" and board[4] == "o" and board[7] == "o":
        loss_dis()
    elif board[2] == "o" and board[5] == "o" and board[8] == "o":
        loss_dis()
    elif board[3] == "o" and board[6] == "o" and board[9] == "o":
        loss_dis()
    

def win_dis():
    global control
    print("You Win!!")
    control = False
    return control
    

def win():
    if board[1] == "x" and board[2] == "x" and board[3] == "x":
        win_dis()
    elif board[4] == "x" and board[5] == "x" and board[6] == "x":
        win_dis()
    elif board[7] == "x" and board[8] == "x" and board[9] == "x":
        win_dis()
    elif board[7] == "x" and board[5] == "x" and board[3] == "x":
        win_dis()
    elif board[1] == "x" and board[5] == "x" and board[9] == "x":
        win_dis()
    elif board[1] == "x" and board[4] == "x" and board[7] == "x":
        win_dis()
    elif board[2] == "x" and board[5] == "x" and board[8] == "x":
        win_dis()
    elif board[3] == "x" and board[6] == "x" and board[9] == "x":
        win_dis()
    
    

def enter_move():
    global control
    
    win()
    loss()
    draw()

    while control:
        move = int(input("Where would you like to place your X?"))
        if board[move] != "x" and board[move] != "o":
           board[move] = "x"
        else:
            print("That spot is already taken!")
            enter_move()
        
        draw_move()

        
    
   
display_board()
enter_move()
