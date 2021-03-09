# Practical 5 A* Algorithm
########################################################
# Author    -   Karan Gupta
# Roll No.  -   2020PMD4224
# Degree    -   M.Tech (Mobile Computing and Data Analytics)
#########################################################

# This class represent a graph
class Graph:
    # Initialize the class
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()
    # Create an undirected graph by adding symmetric edges
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist

    # Add a link from A and B of given distance, and also add the inverse link if the graph is undirected
    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance

    # Get neighbors or a neighbor
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    # Return a list of nodes in the graph
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)

# This class represent a node
class Node:
    # Initialize the class
    def __init__(self, name:str, parent:str):
        self.name = name
        self.parent = parent
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost

    # Compare nodes
    def __eq__(self, other):
        return self.name == other.name

    # Sort nodes
    def __lt__(self, other):
         return self.f < other.f

    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.name, self.f))

# A* search
def astar_search(graph, heuristics, start, end):
    
    # Create lists for open nodes and closed nodes
    open_nodes = []
    closed_nodes = []
    # Create a start node and an goal node
    start_node = Node(start, None)
    goal_node = Node(end, None)
    # Add the start node
    open.append(start_node)
    
    # Loop until the open list is empty
    while len(open_nodes) > 0:
        # Sort the open list to get the node with the lowest cost first
        open_nodes.sort()
        # Get the node with the lowest cost
        current_node = open_nodes.pop(0)
        # Add the current node to the closed list
        closed.append(current_node)
        
        # Check if we have reached the goal, return the path
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.name + ': ' + str(current_node.g))
                current_node = current_node.parent
            path.append(start_node.name + ': ' + str(start_node.g))
            
            # Return reversed path
            return path[::-1]
        
        # Get neighbours
        neighbors = graph.get(current_node.name)
        
        # Loop neighbors
        for key, value in neighbors.items():
            # Create a neighbor node
            neighbor = Node(key, current_node)
            # Check if the neighbor is in the closed list
            if(neighbor in closed_nodes):
                continue
            # Calculate full path cost
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            neighbor.h = heuristics.get(neighbor.name)
            neighbor.f = neighbor.g + neighbor.h
            # Check if neighbor is in open list and if it has a lower f value
            
            if(add_to_open(open_nodes, neighbor) == True):
                # Everything is green, add neighbor to open list
                open_nodes.append(neighbor)
    # Return None, no path is found
    return None

# Check if a neighbor should be added to open list
def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f > node.f):
            return False
    return True

# The main entry point for this module
def main():
    # Create a graph
    graph = Graph()

    # Create graph connections (Actual distance)
    while True:
        print("Add connections in Graph? Y/N (Enter your Choice)")
        choice=input()
        if choice=='Y':
            graphNodeConnection=str(input(" Enter Connection node Like this Node1 Node2 EdgeWeight : "))
            connection=graphNodeConnection.split()
            if len(connection)==3:
                graph.connect(connection[0],connection[1],int(connection[2]))
            else:
                print(" Enter a Valid Connection between Edges")
        elif choice=='N':
            break
        else:
            print(" Enter a vaild choice")
    
    # Make graph undirected, create symmetric connections
    print("Is your graph Undirected ? Y/N")
    choice=input("  Enter your choice : ")
    if choice=='Y':
        graph.make_undirected()

    # Create heuristics (straight-line distance)
    heuristics = {}
    print("Enter Your Heuristcs for Each Node")
    nodes=int(input("Enter No. of Nodes in the Graph : "))

    for i in range(0,nodes):
        heuristicValue=input(" Enter your Heuristic value like this Node HeuristicValue :")
        heuristic=heuristicValue.split()
        heuristics[heuristic[0]]=int(heuristic[1])
    
    # Run the search algorithm
    startAndGoalNode=input("Enter your Start Node and Goal Node (StartNode:GoalNode) - ")
    startAndGoal=startAndGoalNode.split(sep=':')
    path = astar_search(graph, heuristics, startAndGoal[0], startAndGoal[1])
    print("\nBelow is the optimal path from graph :")
    for i in range(len(path)):
        if i==len(path)-1:
            print(path[i])
        else:
            print(path[i],end='-->')


# Tell python to run main method
if __name__ == "__main__": 
    main()