from base import *

def where_to_go(where_am_i,orien,surr,maze):
	'''this function returns the direction of movement given three variables:
	   where_am_i = a tuple of x,y --> (x,y)
	   orien = from 0 to 4 (the absolute orientation is facing forward (0) (1 --> left) (2 --> backward) (3 --> right))
	   surr = a tuple of the surrounding blocks (right,up,left,down) --> 1 if the block is clear (can move there),
		      0 or None if a wall is detected.'''

	current_vertex = maze[where_am_i[0]][where_am_i[1]]
	surr = calibirate_orien(orien,surr)
	update_vertex(current_vertex,surr,maze)
	return

def calibirate_orien(orien,surr):
	'''this function rotates a tuple (surr) by a given number (orien) in order to align the micro-mouse with the maze'''

	while orien>=len(surr):
	    orien = orien - len(surr)
	return surr[-orien:] + surr[:-orien]

def update_vertex(vertex,surr,maze):
	'''this function updates each vertex with the correct information recieved from the micro-mouse
	   whether it is a wall or not --We assumed earlier that all vertices in the maze are open (not walls)'''

	directions ={0:"right",1:"up",2:"left",3:"down"}
	for i in range(4):
		neighbor_vertex = getattr(vertex,directions[i])
		if not (neighbor_vertex and surr[i]):
			if neighbor_vertex:
				maze[neighbor_vertex.position[0]][neighbor_vertex.position[1]] = None
	maze_connector(maze)

def main():
	maze = maze_creator(3,3)
	maze_printer(maze)

main()





