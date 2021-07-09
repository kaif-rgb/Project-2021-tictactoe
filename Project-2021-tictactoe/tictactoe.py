from tkinter import *
from tkinter import messagebox
from functools import partial
import random 
from copy import deepcopy 

global board
board = [[' ' for x in range(3)] for y in range(3)]
sign = 0
def winner(b,l):
    return ((b[0][0]==l and b[0][1]==l and b[0][2]==l) or
            (b[1][0]==l and b[1][1]==l and b[1][2]==l) or
            (b[2][0]==l and b[2][1]==l and b[2][2]==l) or
            (b[0][0]==l and b[1][0]==l and b[2][0]==l) or
            (b[0][1]==l and b[1][1]==l and b[2][1]==l) or
            (b[0][2]==l and b[1][2]==l and b[2][2]==l) or
            (b[0][0]==l and b[1][1]==l and b[2][2]==l) or
            (b[0][2]==l and b[1][1]==l and b[2][0]==l))
            
            
def isfull():
    flag = True
    for i in board:
        if  i.count(' ') > 0:
            flag = False
    return flag 
    
def pc():
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i,j])
    if len(possiblemove) == 0:
        return
    else:
        for let in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if winner(boardcopy, let):
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner)-1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge)-1)
            return edge[move]
                    
        
        
def get_text_pc(i,j,gb,l1,l2):
    global sign
    if board[i][j] == " ":
        if sign % 2==0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = 'X'
        else:
            l1.config(state=ACTIVE)
            l2.config(state=DISABLED)
            board[i][j] = 'O'
        sign +=1
        button[i][j].config(text = board[i][j])
        x = True
        if winner(board,'X'):
            x = False
            gb.destroy()
            messagebox.showinfo('Winner','Player X won the match.')
            
        elif winner(board,'O'):
            x = False
            gb.destroy()
            messagebox.showinfo('Winner','Player O won the match.')
            
        elif isfull():
            x = False
            gb.destroy()
            messagebox.showinfo('Tie','No one won the match')
            
        if x:
            if sign %2 != 0:
                move = pc()
                button[move[0]][move[1]].config(state=DISABLED)
                get_text_pc(move[0],move[1],gb,l1,l2)
            
def get_text_pl(i,j,gb,l1,l2):
    global sign
    if board[i][j] == " ":
        if sign % 2==0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = 'X'
        else:
            l1.config(state=ACTIVE)
            l2.config(state=DISABLED)
            board[i][j] = 'O'
        sign +=1
        button[i][j].config(text = board[i][j])
        if winner(board,'X'):
            gb.destroy()
            messagebox.showinfo('Winner','Player X won the match.')
            
        elif winner(board,'O'):
            gb.destroy()
            messagebox.showinfo('Winner','Player O won the match.')
            
        elif isfull():
            gb.destroy()
            messagebox.showinfo('Tie','No one won the match')
        
        
def gameboard_pc(game_board,l1,l2):
    global button 
    button = []
    for i in range(3):
        m = i + 3 
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc,i,j,game_board,l1,l2)
            button[i][j] = Button(game_board,height=4, width=8,bd=2,command=get_t)
            button[i][j].grid(row=m,column=n)
    game_board.mainloop()

def gameboard_pl(game_board,l1,l2):
    global button 
    button = []
    for i in range(3):
        m = i + 3 
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t_pl = partial(get_text_pl,i,j,game_board,l1,l2)
            button[i][j] = Button(game_board,height=4, width=8,bd=2,command=get_t_pl)
            button[i][j].grid(row=m,column=n)
    game_board.mainloop()           

def withplayer(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title('tiktactoe')
    l1 = Button(text = 'Player: X',state=ACTIVE,width=10)
    l2 = Button(text = 'Player: O',state=DISABLED,width=10)
    l1.grid(row=1,column=1)
    l2.grid(row=2,column=1)
    gameboard_pl(game_board,l1,l2)    
        
        
def withpc(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title('tiktaktoe')
    l1 = Button(text = 'Player: X',state=ACTIVE,width=10)
    l2 = Button(text = 'Player: O',state=DISABLED,width=10)
    l1.grid(row=1,column=1)
    l2.grid(row=2,column=1)
    gameboard_pc(game_board,l1,l2)
    

def play():
    menu = Tk()
    menu.config(background= 'light green')
    menu.geometry('250x250')
    menu.title('tictactoe')
    wpc= partial(withpc,menu)
    wpl = partial(withplayer,menu) 
    button1 = Button(menu,text='Tictactoe',activebackground='yellow',activeforeground='red',bg='red',fg='yellow',width=50,bd=5)
    button2 = Button(menu,text='Singleplayer',activebackground='yellow',activeforeground='red',bg='red',command=wpc,fg='yellow',width=50,bd=5)
    button3 = Button(menu,text='Multiplayer',activebackground='yellow',activeforeground='red',bg='red',command=wpl,fg='yellow',width=50,bd=5)
    button4 = Button(menu,text='Exit',command=menu.quit,activebackground='yellow',activeforeground='red',bg='red',fg='yellow',width=50,bd=5)
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    menu.mainloop()
    
    
play()