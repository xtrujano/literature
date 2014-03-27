import networkx as nx
import itertools
import matplotlib.pyplot as plt


G = nx.Graph()

G.add_edges_from([(1,2,{'w': 3}),
                  (2,3,{'w': 2}),
                  (3,1,{'w': 1}),
                  (3,4,{'w': 4}),
                  (4,5,{'w': 12}),
                  (5,6,{'w': 11}),
                  (6,4,{'w': 13}),
              ])



import pprint


# detect triangles
triangles = []
for trio in itertools.combinations(G.nodes(), 3):
    vertices = []
    for v in itertools.combinations(trio, 2):
        vertice = G.get_edge_data(*v)
        if vertice:
            vertices.append(v)

    if len(vertices)==3:
        triangles.append(vertices)

pprint.pprint(triangles)

nx.draw(G)



for t in triangles:
    weights = {}
    for v in t:
        k = (G.get_edge_data(*v)['w'])
        weights[k]=v
        
    l = weights.keys()
    l.sort()
    l.reverse()
    quitar = l.pop()
    G.remove_edge(*weights[quitar])



#for  G.edges(data=True)
# EdgeWidth = [G.get_edge_data(*e)['w']*10 for e in G.edges()]
# pos = nx.spring_layout(G)
# nx.draw_networkx_edges(G, pos=pos, edge_width=EdgeWidth, alpha=0.75)
# nx.draw_networkx_nodes(G, pos=pos)
nx.draw(G)
plt.show()
