import numpy as np
from fractions import Fraction
import io
import webbrowser

from tableau import tformat
from htmltemplate import html


tableau = np.array([\
    [  2,  3,   4,  5, 0, 0, 0, 0], 
#   -------------------------------
    [ -1,  1,  -1,  1, 1, 0, 0, -10],  #A[0]
    [ -1,  2,  -3,  4, 0, 1, 0,  -6],  #A[1]
    [ -3,  4,  -5,  6, 0, 0, 1, -15],  #A[2]
    ], dtype=object)

output = 'output/simplex.html'

def do_pivot(tableau, pivot):
    r, c = pivot
    pr = tableau[r]
    # normalize pivot row
    pr /= pr[c-1]
    # normalize rest of table
    for i in range(len(tableau)):
        if i != r:
            mult = tableau[i][c-1]
            tableau[i] -= mult*pr

def find_pivot(tableau):
    
# make the matrix use fraction math
tableau += Fraction()   

# define the parts of the tableau
z = tableau[0] # top row (Z) of tableau
M = tableau[1:]


out = io.StringIO()
out.write('Initial tableau')

# tableau(matrix name, [basic variable], (r,c) of pivot (optional) )
pivot = (1,1)
out.write(tformat(tableau, [5,6,7], pivot))

out.write(r"$x_5$ exits. $x_1$ enters")
do_pivot(tableau, pivot)
out.write(tformat(tableau, [1,6,7]))

open(output, 'w').write(html.format(out.getvalue()))
webbrowser.open(output)



