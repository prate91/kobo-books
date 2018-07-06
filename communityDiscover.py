from networkx.algorithms.community import k_clique_communities
from networkx.algorithms.community import label_propagation_communities
from networkx.algorithms.community import girvan_newman
from networkx.algorithms import community
import community as louvain
import csv
import networkx as nx
import collections
import matplotlib.pyplot as plt
import itertools
import tqdm
import demon as d
import pquality
from collections import Counter
from collections import defaultdict
import timeCount

def takeSecond(elem):
    return elem[1]

def printCommunities(communities, filename):
    filename = filename + ".txt"

    f = open(filename, "w")

    for community in communities:
        f.write(str(list(community)))
        f.write("\n")
    
    f.close()

def overlapNodes(communities):
    overlap = {}
    for community in communities:
        for node in community:
            if node in overlap.keys():
                overlap[node] += 1
            else:
                overlap[node] = 1
    return overlap

def numberOfCommunities(communities):
    return len(communities)

def numberOfNodesCommunities(communities):
    coms = []
    for community in communities:
        coms.append(len(community))    
    return coms

def sortDictionary(dictionary):
    for k, v in sorted(dictionary.items(), key=takeSecond, reverse=True):
        print (k, v)


def communitiesCSV(communities, filename):

    filename = filename + ".csv"

    f = open(filename, "w")

    i = 1
    for community in communities:
        for node in community:
            f.write(str(node) +";"+ str(i))
        i=i+1

# K CLIQUE
def kClique(graph, k):
    k = list(k_clique_communities(graph, k))
    return k


# LABEL PROPAGATION
def labelPropagation(graph):
    lps = list(community.label_propagation_communities(graph))
    return lps

# DEAMON
def demon(graph, epsilon):
    dm = d.Demon(graph=graph, epsilon=epsilon, min_community_size=3)
    coms = dm.execute()
    dcoms = list(coms)
    return dcoms

# LOUVAIN
def louvainCommunities(graph):
    coms = louvain.best_partition(graph)

    # Reshaping the results to make them in the same format of the other CD algorithms
    coms_to_node = defaultdict(list)
    for n, c in coms.items():
        coms_to_node[c].append(n)

    coms_louvain = [tuple(c) for c in coms_to_node.values()]

    return list(coms_louvain)

# GIRVAN NEWMAN
def girvanNewman(graph):
    k = 10
    comp = girvan_newman(graph)
    limited = itertools.takewhile(lambda c: len(c) <= k, comp)
    for communities in limited:
        return (tuple(sorted(c) for c in communities)) 



# Community menu
def community_menu():      
    print (10 * "-" , "MENU" , 10 * "-")
    print ("1. K-Clique")
    print ("2. Label propagation")
    print ("3. Deamon")
    print ("4. Louvain")
    print ("5. Girvan Newman")
    print ("6. Exit")
    print (27 * "-")
  

def communityDiscover(graph, start):
    numeric = input("If you want numeric nodes partition type Y: ")
    if (numeric=='Y')|(numeric=='y'):
        graph = nx.convert_node_labels_to_integers(graph,first_label=2)
    
    loop=True      

    while loop:          
        community_menu()   
        choice = input("Enter your choice [1-6]: ")
        
        if choice=='1':
            val = input("Enter k > 54: ")
            k = int(val)
            if k > 54:   
                print ("Calculate and print K-Clique communities partition")
                filename = "kclique" + str(k)
                printCommunities(kClique(graph, k), filename)
                print(str(timeCount.getTime(start))+"s")
        elif choice=='2':
            print ("Calculate and print Label propagation communities partition")
            filename = "labelPropagation"
            printCommunities(labelPropagation(graph), filename)
            print(str(timeCount.getTime(start))+"s")
        elif choice=='3':
            val = input("Enter epsilon (0,1): ")
            epsilon = float(val)
            if (epsilon > 0 )|(epsilon < 1):   
                print ("Calculate and print Demon communities partition")
                print ("epsilon = " + str(epsilon))
                filename = "demon" + str(epsilon)
                printCommunities(demon(graph, epsilon), filename)
                print(str(timeCount.getTime(start))+"s")
        elif choice=='4':
            print ("Calculate and print Louvain communities partition")
            filename = "louvain"
            printCommunities(louvainCommunities(graph), filename)
            print(str(timeCount.getTime(start))+"s")
        elif choice=='5':
            print ("Calculate and print Girvan Newman communities partition")
            filename = "girvanNewman"
            printCommunities(girvanNewman(graph), filename)
            print(str(timeCount.getTime(start))+"s")
        elif choice=='6':
            print ("Exit")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            input("Wrong option selection. Enter any key to try again.. \n")


