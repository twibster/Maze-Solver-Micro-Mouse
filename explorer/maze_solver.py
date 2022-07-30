from base import *
import os

def where_to_go(where_am_i,orien,surr,maze,dfs_history,start=False):
	'''this function returns the direction of movement given three variables:
	   where_am_i = a tuple of x,y --> (x,y)
	   orien = from 0 to 4 (the absolute orientation is facing forward (0) (1 --> left) (2 --> backward) (3 --> right))
	   surr = a tuple of the surrounding blocks (up,left,down,right) --> 1 if the block is clear (can move there),
		      0 or None if a wall is detected.'''

	# where_am_i = calibrate_tuple(where_am_i,1) #reverse the x , y coordinates 
	current_vertex = maze[where_am_i[0]][where_am_i[1]]
	if not current_vertex: # hopefully this condition will not be met (the robot got through one of the walls)
		return 0
	if start:
		current_vertex.start=True
	surr = calibrate_tuple(surr,orien)
	update_vertex(current_vertex,surr,maze)
	dfs(current_vertex,dfs_history,maze)
	return 

def calibrate_tuple(to_rotate,factor):
	'''this function rotates a tuple (surr),(where_am_i) by a given number(orien),(1)in order to align the micro-mouse with the maze'''

	while factor>=len(to_rotate):
	    factor = factor - len(to_rotate)
	return to_rotate[-factor:] + to_rotate[:-factor]

def update_vertex(vertex,surr,maze):
	'''this function updates each vertex with the correct information received from the micro-mouse
	   whether it is a wall or not --We assumed earlier that all vertices in the maze are open (not walls)'''

	directions ={0:"up",1:"left",2:"down",3:"right"}
	for i in range(4):
		neighbor_vertex = getattr(vertex,directions[i])
		if neighbor_vertex:
			if not neighbor_vertex.updated:
				if not (neighbor_vertex and surr[i]): # check if the received status is the same as the assumed one 
					maze[neighbor_vertex.position[0]][neighbor_vertex.position[1]] = None # set the block as a wall
				neighbor_vertex.updated = True # flag the vertex as updated (future updates will be ignored)
	maze_connector(maze)

def dfs(vertex,history,maze):
	if vertex.start:
		start=vertex
		vertex.updated = vertex.visited = True
		history.append(vertex)

	for neighbor in vertex.neighbors():
		if neighbor and (not neighbor.visited):
			neighbor.visited = True
			history.append(neighbor) 
			orein = vertex.deal_neighbor(neighbor,0) # get the direction to the next vertex
			os.system("cls")
			print(history,orein)
			maze_printer(maze,0,neighbor,orien=orein)
			surr=tuple(map(int,input("Data: ").split(" "))) # get the surroundings from the user (these will be obtained from the sensors later)
			where_to_go(neighbor.position,orein,surr,maze,history)
	return 1

def main():
	maze = maze_creator(9,9)
	where_to_go((0,1),2,(1,0,1,0),maze,[],1) #initiate the first step
	print("the maze has been explored or a loop messed me up")
	maze_printer(maze,0,vertex)

main()