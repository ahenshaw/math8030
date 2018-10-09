costs = '''
5 2 6 5
7 12 5 6
8 9 7 8
'''
supply = '25 30 50'
demand = '17 38 20 30'

import numpy as np

def northwest(costs, supply, demand):
    print('\nNorthwest method')
    x = np.zeros(costs.shape)
    r = 0
    c = 0
    bfs = []
    while True:
        bfs.append((r+1,c+1))
        x[r,c] = v = min(supply[r], demand[c])
        supply[r] -= v
        demand[c] -= v
        if supply[r] != 0:
            c += 1
        else:
            r += 1
        if not np.any(supply) and not np.any(demand):
            break
    print(x)
    print('\nz   =', np.sum(x*costs))
    print('bfs =', bfs)
    return x, bfs

costs = [[int(y) for y in x.split()] for x in (filter(None, costs.split('\n')))]
costs = np.array(costs, dtype=int)
supply = np.array(list(map(int, supply.split())), dtype=int)
demand = np.array(list(map(int, demand.split())), dtype=int)
print('costs =\n',costs)
print('supply =',supply)
print('demand =',demand)

x, bfs = northwest(costs, supply, demand)