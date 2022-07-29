##### Start of DFS vertex object
class vertex:
	def __init__(self,position,maze):
		self.position = position
		self.maze = maze
		self.visited = False

	def connect(self):
		self.right = self.maze[self.position[0]][self.position[1]+1] if self.position[1] < len(self.maze)-1 else None
		self.up = 	 self.maze[self.position[0]-1][self.position[1]] if self.position[0] > 0 else None
		self.left =  self.maze[self.position[0]][self.position[1]-1] if self.position[1] > 0 else None
		self.down=   self.maze[self.position[0]+1][self.position[1]] if self.position[0] < len(self.maze)-1 else None
		return 

	def neighbors(self):
		return self.right,self.up,self.left,self.down

	def __repr__(self):
		return f"vertex {self.position}"

	def __str__(self):
		return f"vertex {self.position}"

##### End of DFS vertex object

##### Start of maze functions
def maze_creator(rows,cols):
	maze = [[0,0,0],
			[0,0,0],
			[0,0,0]] ## this is temporary (hard-coded for trial)

	for row in range(rows):
		for col in range(cols):
			maze[row][col]=vertex((row,col),maze)

	maze_connector(maze)
	return maze

def maze_connector(maze):
	'''this function connects each vertex with its surrounding vertices'''
	for row in range(len(maze)):
		for col in range(len(maze)):
			maze[row][col].connect()

def maze_printer(maze):
	for row in range(len(maze)):
		print(maze[row])

#### End of maze functions