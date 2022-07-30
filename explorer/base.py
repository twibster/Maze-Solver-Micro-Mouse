from copy import deepcopy

##### Start of DFS vertex object
class vertex:
	def __init__(self,position,maze):
		self.position = position
		self.maze = maze
		self.start = False
		self.visited = False
		self.updated = False

	def connect(self):
		self.right = self.maze[self.position[0]][self.position[1]+1] if self.position[1] < len(self.maze)-1 else None
		self.up = 	 self.maze[self.position[0]-1][self.position[1]] if self.position[0] > 0 else None
		self.left =  self.maze[self.position[0]][self.position[1]-1] if self.position[1] > 0 else None
		self.down=   self.maze[self.position[0]+1][self.position[1]] if self.position[0] < len(self.maze)-1 else None
		return 

	def neighbors(self):
		return self.right,self.up,self.left,self.down

	def deal_neighbor(self,neighbor,command):
		'''this method does what the command says to the given neighbor:
		   command --> 0 returns the neighbor vertex direction
		   command --> 1 clears the neighbor vertex'''

		directions ={0:"up",1:"left",2:"down",3:"right"}

		for i in range(4):
			if getattr(self,directions[i])==neighbor:
				if command == 0:
					return i
				else:
					setattr(self,directions[i],None)

	def __repr__(self):
		return f"vertex {self.position}"

	def __str__(self):
		return f"vertex {self.position}"

##### End of DFS vertex object

##### Start of maze functions
def maze_creator(rows,cols):
	maze = [[0,0,0,0,0,0,0,0,0], # 9x9
		   [0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0],
		   [0,0,0,0,0,0,0,0,0]] ## this is temporary (hard-coded for trial)

	for row in range(rows):
		for col in range(cols):
			maze[row][col]=vertex((row,col),maze)

	maze_connector(maze)
	return maze

def maze_connector(maze):
	'''this function connects each vertex with its surrounding vertices'''
	for row in range(len(maze)):
		for col in range(len(maze)):
			vertex = maze[row][col]
			vertex.connect() if vertex else None

def maze_printer(maze,status,current_vertex=None,orien=None):
	'''this functions prints the maze given 2 parameters:
	maze: the maze itself
	status: 0 --> raw maze (the path is shown as vertices and the walls as None)
			1(default) --> cleared maze (the path is shown as empty place and the walls as #)'''
	direction_symbol={0:"|^",1:"<-",2:"| ",3:"->"} # symbols to represent the orientation
	temp_maze = deepcopy(maze)
	if not status:
		for row in range(len(maze)):
			for col in range(len(maze)):
				vertex = maze[row][col]
				if vertex:
					if vertex.start:
						temp_maze[row][col]= "S "
					elif vertex == current_vertex:
						temp_maze[row][col]= direction_symbol[orien]
					elif vertex.visited:
						temp_maze[row][col]= "/ "
					else:
						temp_maze[row][col]= "  "
				else:
					temp_maze[row][col]= "# "

	for row in range(len(maze)):
		print(temp_maze[row])
	print("\n ---------------------")

#### End of maze functions