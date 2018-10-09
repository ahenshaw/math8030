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
import sys

import matplotlib.pyplot as plt
import matplotlib.cbook
import networkx as nx
import warnings
warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation) 

G=nx.DiGraph()
for edge in filter(None, edges.split('\n')):
    src, dest, weight = map(int, edge.split())
    G.add_edge(src, dest, weight=weight)

edge_labels=dict([((u,v,),d['weight'])
             for u,v,d in G.edges(data=True)])
pos = nx.kamada_kawai_layout(G)
nx.draw_networkx(G,pos,node_size=1200, node_color='#dddddd', font_size=20)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels,font_size=20)

plt.show()