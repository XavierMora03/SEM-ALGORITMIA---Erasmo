# %%
import networkx as nx
import matplotlib.pyplot as plt
import random as rd
import string as s

G = nx.Graph()

max_aristas = rd.randint(10,50)

# tenemos n/3 vértices
# pero para simplificar, maximo 27 vertices (cantidad de letras)
ind = int(min(27, max_aristas/3))
G.add_nodes_from(s.ascii_uppercase[0:ind])

lista = list(G.nodes)
for _ in range(max_aristas):
    nodo1, nodo2 = rd.sample(lista, 2)
    peso = rd.randint(10, 50)/10
    G.add_edge(nodo1, nodo2, weigth=peso, p=peso)

pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_color="#b74550")
labels = nx.get_edge_attributes(G, "p")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)

plt.figure()
T = nx.minimum_spanning_tree(G)

nx.draw(T, pos, with_labels=True, node_color="#45b7ac")
labels = nx.get_edge_attributes(T, "p")
nx.draw_networkx_edge_labels(T, pos, edge_labels=labels, font_size=8)
# %%
