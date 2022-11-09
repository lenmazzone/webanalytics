import networkx as nx
from operator import itemgetter
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
# create an empty graph
G=nx.DiGraph()

# read your data line by line and start adding nodes and edges to the graph
with open('./flow.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        # read information of which website (source) points to which website (target), and how many times (w)
        source,target,w=line.strip().split('\t')
        # add weighted edges to graph
        w=int(w)
        G.add_edge(source,target,weight=w)

pr = nx.pagerank(G, alpha=0.85,weight='weight')

srt = sorted(pr.items(),key=itemgetter(1),reverse=True)

pprint(srt[:50])


G = nx.DiGraph()
G.add_nodes_from("ABCD")
nx.draw(G, with_labels=True)
plt.show()

pr=nx.pagerank(G, alpha=0.1)
pr

G = nx.DiGraph()
G.add_nodes_from([1,2,3,4])
G.add_weighted_edges_from([(1,3,1), (1,4, 1),(1,2,1),(2,3,1),(2,4,1),(3,1,1),(4,1,1),(4,3,1)])
nx.draw(G, with_labels=True)
plt.show()