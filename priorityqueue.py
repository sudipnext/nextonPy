from queue import PriorityQueue

def astar(start, goal, graph, heuristic):
    """Find the shortest path from start to goal using A* algorithm."""
    frontier = PriorityQueue()
    frontier.put((0, start))  # initial priority is 0
    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        _, current = frontier.get()

        if current == goal:
            break

        for next_node in graph[current]:
            # Calculate the cost to move to the next node
            cost = cost_so_far[current] + graph[current][next_node]
            # Calculate the estimated total cost of the next node
            total_cost = cost + heuristic(next_node, goal)

            if next_node not in cost_so_far or cost < cost_so_far[next_node]:
                cost_so_far[next_node] = cost
                priority = total_cost
                frontier.put((priority, next_node))
                came_from[next_node] = current

    # Reconstruct the path from start to goal
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()

    return path


# Define the graph as a dictionary
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2},
    'C': {'D': 3},
    'D': {'E': 1},
    'E': {}
}

# Define the heuristic function
def heuristic(node, goal):
    return abs(ord(goal) - ord(node))

# Call the astar function with start node 'A' and goal node 'E'
path = astar('A', 'E', graph, heuristic)

# Print the shortest path and its total cost
print("Shortest path:", path)
total_cost = sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))
print("Total cost:", total_cost)
