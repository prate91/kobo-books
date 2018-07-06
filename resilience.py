import csv
import networkx as nx
import collections
import matplotlib.pyplot as plt
import timeCount
from random import choice

def takeSecond(elem):
    return elem[1]

# RANDOM REMOVE
def randomRemove(graph, n):
    
    filename = "randomAttack.csv"

    f = open(filename, "w")
    nodes = list(graph.nodes())
    random_nodes = []
    for i in range(n):
        random_node = choice(nodes)
        nodes.remove(random_node)
        random_nodes.append(random_node)
    j=1
    for item in random_nodes:
        graph.remove_node(item)
        f.write(str(nx.number_connected_components(graph)))
        f.write("\n")
        j=j+1

# TOP REMOVE
def topRemove(graph, n):
    filename =  "topAttack.csv"

    f = open(filename, "w")

    R = nx.Graph()
    R = graph.copy()   
    higtdeg10 = []
    toRemove = []
    for i in range(n):
        deg_dist = sorted(R.degree(), key=takeSecond, reverse=True)
        higtdeg10.append(deg_dist[0])
        node_to_remove = list(zip(*higtdeg10))[0]
        toRemove.append(node_to_remove[i])
        R.remove_node(node_to_remove[i])
    j=1
    for item in toRemove:
        graph.remove_node(item)
        f.write(str(nx.number_connected_components(graph)))
        f.write("\n")
        j=j+1

# Degree removed

def degreeRemove(graph, n):
    filename = "degreeAttack.csv"

    f = open(filename, "w")

    deg_cen = nx.degree_centrality(graph)
    higtdeg_cen10 = []

    #lista = sorted(deg_cen, key=takeSecond, reverse=True)
    i=0
    for k in sorted(deg_cen.items(), key=takeSecond, reverse=True):
        if i<n:
            higtdeg_cen10.append(k[0])
        i=i+1
    j=1
    for item in higtdeg_cen10:
        graph.remove_node(item)
        f.write(str(nx.number_connected_components(graph)))
        f.write("\n")
        j=j+1




# Community menu
def resilience_menu():      
    print (10 * "-" , "MENU" , 10 * "-")
    print ("1. Top attack")
    print ("2. High degree attack")
    print ("3. Random attack")
    print ("4. Exit")
    print (27 * "-")
  

def resilience(graph, start):
    
    loop=True      

    while loop:          
        resilience_menu()   
        choice = input("Enter your choice [1-4]: ")
        
        if choice=='1':
            print ("Calculate and print Top attack")
            iteration = input("Enter number of iteration: ")
            iteration = int(iteration)
            topRemove(graph, iteration)
            print(str(timeCount.getTime(start))+"s")
        elif choice=='2':
            print ("Calculate and print high degree attack")
            iteration = input("Enter number of iteration: ")
            iteration = int(iteration)
            degreeRemove(graph, iteration)
            print(str(timeCount.getTime(start))+"s")
        elif choice=='3':
            print ("Calculate and print high degree attack")
            iteration = input("Enter number of iteration: ")
            iteration = int(iteration)
            randomRemove(graph, iteration)
            print(str(timeCount.getTime(start))+"s")
        elif choice=='4':
            print ("Exit")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            input("Wrong option selection. Enter any key to try again.. \n")

