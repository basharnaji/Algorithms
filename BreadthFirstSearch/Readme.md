# Breadth First Search

**Summary:**
Breadth First Search algorithm is a **_graph based_** algorithm that is used to answer 2 main questions:
1. does a connection exist between object a and object z?
2. What is the shortest path between these two objects?

This algorithm is a simple heuristic to determine shortest path as in the number of hops between two object.  Queues (controlling how objects are added the list) are a critical part of this algorithm to answer the 2nd questoin.

Breadth-first search doesn't include any "cost" in determining the shortest path; Djikstra's algorithm does.

**Graph**

_This is a sample graph to show path from San Diego to San Francisco with the different paths._  The objective of the algorithm is to find if a path exists betweeen two nodes and if it does than what is the shortest path (least number of hops).
![alt text][Graph]

[Graph]: BreadthFirstSearch.png "Sample Graph"

**Sample Code**

```python

from collections import deque

def is_city_string(name, str_city):
    if (name == str_city):
        return True

# Creating the graph 
#   a dictionary with the key being the node and the values are the nodes
#   connected to it.
Path = {}
Path['San Diego'] = ['San Bernardino', 'Los Angeles', 'Long Beach']
Path['San Bernardino'] = ['Fresno']
Path['Los Angeles'] = ['San Francisco']
Path['Long Beach'] = ['Santa Barbara']
Path['Fresno'] = ['Stockton']
Path['Santa Barbara'] = ['Monterey']
Path['Stockton'] = ['San Francisco']
Path['Monterey'] = ['San Francisco']
Path['San Francisco'] = []

# Creating some dead ends for negative testing
Path['Las Vegas'] = ['Denver', 'Portland']
Path['Denver'] = []
Path['Portland'] = []

# This function makes sure that there is a path from start node to the end node
def search_city(start_city, str_city):
    search_queue = deque()
    visited_city = set()
    search_queue += Path[start_city]
    visited_city.add(start_city)

    while search_queue:
        city = search_queue.popleft()
        if city not in visited_city:
            if is_city_string(city, str_city):
                print (f'Path to {str_city} was found')
                shortest_path = find_path (Path, start_city, str_city)
                return shortest_path
            else:
                search_queue += Path[city]
                visited_city.add(city)
    return False

def find_path(graph, start_city, end_city):
    path_list = [[start_city]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {start_city}
    if start_city == end_city:
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if end_city in next_nodes:
            current_path.append(end_city)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []    

start_city = 'San Diego'
destination_city = 'San Francisco'

path_to_city = search_city(start_city, destination_city)
if path_to_city:
    print (f'Shortest path from {start_city} to {destination_city} is: {path_to_city}')
else:
    print (f'No path was found from {start_city} to {destination_city}')