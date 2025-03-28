# Simple Traversal
graph = {
  "New York": ["Chicago", "DC"],
  "Chicago": [],
  "DC": ["SFO", "LAX"],
  "SFO": ["LAX"],
  "LAX": ["New York"]
}

def dfs (graph, starting_node):
  visited = []
  stack = []
  stack.append(starting_node)
  while (stack):
    node = stack.pop(-1)
    print (f'DFS Visited {node}')
    visited.append(node)
    for neighbor in graph[node]:
      if neighbor not in visited:
        stack.append(neighbor)

# dfs(graph, "New York")

def bfs(graph, starting_node):
  visited = []
  queue = []
  queue.append(starting_node)
  while (queue):
    node = queue.pop(0)
    print(f'BFS Visited {node}')
    visited.append(node)
    for neighbor in graph[node]:
      if neighbor not in visited:
        queue.append(neighbor)

# bfs (graph, "New York")

# Weighted Traversal
graph_weighted = {
  "New York": [("Chicago", 300), ("DC", 100)],
  "Chicago": [],
  "DC": [("SFO", 1000), ("LAX", 1000)],
  "SFO": [("LAX", 100)],
  "LAX": [("New York", 1200)]
}

def bfs_weighted (source, destination):
  distances = []
  visited = []
  queue = []
  queue.append((source, 0))
  while (queue):
    node = queue.pop(0)
    visited.append(node[0])
    distances.append((node[0], node[1]))
    for neighbour in graph_weighted[node[0]]:
      if neighbour[0] not in visited:
        queue.append((neighbour[0], neighbour[1] + node[1]))
      if neighbour[0] not in distances:
        distances.append((neighbour[0], neighbour[1] + node[1]))
  for distance in distances:
    print(f'{distance}')

bfs_weighted("New York", "DC")