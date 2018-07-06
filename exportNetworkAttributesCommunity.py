import buildGraph
import networkx as nx

g = buildGraph.makeGraph("deepNetworkClean.csv")

def readCSVComm(filename, g):
    group_attr = []
    with open(filename) as f:
        coms = tuple(f.read().splitlines())
        for c in coms:
            l = c.split(",")
            group_attr.append(tuple(l))
    group_attr_dict = {}
    for k, v in group_attr:
        group_attr_dict[k] = group_attr_dict.get(k, ()) + (v,)   

    nx.set_node_attributes(g, group_attr_dict, 'community')


readCSVComm("louvain2.csv", g)

nx.write_gml(g, "labelLouvain.gml")
#print(g.nodes(data=True))
