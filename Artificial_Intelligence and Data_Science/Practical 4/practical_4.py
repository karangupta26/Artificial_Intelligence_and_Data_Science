# Practical 4 Travelling Salesman Problem Using Hill Climbing
########################################################
# Author    -   Karan Gupta
# Roll No.  -   2020PMD4224
# Degree    -   M.Tech (Mobile Computing and Data Analytics)
#########################################################

import random

# Function for return a Random path for intialization
def randomSolution(tspMatrix):
    cities = list(range(len(tspMatrix)))
    solution = []

    for i in range(len(tspMatrix)):
        randomCity = cities[random.randint(0, len(cities) - 1)]
        solution.append(randomCity)
        cities.remove(randomCity)
    print(solution)
    return solution

# Return the route length
def routeLength(tspMatrix, solution):
    routeLength = 0
    for i in range(len(solution)):
        routeLength += tspMatrix[solution[i - 1]][solution[i]]
    print("Current Route Length",routeLength)
    return routeLength

# Return all the Neighbours
def getNeighbours(solution):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
    print("Current neightbours",neighbours)
    return neighbours

# Get the Best Neighbour and Route Length 
def getBestNeighbour(tspMatrix, neighbours):
    bestRouteLength = routeLength(tspMatrix, neighbours[0])
    bestNeighbour = neighbours[0]
    for neighbour in neighbours:
        currentRouteLength = routeLength(tspMatrix, neighbour)
        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNeighbour = neighbour
    print("Best neighbour and route length ",bestNeighbour,bestRouteLength)
    return bestNeighbour, bestRouteLength

# Hill Climbing Based on Minimal path function
def hillClimbing(tspMatrix):
    currentSolution = randomSolution(tspMatrix)                                             # Initialize a random path 
    currentRouteLength = routeLength(tspMatrix, currentSolution)                            # Get the route length of random path
    neighbours = getNeighbours(currentSolution)                                             # Get all the neighbours from current solution
    bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tspMatrix, neighbours)       # Get the best neighbour with its route length
    i=0
    while bestNeighbourRouteLength < currentRouteLength:                                    # Check for minimum route length value
        print("i=",i)
        currentSolution = bestNeighbour
        currentRouteLength = bestNeighbourRouteLength
        neighbours = getNeighbours(currentSolution)
        bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(tspMatrix, neighbours)

        i+=1
    return currentSolution, currentRouteLength

# Graph Input as Adjanceny Matrix
def main():
    tspMatrix = [
        [0, 2, 3, 3, 6],
        [2, 0, 4, 5, 7],
        [3, 4, 0, 7, 3],
        [3, 5, 7, 0, 3],
        [6, 3, 3, 3, 0]
    ]

    result=hillClimbing(tspMatrix)
    print("The Minimal TSP Route is : ",end=" ")
    for i in range(len(result[0])):
        if i==(len(result[0])-1):
            print(result[0][i]+1)
        else:
            print(result[0][i]+1,end=" ")
    print("The Minimum Route Path : ",result[1])

if __name__ == "__main__":
    main()