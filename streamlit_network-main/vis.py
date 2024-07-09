import dgl
from pyvis.network import Network
import networkx as nx

dataset = dgl.data.CoraGraphDataset()

g = Network(height=800, width=800, notebook=True)

netxG = nx.Graph(dataset[0].to_networkx())

mapping = {i:i for i in range(netxG.size())} #Setting mapping for the relabeling
netxH = nx.relabel_nodes(netxG,mapping) #relabeling nodes

g.from_nx(netxH)
g.show('ex.html')