from tkinter import *
#import tkMessageBox
from tkinter import messagebox
import webbrowser

TicTacToeApp = Tk()
TicTacToeApp.title("Tic Tac Toe")
TicTacToeApp.geometry("600x500")
TicTacToeApp.configure(bg = "blue")
TicTacToeApp.minsize(600,500)
TicTacToeApp.maxsize(600,500)
#general variables
bg_color = 'blue'
text_font = ("Times New Roman",20)
rets_photo = PhotoImage(file="CodeWithRets(small).png")

pcScoreVar = IntVar()
tieScoreVar = IntVar()
playerScoreVar = IntVar()

board = ['-' for i in range(9)]
current_symbol = 'X'
possible_moves = [i+1 for i in range(9)]

def init_game():
	global board
	board = ['-' for i in range(9)]
	global current_symbol
	current_symbol = 'X'
	global possible_moves
	possible_moves = [i+1 for i in range(9)]
	global Buttons
	for b in Buttons:
		b.configure( text = "-" , state = "active")


def end_game( who = " "):
	for i in Buttons:
		i.configure( state = "disable")

	if who == " ":
		tieScoreVar.set(tieScoreVar.get()+1)
		messagebox.showinfo("Its a Tie", "None of you Won its a tie")
	else:
		if who == "X":
			playerScoreVar.set(playerScoreVar.get() + 1)
		else :
			pcScoreVar.set(pcScoreVar.get() + 1)	
		messagebox.showinfo("Its a Win", f"{who} Won!!!")
	init_game()

def update_board(pos,symbol):
	board[pos] = symbol

def howWon(mark):
	global board
	if board[0] == board[1] and board[0] == board[2] and board[0] == mark:
		return True
	elif board[3] == board[4] and board[3] == board[5] and board[3] == mark:
		return True
	elif board[6] == board[7] and board[6] == board[8] and board[6] == mark:
		return True
	elif board[0] == board[3] and board[0] == board[6] and board[0] == mark:
		return True
	elif board[1] == board[4] and board[1] == board[7] and board[1] == mark:
		return True
	elif board[2] == board[5] and board[2] == board[8] and board[2] == mark:
		return True
	elif board[0] == board[4] and board[0] == board[8] and board[0] == mark:
		return True
	elif board[2] == board[4] and board[2] == board[6] and board[2] == mark:
		return True
	else :
		return False

def check_tie_min():
	global board
	for i in board:
		if i == '-':
			return False
	return True

def minmax( board , depth , isMaximazing ):
	#print(f"in minmax {depth} {board} {isMaximazing}")
	if howWon("O") :
		return 50

	elif howWon("X"):
		return -50

	elif check_tie_min():
		return 0

	if isMaximazing :
		bestScore = -50	

		for pos in range(len(board)):
			#print(f"APO isMaximazing pos = {pos}")
			if board[pos] == '-':
				board[pos] = "O"
				score = minmax(board,0,False)
				board[pos]="-"
				if score > bestScore:
					bestScore = score
		return bestScore
	else:
		bestScore = 800	

		for pos in range(len(board)):
			#print(f"APO isMaximazing not True pos = {pos}")
			if board[pos] == '-':
				board[pos] = "X"
				score = minmax(board,depth + 1,True)
				board[pos]="-"
				if score < bestScore:
					bestScore = score
		return bestScore


def pc_pos():
	#while True:
	bestScore = -50
	bestMove = 0
	global board
	global possible_moves

	for pos in range(len(board)):
		#print(f"APO PC_POS pos = {pos}")
		if board[pos] == '-':
			board[pos] = "O"
			score = minmax(board,0,False)
			board[pos]="-"
			if score > bestScore:
				bestScore = score
				bestMove = pos
		#if board[bestMove] == '-':
		#	break		
	print("Pcs pos= ",bestMove)
	possible_moves.pop(possible_moves.index(bestMove+1))
	return bestMove

def cliked(pos):

	global current_symbol
	
	Buttons[pos].configure( text = current_symbol , state = "disable")
	global board
	board[pos] = current_symbol

	print(board)
	global possible_moves
	
	possible_moves.pop(possible_moves.index(pos+1)) #
	print("Users pos = ",pos)
	print(possible_moves)
	if howWon(current_symbol):
		print("User Won")
		end_game("X")
	if check_tie_min():
		print("its a tie")
		end_game()
	current_symbol = "O"
	
	pcboardpos = pc_pos()
	Buttons[pcboardpos].configure( text = current_symbol , state = "disable")

	board[pcboardpos] = current_symbol
	print(possible_moves)
	if howWon(current_symbol):
		print("PC Won")
		end_game("O")
	if check_tie_min():
		print("its a tie")
		end_game()
	current_symbol = "X"


###########################
### ALL FRAMES ARE HERE ###
###########################
def gotoplay():
	PlayFramePage.pack(fill = "x")
	HomeFrame.forget()

def find_rets():  
	webbrowser.open_new_tab("https://linktr.ee/_rets")  

def init_score():
	pcScoreVar.set(0)
	tieScoreVar.set(0)
	playerScoreVar.set(0)

def play2main():
	init_game()
	init_score()
	HomeFrame.pack(fill = "x")
	PlayFramePage.forget()

def main2howtoplay():
	HowToPlay.pack(fill = "x")
	HomeFrame.forget()

def HowToPlay2HomePage():
	HomeFrame.pack(fill = "both")
	HowToPlay.forget()
############################
HowToPlay = Frame( TicTacToeApp, bg = bg_color)

FirstLabel = Label(HowToPlay , 
						text = "Game Instructions",
						#fg = f_color ,
						font = text_font,
						background = bg_color)

InstructionsText = Text(HowToPlay , 
							height = 15,
							#fg = f_color ,
							font = text_font,
							background = bg_color)
InstructionsText.insert(END, """In next Version will be Instructions\n\n\n\n\n\n\n\n\n\n
	It took me 3 hours just to make the fucking scroll bar \n\n\n\n\n\n\nSo ill write the Instrutions later\n\n\n\n\n\n
	Kissesssss<3<3""")
Scrollbar = Scrollbar(HowToPlay, 
							orient='vertical', 
							command=InstructionsText.yview
							)
BackToHomePageButton = Button(HowToPlay , 
						text = "Back To Main",
					 	#fg = button_color ,
                     	bg= bg_color,
                     	font = (text_font[0],14),
                     	#activebackground = button_bg_color,
	                    #activeforeground = button_color,
                     	pady = 10 ,
                     	padx = 70 ,
                     	command = HowToPlay2HomePage)
FirstLabel.pack()
BackToHomePageButton.pack(side = "bottom" , fill = "x")
Scrollbar.pack(side="right", fill="y")
InstructionsText.pack(side = "top" ,fill= "x")
Scrollbar.config(command=InstructionsText.yview)
InstructionsText.config(state = 'disabled' ,yscrollcommand=Scrollbar.set)

#######################
### FIND RETS FRAME ###
#######################
FindRetsFrame = Frame( TicTacToeApp , bg = bg_color , width = 7)

#FindRetsLabel = Label( FindRetsFrame , bg = bg_color , font = text_font, text = "Find Rets on Social")
FindRetsButton = Button( FindRetsFrame , bg = bg_color , font = ("Times New Roman",15), text = "Find Rets on Social",command = find_rets)
FindRetsButton.pack(fill = "x")
###################
### HOME FRAME ####
###################
HomeFrame = Frame(TicTacToeApp , bg = bg_color)

WelcomeLabel = Label(HomeFrame ,text = "Tic Tac Toe",font = text_font, bg = bg_color)
RetsLabel = Label(HomeFrame , text = "The app made by Rets",font = text_font, bg = bg_color)
RetsPhotoLabel = Label(HomeFrame , image = rets_photo, bg = bg_color)

ButtonsFrame = Frame(HomeFrame , bg = bg_color)
LearnAboutGameButton = Button(ButtonsFrame , text = "More About The Game",font = text_font,bg = "red", command = main2howtoplay)
GoToPlayButton = Button(ButtonsFrame ,text = "Play",font = text_font,bg = "red" , command = gotoplay)
LearnAboutGameButton.pack( pady = 30)#.grid(row = 0 , column = 0 , padx = "5")
GoToPlayButton.pack()#.grid(row = 0 , column = 1 )

WelcomeLabel.pack(fill = "x" )
RetsLabel.pack(fill = "x")
RetsPhotoLabel.pack(fill = "x")
ButtonsFrame.pack(fill = "x", pady = 30)


#######################
### PLAY PAGE FRAME ###
#######################

PlayFramePage = Frame(TicTacToeApp,bg = bg_color)
Buttons = []
#for i in range(9):

PlayFrameUP = Frame(PlayFramePage,bg = bg_color)

#, font = ("Times New Roman",20)

Buttons.append(Button(PlayFrameUP , text = "-", font = ("Times New Roman",10), width = 20 , height = 7, command = lambda : cliked( 0 )))
Buttons.append(Button(PlayFrameUP , text = "-", font = ("Times New Roman",10), width = 20 , height = 7, command = lambda : cliked( 1 )))
Buttons.append(Button(PlayFrameUP , text = "-", font = ("Times New Roman",10), width = 20 , height = 7, command = lambda : cliked( 2 )))
Buttons.append(Button(PlayFrameUP , text = "-", font = ("Times New Roman",10), width = 20 , height = 7, command = lambda : cliked( 3 )))
Buttons.append(Button(PlayFrameUP , text = "-", font = ("Times New Roman",10), width = 20 , height = 7, command = lambda : cliked( 4 )))
Buttons.append(Button(PlayFrameUP , text = "-", font = ("Times New Roman",10), width = 20 , height = 7, command = lambda : cliked( 5 )))
Buttons.append(Button(PlayFrameUP , text = "-", font = ("Times New Roman",10), width = 20 , height = 7, command = lambda : cliked( 6 )))
Buttons.append(Button(PlayFrameUP , text = "-", font = ("Times New Roman",10), width = 20 , height = 7, command = lambda : cliked( 7 )))
Buttons.append(Button(PlayFrameUP , text = "-", font = ("Times New Roman",10), width = 20 , height = 7, command = lambda : cliked( 8 )))

for i in range(9):
	Buttons[i].grid(row = i//3 , column = i%3, ipadx = 15, padx = 10, pady = 5)#

PlayFrameBottom = Frame(PlayFramePage , bg = bg_color)

PcScoreLabel = Label(PlayFrameBottom , text = "O's Score", font = ("Times New Roman",20),bg = bg_color)
PcScoreNumLabel = Label(PlayFrameBottom , textvariable = pcScoreVar, font = ("Times New Roman",20) ,bg = bg_color)

TieScoreLabel = Label(PlayFrameBottom , text = "Tie", font = ("Times New Roman",20),bg = bg_color)
TieScoreNumLabel = Label(PlayFrameBottom , textvariable = tieScoreVar, font = ("Times New Roman",20),bg = bg_color )

PlayersScoreLabel = Label(PlayFrameBottom , text = "X's Score", font = ("Times New Roman",20),bg = bg_color)
PlayersScoreNumLabel = Label(PlayFrameBottom , textvariable = playerScoreVar, font = ("Times New Roman",20),bg = bg_color)


PcScoreLabel.grid(row = 0 , column = 0)
TieScoreLabel.grid(row = 0 , column = 1)
PlayersScoreLabel.grid(row = 0 , column = 2)
PcScoreNumLabel.grid(row = 1 , column = 0 )
TieScoreNumLabel.grid(row = 1 , column = 1)
PlayersScoreNumLabel.grid(row = 1 , column = 2)

BackToMainButton = Button(PlayFrameBottom , text = "Back to main", font = ("Times New Roman",15),bg = bg_color, command = play2main)
BackToMainButton.grid(row = 0 , rowspan = 2 , column = 3)
InitializeScoreButton = Button(PlayFrameBottom , text = "Init Score", font = ("Times New Roman",15) ,bg = bg_color, command = init_score)
InitializeScoreButton.grid(row = 0 , rowspan = 2 , column = 4)
PlayFrameBottom.pack(side = "bottom",fill = "x")

PlayFrameUP.pack(side = "top" , fill = "both" , anchor = 'center')

#for i in range(9):
#	print(Buttons[i][Text])
#current_symbol = "X"



### START APP ###

FindRetsFrame.pack(side = 'bottom', fill = "x" )
HomeFrame.pack(fill = "both")
TicTacToeApp.mainloop()