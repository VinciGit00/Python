from pyvis import network as net
import networkx as nx

#%%
g=net.Network('500px', '500px')
nxg = nx.complete_graph(5)
g.from_nx(nxg)

#%%
g.show("example.html")
