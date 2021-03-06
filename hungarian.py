# fill in the following cost matrix
costs = '''
1 3 5 -1 0 2
2 3 5 6 1 3
1 1 3 7 1 2
7 0 1 1 5 7
5 5 1 1 2 1
-1 3 2 8 -1 8
'''

from scipy.optimize import linear_sum_assignment
import numpy as np

def pp(table, side=None):
    if len(table.shape) == 1:
        for v in table:
            print('{:3}'.format(v), end='')
        print()
    else:
        for i, row in enumerate(table):
            for v in row:
                print('{:3}'.format(v), end='')
            if side is not None:
                print(' | {:3}'.format(side[i][0]))
            else:
                print()


costs = [[int(y) for y in x.split()] for x in (filter(None, costs.split('\n')))]
costs = np.array(costs)

r, c = linear_sum_assignment(costs)
out = []
for row, col in zip(r,c):
    out.append('x{}{} = '.format(row+1, col+1))

print('--------- Solution ----------')
print('{}1'.format(''.join(out)))
print('cost: {}'.format(costs[r,c].sum()))
print('\n --------- Steps ----------')
redo = costs.copy()
print('Row minimums')
min_rows = np.min(redo, axis=1).reshape((-1,1))
pp(redo, min_rows)

redo -= min_rows
print('\nCol minimums')
min_cols = np.min(redo, axis=0)
pp(redo)
print('-'*3*len(redo[0]))
pp(min_cols)
redo -= min_cols
print()
pp(redo)
print('\nCover all zeros')
print('Find min of uncovered cells = x')
print('Subtract x from uncovered cells')
print('Add x to intersection points of lines')
print('Repeat until zero on each row and column')

LP = True
VERBOSE = False
if LP:
    print('\n----- Gurobi Solver -----\n')
    from gurobipy import *
    m = Model()
    m.setParam(GRB.Param.OutputFlag, VERBOSE)

    x = {}
    r, c = costs.shape
    for i in range(r):
        for j in range(c):
            x[i,j] = m.addVar(0, 1, costs[i,j], GRB.BINARY, 'x{}{}'.format(i+1, j+1))

    # Each row must be assigned to one column
    for i in range(r):
        expr = LinExpr()
        for j in range(c):
            expr.addTerms(1, x[i, j])
        m.addConstr(expr, GRB.EQUAL, 1)

    # Each column must be assigned to one row
    for j in range(c):
        expr = LinExpr()
        for i in range(r):
            expr.addTerms(1, x[i, j])
        m.addConstr(expr, GRB.EQUAL, 1)
    
    m.update()
    m.write('output/match.lp')
    m.optimize()
    print('\nObjective = {}'.format(m.ObjVal))
    for i, j in sorted(x):
        v = x[i, j].x
        if v > 0.5:
            print ('x{}{} = {}'.format(i+1, j+1 , 1))



