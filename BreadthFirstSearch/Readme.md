# Breadth First Search

**Summary:**
Breadth First Search algorithm is a **_graph based_** algorithm that is used to determine the shortest path between two objects.  This algorithm is simple heuristic to determine shortest path as in the number of hops between two object/points.  It doesn't include any "cost" in determining the shortest; Djikstra's algorithm includes cost.

**Graph**

_This is a sample graph to show path from San Diego to San Franciscon with the different paths._  The objective of the algorithm is to find the shortest path (least number of hops)
![alt text][Graph]

[Graph]: BreadthFirstSearch.png "Sample Graph"

**Sample Code**

```python

# Creating the graph 
Path = []
Path['San Diego'] = ['San Bernardino', 'Los Angeles', 'Long Beach']
Path['San Bernardino'] = ['Fresno']
Path['Los Angeles'] = ['San Francisco']
Path['Long Beach'] = ['Santa Barbara']
Path['Fresno'] = ['Stockton']
Path['Santa Barbara'] = ['Monterey']
Path['Stockton'] = ['San Francisco']
Path['Monterey'] = ['San Francisco']