import sys
from collections import defaultdict

import matplotlib.pyplot as plt
import matplotlib.cbook
import networkx as nx
import warnings
from   gurobipy import *
warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation) 

def solver(edges, capacity, plot=False, lp='graph.lp', verbose=0):
    G=nx.DiGraph()
    for edge in filter(None, edges.split('\n')):
        src, dest, weight = map(int, edge.split())
        G.add_edge(src, dest, weight=weight)

    edge_labels=dict([((u,v,),d['weight'])
                for u,v,d in G.edges(data=True)])

    m = Model()
    m.setParam(GRB.Param.OutputFlag, verbose)

    x = {}
    constraints = defaultdict(LinExpr)
    for src, dest, d in G.edges(data=True):
        x[src, dest] = v = m.addVar(0,GRB.INFINITY, d['weight'], GRB.CONTINUOUS, 'x{}{}'.format(src, dest))
        m.update()
        constraints[src].addTerms(1, v)
        constraints[dest].addTerms(-1, v)

    for node, expr in constraints.items():
        m.addConstr(expr, GRB.EQUAL, capacity.get(node,0))
    m.update()
    m.write(lp)
    m.optimize()

    print('Objective: {}'.format(m.ObjVal))
    for src, dest in sorted(x):
        print ('x{}{} = {}'.format(src, dest ,x[src, dest].x))

    if plot:
        pos = nx.kamada_kawai_layout(G)
        nx.draw_networkx(G,pos,node_size=1200, node_color='#dddddd', font_size=20)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,font_size=20)

        plt.show()
