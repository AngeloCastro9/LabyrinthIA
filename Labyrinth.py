graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : ['A', 'B'],
  'E' : ['F'],
  'F' : ['F', 'C'],
  'G' : ['C', 'E'],
  'H' : ['A', 'F']
}

def dfs(graph, vertex):
    visited = set()

    def dfs_recursive(graph, vertex):
        visited.add(vertex)
        print("visitando: " + vertex)
        for neighbor in graph[vertex]:
            if vertex == 'E':
                print("me achou")
                break
            if neighbor not in visited:
                dfs_recursive(graph, neighbor) 

    dfs_recursive(graph, vertex)        

dfs(graph, 'A')
