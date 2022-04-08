# Dijkstra's Algorithm

**Summary:**
Unlike [Breadth First Search](../BreadthFirstSearch/) algorithm which calculates the shortest path based on _number of hops_, Dijkstra's algorithm calculates the shortest path based on _cost_.

This algorithm uses a _cost/weight_ between nodes to determine the shortest. *Note*: When there is a negative cost Dijkstra's algorithm can not be used and you should use Bellman-Ford algorithm.  Also Dijkstra's algorithm can not be used when there are cycles in your graph (starting from a node and ending up where you started)

The algorithm can be summarized by the following steps:

1. Find the chepest node
2. Calculate if there a cheper path to its neighbors, if so then update cost for that node
3. Repeat until this is done for all nodes
4. Determine the cheapest path

<br>

**Graph**

_This is a sample graph to show path from San Diego to San Francisco with the different path with their cost (here cost could be time ar anything of value to this problem)._  The objective of the algorithm is to find the path the lowest total cost between two nodes (in this example: San Diego to San Francisco)

![alt text][Graph]

[Graph]: Dijkstra.png "Sample Graph"


```python

# creating the graph of the nodes above
# creating the graph of the nodes above
Path = dict()
Path['San Diego'] = dict()
Path['San Diego']['San Bernardino'] = 6
Path['San Diego']['Los Angeles'] = 15
Path['San Diego'][ 'Long Beach'] = 8

Path['San Bernardino'] = dict()
Path['San Bernardino']['Fresno'] = 3
Path['San Bernardino']['Los Angeles'] = 7

Path['Los Angeles'] = dict()
Path['Los Angeles']['San Francisco'] = 15
Path['Los Angeles']['Fresno'] = 5
Path['Los Angeles']['Santa Barbara'] = 6
Path['Los Angeles']['Monterey'] = 6

Path['Long Beach'] = dict()
Path['Long Beach']['Los Angeles'] = 6

Path['Fresno'] = dict()
Path['Fresno']['Stockton'] = 4

Path['Santa Barbara'] = dict()
Path['Santa Barbara']['Monterey'] = 5

Path['Stockton'] = dict()
Path['Stockton']['San Francisco'] = 4

Path['Monterey'] = dict()
Path['Monterey']['San Francisco'] = 4
Path['San Francisco'] = []

# definining the cost hash table
# this will be used to maintain the lowest cost option
cost = dict()
cost['Long Beach'] = 8
cost['Los Angeles'] = 15
cost['San Bernardino'] = 6
cost['Fresno'] = 3
cost['Santa Barbara'] = 6
cost['Monterey'] = 6
cost['Stockton'] = 4
cost['San Francisco'] = float('inf')

# defining the parent hash table
# this will be used to determine the calling node for the lowest cost option
parent = dict()
parent['Long Beach'] = 'San Diego'
parent['Los Angeles'] = 'San Diego'
parent['San Bernardino'] = 'San Diego'
parent['Fresno'] = 'San Bernardino'
parent['Santa Barbara'] = 'Los Angeles'
parent['Monterey'] = 'Los Angeles'
parent['Stockton'] = 'Fresno'
parent['San Francisco'] = None
