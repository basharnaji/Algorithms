# Breadth First Search

**Summary:**
Breadth First Search algorithm is a **_graph based_** algorithm that is used to answer 2 main questions:
1. does a connection exist between object a and object z?
2. What is the shortest path between these two objects?

This algorithm is a simple heuristic to determine shortest path as in the number of hops between two object.  Queues (controlling how objects are added the list) are a critical part of this algorithm to answer the 2nd questoin.

Breadth-first search doesn't include any "cost" in determining the shortest path; Djikstra's algorithm does.

**Graph**

_This is a sample graph to show path from San Diego to San Franciscon with the different paths._  The objective of the algorithm is to find the shortest path (least number of hops)
![alt text][Graph]

[Graph]: BreadthFirstSearch.png "Sample Graph"

**Sample Code**

```python

from collections import deque

def is_city_SF(name):
    if (name == 'San Francisco'):
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


def search_city(start_city):
    search_queue = deque()
    visited_city = set()
    search_queue += Path[start_city]

    while search_queue:
        city = search_queue.popleft()
        if city not in visited_city:
            if is_city_SF(city):
                print ('we have reached San Francisco')
                return True
            else:
                search_queue += Path[city]
        visited_city.add(city)
    print ('San Francisco is not reachable')
    return False


search_city('San Diego')