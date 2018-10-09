# src dest weight
edges = '''
1 2 2
1 3 3
1 5 3
2 3 2
2 4 4
3 4 1
3 5 2
4 6 3
5 6 1
'''
capacity = {1:1, 2:3, 6:-4}
# capacity is a dict using {node:capacity}.  
# If not specified, defaults to 0

from network import solver
solver(edges, capacity, plot=False, verbose=False)