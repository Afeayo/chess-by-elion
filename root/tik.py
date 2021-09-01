### this code is a tutorial
import tkinter as tk
import god

def what(x):
	# function to know more about an object
	print(repr(x), "<", str(x), ">") # repr and str
	# family tree of the class
	for base in x.__class__.__bases__:
		print("\t", base, base.__class__.__bases__)
	
	
def chessnot(n):
	# turns n into chess notation
	s = ""
	s += chr(n//8 + 97)
	s += str(n%8+1)
	return s
	
def notchess(s):
	#turns chess notation into n
	n = ord(s[0]) - 97
	n += int(s[1])*8
	return n
	


###
###
###

class Game(object):
	
	class Tile(tk.Button):

		number = None # 0-63
		color = None  # light or dark square 
		clicked = 0   # 0 means not clicked yet
		
		def setpiece(self,p):
			# s is a piece object
			if p is None:
				self["text"] = None		
			else:	
				self["text"] = p.unic
				

			
		def click(self):	# onclick protocol
			print(self.number, chessnot(self.number))
			if Game.selected is None:
				Game.selected = chessnot(self.number)
			self.clicked = (self.clicked+1)%2
			self["bg"] = [self.color, "red"][self.clicked]

	
	
	selected = None
	darkcol = "#769656"
	pieces = { 
		"wk" : "\u2654" , 
		"wq" : "\u2655" ,
		"wr" : "\u2656" ,
		"wb" : "\u2657" ,
		"wn" : "\u2658" ,
		"wp" : "\u2659" , 
		"bk" : "\u265A" ,
		"bq" : "\u265B" ,
		"br" : "\u265C" ,
		"bb" : "\u265D" ,
		"bn" : "\u265E" ,
		"bp" : "\u265F"
	}
	
	spots = { 
		"wk" : ("e1",), 
		"wq" : ("d1",),
		"wr" : ("a1","h1"),
		"wb" : ("c1","f1"),
		"wn" : ("b1","g1"),
		"wp" : ("a2","b2","c2","d2","e2","f2","g2","h2"), 
		"bk" : ("e8",),
		"bq" : ("d8",),
		"br" : ("a8","h8"),
		"bb" : ("c8","f8"),
		"bn" : ("b8","g8"),
		"bp" : ("a7","b7","c7","d7","e7","f7","g7","h7")
	}
	
	def __init__(self):
		self.tiles = []
		self.root = tk.Tk()
		pass
		
	def initialize_board(self):
		darkcol = "#769656"
		lightcol = "#eeeed2"
		
		#draws blank board
		root = self.root
		root.title("Chess by Elion")
		# root.geometry("800x800")
		
		#make the tiles	
		for i in range(64):
			# light square vs dark square
			color = lightcol
			if (i%2 + i//8%2)%2==0:
				color = darkcol
				
			# make button/square object
			b = self.Tile(root, font=("Arial", 40), height=1, width=3, bg=color)
			b["command"] = b.click
			b.color = color
			b.number = i
			# photo = tk.PhotoImage(file="white_pawn.png")
			# photo = photo.subsample(3,3)
			# b["image"] = photo
			
			self.tiles += [b]
		for b,i in zip(self.tiles, range(len(self.tiles))):
			b.grid(column = i//8, row = 7-i%8)
		
		# root.mainloop() # loop, last step?


	def set_pos(self, pos):
		# pos is a linear grid with piece objects
		for pis,til  in zip(pos, self.tiles):
			til.setpiece(pis)
			
	
	def initialize_pieces(self):
		print("init pieces")
		self.set_pos(god.God.home_lin())
	
	def play(self):
		self.initialize_board()
		self.initialize_pieces()
		self.root.mainloop() # loop, last step?


x = Game()
x.play()



'''
for tomorow:
	make classes for pieces ---
	make position class 
	have the game display a position
	make the game recieve a move request
	abstract away from the gui
	
'''