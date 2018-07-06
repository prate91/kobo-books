import csv
import networkx as nx
import collections
import matplotlib
import matplotlib.pyplot as plt
import buildGraph
import timeCount
import plotCentralityMesaures

# compute the network analysis and print a file
def networkAnalysis(graph):

    filename = input("Enter filename: ")
    
    filenames = filename.split(".")
    filenameNodes = filenames[0] + ".txt"
    # set print filename
    #filenameNodes = "networkAnalysis.txt"
    f = open(filenameNodes, "w")

    giant = greatestCC(graph)

    highDegree = highestDegree(graph)

    f.write("-----------------------------------------------------"+"\n")
    f.write("\t\t\t\tNetwork Analysis "+"\n")
    f.write("-----------------------------------------------------"+"\n")
    f.write("Numero di nodi:\t\t\t\t" + str(graph.number_of_nodes())+"\n")
    f.write("Numero di archi:\t\t\t" + str(graph.number_of_edges())+"\n")
    f.write("Diretto:\t\t\t\t\t" + str(graph.is_directed())+"\n")
    f.write("Components:\t\t\t\t\t" + str(nx.number_connected_components(graph))+"\n")
    f.write("Size of largest component:\t" + str(giant.number_of_nodes())+"\n")
    f.write("Self loops:\t\t\t\t\t" + str(graph.number_of_selfloops())+"\n")
    f.write("Highest degree node:\t\t" + str(highDegree)+"\n")
    f.write("Density:\t\t\t\t\t" + str(nx.density(graph))+"\n")
    f.write("Clustering coefficient:\t\t" + str(nx.average_clustering(graph))+"\n")
    f.write("Average degree:\t\t\t\t" + str(2*(graph.number_of_edges())/graph.number_of_nodes())+"\n")
    f.write("-----------------------------------------------------"+"\n")

    f.close()

    filenameClustering = "clusteringCoefficient.txt"
    sortMesaure("clusteringCoefficient", clusteringCoefficient(graph))
    plotCentralityMesaures.plotCentrality("clusteringCoefficient.txt", graph)

# print centrality mesaures 
def sortMesaure(filename, mesaure):
    
    filename = filename + ".txt"

    f = open(filename, "w")

    for k, v in sorted(mesaure.items(), key=takeSecond, reverse=True):
        f.write(str(k) +"\t"+ str(v) + "\n")
    
    f.close()



def takeSecond(elem):
    return elem[1]

def clusteringCoefficient(graph):
    clu = nx.clustering(graph)
    return clu

def greatestCC(graph):
    gcc = nx.connected_components(graph)
    max = 0
    for item in gcc:
        if len(item) > max:
            max = len(item)
            giant = graph.subgraph(item)
    return giant

#print (sorted(G.degree(), key=takeSecond, reverse=True))

def highestDegree(graph):
    degree_sequence = sorted([d for n, d in graph.degree()], reverse=True)
    highDegree = degree_sequence[0]
    return highDegree



