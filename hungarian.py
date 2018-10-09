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

costs = [[int(y) for y in x.split()] for x in (filter(None, costs.split('\n')))]
costs = np.array(costs)

r, c = linear_sum_assignment(costs)
out = []
for row, col in zip(r,c):
    out.append('x{}{} = '.format(row+1, col+1))
print('{}1'.format(''.join(out)))
print('cost: {}'.format(costs[r,c].sum()))


