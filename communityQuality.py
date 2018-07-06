from nf1 import NF1
import networkx as nx
from networkx.algorithms import community
import pquality
import csv
import demon as d
import numpy
import timeCount
import communityDiscover
import re



def readCommunities(filename):
    with open(filename) as f:
        communities = tuple(f.read().splitlines())
    comms = []
    for community in communities:
        c = community.split(',')
        com = ()
        for w in c:
            w = re.sub(r'[\[\]]', '', w)
            w = int(w)
            com = com + (int(w),)
        comms.append(com)
    return comms


def qualityScores(communities, graph):

    g = nx.convert_node_labels_to_integers(graph,first_label=2)
    coms = [tuple(x) for x in communities]
    scores = pquality.pquality_summary(g, coms)
    print(scores['Indexes'])
    print(scores['Modularity'])


# Computing the NF1 scores and statistics
def NF1scores(filenames):
    communities = []
    for filename in filenames:
        comm = readCommunities(filename)
        comms = [tuple(x) for x in comm]
        communities.append(comms)
    nf = NF1(communities[0], communities[1])
    results = nf.summary()
    print(results['scores'])
    print(results['details'])


    # Visualising the Precision-Recall density scatter-plot
    nf.plot()


# Community menu
def quality_menu():      
    print (10 * "-" , "MENU" , 10 * "-")
    print ("1. pquality")
    print ("2. NF1")
    print ("3. Exit")
    print (27 * "-")
  

def communityQuality(graph, start):

    loop=True      

    while loop:          
        quality_menu()   
        choice = input("Enter your choice [1-3]: ")
        
        if choice=='1':
            filename = input("Enter name of community file: ")   
            print ("pquality on " + filename)
            communities = readCommunities(filename)
            qualityScores(communities, graph)
            print(str(timeCount.getTime(start))+"s")
        elif choice=='2':
            filenames = []
            i=0
            while i<2:
                filename = input("Enter name of community files: ")
                filenames.append(filename)
                i=i+1
            print ("NF1 scores on " + filename)
            NF1scores(filenames)
            print(str(timeCount.getTime(start))+"s")
        elif choice=='3':
            print ("Exit")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            input("Wrong option selection. Enter any key to try again.. \n")



