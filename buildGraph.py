import csv
import networkx as nx

def makeGraph(filename):
    # initialize a new graph
    G = nx.Graph()

    # open a csv reader
    f1 = csv.reader(open(filename,"r"))

    # add edges and nodes for every row
    for row in f1:
        G.add_edge(row[0],row[1])

    return G

# Barabasi-Albert 
def makeBA(nodes, pattach):
    ba = nx.barabasi_albert_graph(nodes, pattach)
    return ba

# Erdos-Renyi
def makeER(nodes, prob):
    er = nx.erdos_renyi_graph(nodes, prob)
    return er


# Graph menu
def graph_menu():      
    print (10 * "-" , "MENU" , 10 * "-")
    print ("1. Kobo-books")
    print ("2. Authors")
    print ("3. Barabasi-Albert")
    print ("4. Erdos-Renyi")
    print ("5. Exit")
    print (27 * "-")
  

def chooseGraph():

    loop=True      

    while loop:          
        graph_menu()   
        choice = input("Enter your choice [1-5]: ")
        
        if choice=='1':
            return makeGraph("deepNetworkClean.csv")
        elif choice=='2':
            return makeGraph("deepAuthors.csv")
        elif choice=='3':
            return makeBA(15598, 14)
        elif choice=='4':
            return makeER(15598,0.005)
        elif choice=='5':
            print ("Exit")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            input("Wrong option selection. Enter any key to try again.. \n")