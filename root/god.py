			



class Piece(object):
	pass

class White_Piece(object):
	pass
class Black_Piece(object):
	pass

class White_King(Piece, White_Piece):
	unic = "\u2654"
	code = "wk"
	homesquare = ("e1",)

class White_Queen(Piece, White_Piece):
	unic = "\u2655"
	code = "wq"
	homesquare = ("d1",)


class White_Bishop(Piece, White_Piece):
	unic = "\u2657"
	code = "wb"
	homesquare = ("c1","f1")


class White_Knight(Piece, White_Piece):
	unic = "\u2658"
	code = "wn"
	homesquare = ("b1","g1")


class White_Rook(Piece, White_Piece):
	unic = "\u2656"
	code = "wr"
	homesquare = ("a1","h1")

class White_Pawn(Piece, White_Piece):
	unic = "\u2659"
	code = "wp"
	homesquare = ("a2","b2","c2","d2","e2","f2","g2","h2")

############
class Black_King(Piece, Black_Piece):
	unic = "\u265A"
	code = "bk"
	homesquare = ("e8",)

class Black_Queen(Piece, Black_Piece):
	unic = "\u265B"
	code = "bq"
	homesquare = ("d8",)


class Black_Bishop(Piece, Black_Piece):
	unic = "\u265D"
	code = "bb"
	homesquare = ("c8","f8")


class Black_Knight(Piece, Black_Piece):
	unic = "\u265E"
	code = "bn"
	homesquare = ("b8","g8")


class Black_Rook(Piece, Black_Piece):
	unic = "\u265C"
	code = "br"
	homesquare = ("a8","h8")

class Black_Pawn(Piece, Black_Piece):
	unic = "\u265F"
	code = "bp"
	homesquare = ("a7","b7","c7","d7","e7","f7","g7","h7")


class God(object):
	
	pieces = ( 
		White_King, White_Queen, White_Pawn, White_Rook, White_Bishop, White_Knight,
		Black_King, Black_Queen, Black_Pawn, Black_Rook, Black_Bishop, Black_Knight
		)
		
	def to_pair(s):
		# translate chess notation to pair of coordinates (file,rank)
		file = ord(s[0])-97
		rank = int(s[1])-1
		return (file, rank)
		
	def make_grid():
		return [ [ None for rank in range(8) ] for file in range(8) ]
	
	def make_home_pos():
		g = God.make_grid()
		for c in God.pieces:
			for sq in c.homesquare:
				p = God.to_pair(sq)
				g[p[0]][p[1]] = c()
		
		return g
				
	def to_lin(g):
		# turns the grid into a list for the gui
		r = []
		for file in g:
			r += file
		return r
	
	def home_lin():
		return God.to_lin(God.make_home_pos())




		
		
def main():
	print("hello")
	x = Black_King
	print(Black_King)
	print(x)
	print(Black_King())
	print(x())
	
main()


