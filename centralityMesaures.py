import csv
import networkx as nx
import collections
import matplotlib.pyplot as plt
import plotCentralityMesaures
import buildGraph
import timeCount


def takeSecond(elem):
    return elem[1]

# Degree centrality
def degreeCentrality(graph):
    print("Start degree centrality")
    deg_cen = nx.degree_centrality(graph)
    print("Finish degree centrality")
    return deg_cen

# Betweenness centrality
def betweennessCentrality(graph):
    print("Start betweenness centrality")
    bet_cen = nx.betweenness_centrality(graph)
    print("Finish betweenness centrality")
    return bet_cen

# Closeness centrality
def closenessCentrality(graph):
    print("Start closeness centrality")
    clo_cen = nx.closeness_centrality(graph)
    print("Start closeness centrality")
    return clo_cen

# print centrality mesaures 
def sortCentralityMesaure(filename, centrality):
    
    filename = filename + ".txt"

    f = open(filename, "w")

    for k, v in sorted(centrality.items(), key=takeSecond, reverse=True):
        f.write(str(k) +"\t"+ str(v) + "\n")
    
    f.close()

# Centrality menu
def centrality_menu():      
    print (10 * "-" , "MENU" , 10 * "-")
    print ("1. Degree centrality")
    print ("2. Betweenness centrality")
    print ("3. Closeness centrality")
    print ("4. Exit")
    print (27 * "-")
  

def centralityMesures(graph, start):

    loop=True      

    while loop:          
        centrality_menu()   
        choice = input("Enter your choice [1-4]: ")
        
        if choice=='1':     
            print ("Calculate and print degree centrality")
            sortCentralityMesaure("degreeCentrality", degreeCentrality(graph))
            print(str(timeCount.getTime(start))+"s")
            plotCentralityMesaures.plotCentrality("degreeCentrality.txt", graph)
        elif choice=='2':
            print ("Calculate and print betweenness centrality")
            sortCentralityMesaure("betweennessCentrality", betweennessCentrality(graph))
            print(str(timeCount.getTime(start))+"s")
            plotCentralityMesaures.plotCentrality("betweennessCentrality.txt", graph)
        elif choice=='3':
            print ("Calculate and print closeness centrality")
            sortCentralityMesaure("closenessCentrality", closenessCentrality(graph))
            print(str(timeCount.getTime(start))+"s")
            plotCentralityMesaures.plotCentrality("closenessCentrality.txt", graph)
        elif choice=='4':
            print ("Exit")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            input("Wrong option selection. Enter any key to try again.. \n")

