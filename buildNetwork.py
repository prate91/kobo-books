import csv
import networkx as nx
import collections
import matplotlib.pyplot as plt

g=nx.DiGraph()

f1 = csv.reader(open("deepNetwork.csv","r"))

for row in f1:
    #print row
    g.add_nodes_from(row) 
    # g.add_node(row[0])
    # g.add_node(row[1]) #17973
    #nx.draw_circular(g,node_color='blue')

f2 = csv.reader(open("deepNetwork.csv","r"))

for row in f2: 
    #print row[0]
    g.add_edge(row[0],row[1])
    #g.add_edges_from(row)

# VECCHIO GRAFO
h=nx.DiGraph()

f3 = csv.reader(open("deepNetworkClean.csv","r"))

for row in f3:
    #print row
    h.add_nodes_from(row)
    #nx.draw_circular(g,node_color='blue')

f4 = csv.reader(open("deepNetworkClean.csv","r"))

for row in f4: 
    #print row[0]
    h.add_edge(row[0],row[1])
    #g.add_edges_from(row)


# print (g.out_degree())
# print (g.in_degree())
#nx.write_adjlist(g, "deepNetwork.adjlist")
#print nx.betweenness_centrality
# print ("---------------------------")
# print ("Diretto? NUOVO")
# print (nx.is_directed(g))
# print ("---------------------------")
# print "Numero di nodi NUOVO"
# print g.number_of_nodes()
# print ("---------------------------")
# print "Numero di archi NUOVO"
# print g.number_of_edges()
# print "---------------------------"
# print "Diretto? VECCHIO"
# print nx.is_directed(h)
# print "---------------------------"
# print "Numero di nodi VECCHIO"
# print h.number_of_nodes()
# print "---------------------------"
# print "Numero di archi VECCHIO"
# print h.number_of_edges()
# print "---------------------------"
# print "Lista dei nodi del grafo"
# #print list(g.nodes())
# print "Lista dei nodi del grafo con grado"
# #print list(g.degree())
# print "---------------------------"
# print "Lista dei nodi del grafo con grado ordinati"
# def takeSecond(elem):
#     return elem[1]
# #print sorted(g.degree(), key=takeSecond, reverse=True)
# print "---------------------------"
# print "grado medio"
# print (2*(g.number_of_edges())/g.number_of_nodes())


#BARABASI
ba = nx.barabasi_albert_graph(15598, 14)
degree_sequenceBA = sorted([d for n, d in ba.degree()], reverse=True)  # degree sequence
degreeCountBA = collections.Counter(degree_sequenceBA)
degBA, cntBA = zip(*degreeCountBA.items())
#ERDOS RENYI
er = nx.erdos_renyi_graph(15598, 0.005)
degree_sequenceER = sorted([d for n, d in er.degree()], reverse=True)  # degree sequence
degreeCountER = collections.Counter(degree_sequenceER)
degER, cntER = zip(*degreeCountER.items())

#GRAFO Diretto
# # IN
degree_sequenceIn = sorted([d for n, d in h.in_degree()], reverse=True)  # degree sequence
degreeCountIn = collections.Counter(degree_sequenceIn)
degIn, cntIn = zip(*degreeCountIn.items())
# # OUT
degree_sequenceOut = sorted([d for n, d in h.out_degree()], reverse=True)  # degree sequence
degreeCountOut = collections.Counter(degree_sequenceOut)
degOut, cntOut = zip(*degreeCountOut.items())
# #plt.loglog(degree_sequenceIn,'bo')
# plt.loglog(degree_sequenceOut,'bo')
for i in range(len(degree_sequenceOut)):
    print (degree_sequenceOut[i])

#GRAFO VECCHIO
degree_sequenceOld = sorted([d for n, d in g.degree()], reverse=True)  # degree sequence
degreeCountOld = collections.Counter(degree_sequenceOld)
degOld, cntOld = zip(*degreeCountOld.items())

degree_sequence = sorted([d for n, d in h.degree()], reverse=True)  # degree sequence
#print "Degree sequence", degree_sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())

#  fig, ax = plt.subplots()
#plt.bar(deg, cnt, width=0.80, color='b')

#plt.bar(degER, cntER, width=0.80, color='r')
#plt.bar(degBA, cntBA, width=0.80, color='g')
#plt.bar(degOld, cntOld, width=0.80, color='b')
plt.bar(degIn, cntIn, width=0.80, color='r')
plt.bar(degOut, cntOut, width=0.80, color='b')


# #plt.plot(deg, cnt, 'r--', deg2, cnt2, 'bs', deg3, cnt3, 'g^')
#plt.loglog(degree_sequenceOld,'bo')
#plt.loglog(degree_sequenceER,'ro')
#plt.loglog(degree_sequenceBA,'go')
#plt.loglog(degree_sequence,'ko')

# plt.title("Degree Histogram")
# plt.ylabel("Count")
# plt.xlabel("Degree")
# # ax.set_xticks([d for d in deg])
# # ax.set_xticklabels(deg)

#plt.show()

# print (nx.density(g))
# print (nx.density(ba))

# print "---------------------------"
# print "Numero componenti connesse"
# print nx.number_connected_components(g)
# print "---------------------------"
# print "Lista delle componenti connesse"
# gcc = nx.connected_components(g)
# k = 0
# for item in gcc:
#     if(k==0):
#         c1 = g.subgraph(item)
#     else:
#         c2 = g.subgraph(item)
#     k = k+1
# print c1.number_of_nodes()
# print c2.number_of_nodes()
# print #list(nx.connected_components(g))
# # print "---------------------------"
# # print "Lista nodi per grado"
# # print sorted([d for n, d in g.degree()], reverse=True) 
# print "---------------------------"
# print "Clustering"
# #print sorted(nx.clustering(g), reverse=True) 
# print 
# print "---------------------------"
# print "Shortest paths"
# # sp = dict(nx.all_pairs_shortest_path(g)) BLOCCA il mio computer!!!
# # print sp[1]

# print "---------------------------"
# print "Average Clustering coefficient"
# print nx.average_clustering(g)


# print "---------------------------"
# print "Diameter"
# print "1 componente"
# #print nx.diameter(c1)
# print "2 componente"
# #print nx.diameter(c2)

# print "---------------------------"
# print "Betweenness centrality"
# #print sorted(nx.betweenness_centrality(g), key=takeSecond, reverse=True) 

# print "---------------------------"
# print "Density"
# print nx.density(g)

# print "---------------------------"
# print "self loop"
# print list(nx.selfloop_edges(g))


# print "---------------------------"
# print "Rimozione di un nodo con maggiore degree"
print(g.number_of_nodes())
print(g.number_of_edges())

cancellati = []

for item in g.degree():
    if item[1]<=5:
        #print(item)
        cancellati.append(item[0])
        
for n in cancellati:
    g.remove_node(n)

print(g.number_of_nodes())
print(g.number_of_edges())


degree_sequenceNew = sorted([d for n, d in g.degree()], reverse=True)  # degree sequence
#plt.loglog(degree_sequenceNew,'ro')

plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")

plt.show()
# g.remove_node("https://www.kobo.com/it/it/ebook/rose-66")
# print "---------------------------"
# print "Numero di nodi"
# print g.number_of_nodes()
# print "---------------------------"
# print "Numero di archi"
# print g.number_of_edges()
# print "---------------------------"
# print "Numero componenti connesse"
# print nx.number_connected_components(g)

# gcc = nx.connected_components(g)
# for item in gcc:
#     print len(item)
