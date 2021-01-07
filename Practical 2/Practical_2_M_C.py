# Practical 2
########################################################
# Author    -   Karan Gupta
# Roll No.  -   2020PMD4224
# Degree    -   M.Tech (Mobile Computing and Data Analytics)
#########################################################
'''
3 Missionaries and 3 Cannibals are on one side of a river, along with a boat that can hold one or two passengers.
Find a way to transport everyone to the other side of the river, without ever
leaving a group of Missionaries in one place outnumbered by the Cannibals in that place.
'''

# Importing Libary
from copy import deepcopy

Possible_Moves = [[1,1],[0,2],[2,0],[0,1],[1,0]]            # An Array consisting possible actions or move on current state

# Class for Defining State with its function
class State():
	
	def __init__(self, leftSide, boat, rightSide):
		self.leftSide = leftSide
		self.boat = boat
		self.rightSide = rightSide
		self.prev = None                        # Pointer or Hash storing of the Previous state

    # Function for printing the state using format method
	def __str__(self):
		return("({},{}) - ({},{}) - {}".format(self.leftSide[0],self.leftSide[1],self.rightSide[0],self.rightSide[1],self.boat))
	
    # Function for checking the equal from deepcopy function
	def __eq__(self, other):
		return (self.leftSide[0]==other.leftSide[0] and self.leftSide[1] == other.leftSide[1] and self.rightSide[0]==other.rightSide[0] and self.rightSide[1]==other.rightSide[1] and self.boat==other.boat)
	
    # Returns the hash value of an object if it has one
	def __hash__(self):
		return hash((self.leftSide[0],self.leftSide[1],self.boat,self.rightSide[0],self.rightSide[1]))
    
    # User Defined Function
    ## Function for validating the next state
	def isValidState(self):	
		# If the cannibals outnumber missionaries on the left or right side
		if(0 < self.leftSide[0] < self.leftSide[1] or 0 < self.rightSide[0] < self.rightSide[1]):
			return False	
		
		# Ensuring that more M/C are not transported than exist on a side
		if(self.leftSide[0]<0 or self.leftSide[1]<0 or self.rightSide[0]<0 or self.rightSide[1]<0):
			return False
		
		return True
	## Function for checking the Goal State
	def isGoalState(self):
		# If all the cannibals and missionaries have been transported across along with the boat
		return(self.leftSide[0]==0 and self.leftSide[1]==0)

def nextStates(current):
	nodes=[]                                        # Array For Storing all possible Node Values

	for moves in Possible_Moves:
		
		nextState = deepcopy(current)
		nextState.prev=current
		
		# When boat will Change Sides
		nextState.boat = 1-current.boat
		
		# Moving from left to right
		if(current.boat==0):

			# Increase right side population
			nextState.rightSide[0]+=moves[0]
			nextState.rightSide[1]+=moves[1]
			
			# Decreases left side population
			nextState.leftSide[0]-=moves[0]
			nextState.leftSide[1]-=moves[1]
		
		#Moving from right to left
		elif(current.boat==1):
			
			# Decreases left side population
			nextState.rightSide[0]-=moves[0]
			nextState.rightSide[1]-=moves[1]
			
			# Increase right side population
			nextState.leftSide[0]+=moves[0]
			nextState.leftSide[1]+=moves[1]
		
		if nextState.isValidState():
			nodes.append(nextState)
    
	return nodes

# Applying BFS for Check Path From Intial State to Final State	
def bfs(root):
	
	if root.isGoalState():
		return root
	
	visited = set()
	queue = [root]

	while queue:
		state = queue.pop()
		if state.isGoalState():
			return state
		
		visited.add(state)
		
		for child in nextStates(state):
			if child in visited:
				continue

			if child not in queue:
				queue.append(child)

def main():
	initial_state = State([3,3],0,[0,0])                                # Intital 
	state = bfs(initial_state)                                          # Intial State from where to start

	# Building Path
	path=[]
	while state:
		path.append(state)
		state = state.prev
	
	# Reversing path as the path which is Genrated using Prev Pointer Like Reversing the Linked list
	path=path[::-1]
	
	# Printing state change
	for state in path:
		if state.boat:
			print("""{:3} |         b| {:3}\n{:3} |          | {:3}""".format("c"*state.leftSide[1], "c"*state.rightSide[1], "m"*state.leftSide[0], "m"*state.rightSide[0]))
		else:
			print("""{:3} |b         | {:3}\n{:3} |          | {:3}""".format("c"*state.leftSide[1], "c"*state.rightSide[1], "m"*state.leftSide[0], "m"*state.rightSide[0]))
		print("--"*10)

if __name__ == "__main__":
	main()