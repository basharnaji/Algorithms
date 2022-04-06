from collections import deque

""" 
Binary Search function

Assumption: provided with a sorted array
Input: a sorted list, item to find in the list
Output: index of the item being searched
"""


def binary_search(arr, item):
    # Set min, max indexes based on size of list
    min_val = 0
    max_val = len(arr) - 1

    while min_val <= max_val:
        # determine the midpoint and its value
        mid = (min_val + max_val) // 2
        guess = arr[mid]

        # check if our guess is right, otherwise determine
        #      the side of the list its on
        if guess == item:
            return mid
        if guess > item:
            max_val = mid - 1
        else:
            min_val = mid + 1
    return -1


""" 
To find the smallest value in the list provided

Input: a list
Output: index of the smallest element in the list
"""


def getMinimum(arr):
    min_value = arr[0]
    min_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
            min_idx = i
    return min_idx


"""
SelectionSort Algorithm

Input: must be providecd with a list to be sorted
Output: Sorted list
"""


def SelectionSort(arr):
    new_arr = []
    for i in range(len(arr)):
        min_idx = getMinimum(arr)
        new_arr.append(arr.pop(min_idx))
    return new_arr


"""
Quicksort algorithm

Input: a list of numbers to be sorted
Output: Sorted list
"""


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        # this is the pivot case
        pivot = arr[0]

        # sub-array of elements less than pivot
        smaller = [i for i in arr[1:] if i <= pivot]

        # sub-array of elements greater than pivot
        larger = [i for i in arr[1:] if i > pivot]

        return quicksort(smaller) + [pivot] + quicksort(larger)


"""
Breadth First Search algorithm

This algorithm requires a graph that has the edges to explore.  The sample provided is specific
to finding the city of San Francisco but this code can be modified for other similar purposes

Input: Graph that contians nodes and edges, starting node name, destination node name
Output: Does a path exist between starting & destination node, if so the shortest path in terms of hops

"""

def is_node_found(name, str_node):
    if (name == str_node):
        return True

def search_city(Path, start_node, dest_node):
    search_queue = deque()
    visited_node = set()
    search_queue += Path[start_node]
    visited_node.add(start_node)

    while search_queue:
        node_name = search_queue.popleft()
        if node_name not in visited_node:
            if is_node_found(node_name, dest_node):
                print (f'Path to {dest_node} was found')
                shortest_path = find_path (Path, start_node, dest_node)
                return shortest_path
            else:
                search_queue += Path[node_name]
                visited_city.add(node_name)
    return False

def find_path(graph, start_node, dest_node):
    path_list = [[start_node]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {start_node}
    if start_node == dest_node:
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if dest_node in next_nodes:
            current_path.append(dest_node)
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
