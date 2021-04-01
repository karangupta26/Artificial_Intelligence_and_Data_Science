# Practical 6 Simulated Annealing
########################################################
# Author    -   Karan Gupta
# Roll No.  -   2020PMD4224
# Degree    -   M.Tech (Mobile Computing and Data Analytics)
#########################################################
import numpy as np
import random

# Swap Function - Return a new route after swap between two cities
def swap(cities, city, city1):
    cities[city], cities[city1] = cities[min(city, city1)], cities[max(city, city1)]
    new_cities = cities.copy()
    return new_cities

# Simmulated Annealing Function - returns a nearly optimal or optimal solution
def simulated_Annealing(tspmatrix,temperature,cool):

    # Intialize the Cities
    cities = list(range(len(tspmatrix)))
    random.shuffle(cities)

    #Calculating cost of the shuffles city order
    old_cost = route_length(tspmatrix, cities)

    iteration = 1 #loop start
    no_of_iteration=int(temperature/cool)

    while iteration <= no_of_iteration:
        city = np.random.randint(0, len(tspmatrix))

        while True:
            city1 = np.random.randint(0, len(tspmatrix))
            if city != city1:
                break

        #swapping cities to find neighbours, i.e, getting new permutated cities
        new_cities = swap(cities, city1, city) 
        #calculating cost of swapped cities
        new_cost = route_length(tspmatrix, new_cities)

        #Optimisation to get the minimum cost tour
        if new_cost < old_cost:
            tour, cost = new_cities, new_cost

        #Annealing procedure to avoid stucking in local maxima
        elif np.random.rand() < np.exp((-(new_cost - old_cost))/temperature):
                tour, cost = new_cities, new_cost

        #cooling procedure. here cooling fucntion taken as anything as we want to reduce temperature at each iteration
        temperature = temperature - cool
        #temperature = temperature / math.log(cool,10)

        iteration+=1

    return tour,cost
    
# cost Function - Return the length of Route
def route_length(graph, cities):
    
   traversal_cost = 0
   
   for itr in range(len(cities)-1):
      traversal_cost += graph[cities[itr]][cities[itr+1]]
      
   traversal_cost += graph[cities[len(cities)-1]][cities[0]] 
   return traversal_cost

def main():
    tspmatrix = [[0, 2, 5, 3, 6],
             [2, 0, 4, 3, 3],
             [5, 4, 0, 7, 3],
             [3, 3, 7, 0, 3],
             [6, 3, 3, 3, 0]]
    
    print("\n\tTravelling Salesman Problem using Simulated Annealing")

    temp=int(input("Enter temperature : "))
    cool=int(input("Enter cooling temperature : "))
    result = simulated_Annealing(tspmatrix,temp,cool)
    
    print("\nSalesman tour:", "City -->" , result[0][0]+1 , "City -->" , result[0][1]+1 , 
          "City -->" , result[0][2]+1 , "City -->" , result[0][3]+1 , "City -->" , result[0][4]+1 , 
          "City -->" , result[0][0]+1)
    print("Traversal cost:" , result[1])
    

if __name__ == "__main__":
    main()