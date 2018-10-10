costs = '''
5 2 6 5
7 12 5 6
8 9 7 8
'''
supply = '25 30 50'
demand = '17 38 20 30'

import numpy as np

def northwest(costs, s, d):
    print('\nNorthwest method')
    supply = s.copy()
    demand = d.copy()
    x = np.zeros(costs.shape, dtype=int)
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
print(supply)

LP = True
VERBOSE = False
if LP:
    print('\n----- Gurobi Solver -----\n')
    from gurobipy import *
    m = Model()
    m.setParam(GRB.Param.OutputFlag, VERBOSE)

    x = {}
    for i, s in enumerate(supply):
        for j, d in enumerate(demand):
            x[i,j] = m.addVar(0, GRB.INFINITY, costs[i,j], GRB.INTEGER, 'x{}{}'.format(i+1, j+1))

    # Each supply row must sum to available stock
    for i, s in enumerate(supply):
        expr = LinExpr()
        for j, d in enumerate(demand):
            expr.addTerms(1, x[i, j])
        m.addConstr(expr, GRB.EQUAL, s)

    # Each demand column must sum to available demand
    for j, d in enumerate(demand):
        expr = LinExpr()
        for i, s in enumerate(supply):
            expr.addTerms(1, x[i, j])
        m.addConstr(expr, GRB.EQUAL, d)
    
    m.update()
    m.write('output/transportation.lp')
    m.optimize()
    print('\nObjective = {}'.format(m.ObjVal))
    for i, s in enumerate(supply):
        for j, d in enumerate(demand):
            print('{:4}'.format(round(x[i,j].X)), end=' ')
        print(' | {}'.format(s))
    print('-'*(5*len(demand)+2))
    for d in demand:
        print('{:4}'.format(d), end=' ')
    print()
