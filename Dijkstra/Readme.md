# Dijkstra's Algorithm

**Summary:**
Unlike [Breadth First Search](../BreadthFirstSearch/) algorithm which calculates the shortest path based on _number of hops_, Dijkstra's algorithm calculates the shortest path based on _cost_.

This algorithm uses a _cost/weight_ between nodes to determine the shortest. *Note*: When there is a negative cost Dijkstra's algorithm can not be used and you should use Bellman-Ford algorithm

**Graph**

_This is a sample graph to show path from San Diego to San Francisco with the different path with their cost (here cost could be time ar anything of value to this problem)._  The objective of the algorithm is to find the path the lowest total cost between two nodes (in this example: San Diego to San Francisco)

![alt text][Graph]

[Graph]: Dijkstra.png "Sample Graph"