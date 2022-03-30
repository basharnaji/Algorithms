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

"""

def is_city_string(name, str_city):
    if (name == str_city):
        return True

# Creating the graph 
#   a dictionary with the key being the node and the values are the nodes
#   connected to it.
Path = {}
Path['San Diego'] = ['San Bernardino', 'Los Angeles', 'Long Beach']
Path['San Bernardino'] = ['Fresno', 'Los Angeles']
Path['Los Angeles'] = ['San Francisco', 'Fresno', 'Santa Barbara', 'Monterey']
Path['Long Beach'] = ['Los Angeles']
Path['Fresno'] = ['Stockton']
Path['Santa Barbara'] = ['Monterey']
Path['Stockton'] = ['San Francisco']
Path['Monterey'] = ['San Francisco']
Path['San Francisco'] = []

# Creating some dead ends for negative testing
Path['Las Vegas'] = ['Denver', 'Portland']
Path['Denver'] = []
Path['Portland'] = []


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
