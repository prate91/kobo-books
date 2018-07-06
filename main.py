import networkAnalysis
import timeCount
import buildGraph
import centralityMesaures
import communityDiscover
import communityQuality
import resilience
import spreading


# Graph menu
def main_menu():      
    print (10 * "-" , "MENU" , 10 * "-")
    print ("1. Network analysis")
    print ("2. Centrality mesaures")
    print ("3. Community discover")
    print ("4. Community quality")
    print ("5. Resilience")
    print ("6. Spreading")
    print ("7. Exit")
    print (27 * "-")
  

def mainMenu():

    loop=True      

    while loop:          
        main_menu()   
        choice = input("Enter your choice [1-7]: ")
        
        if choice=='1':
            networkAnalysis.networkAnalysis(graph)
        elif choice=='2':
            centralityMesaures.centralityMesures(graph, start)
        elif choice=='3':
            communityDiscover.communityDiscover(graph, start)
        elif choice=='4':
            communityQuality.communityQuality(graph, start)
        elif choice=='5':
            resilience.resilience(graph, start)
        elif choice=='6':
            spreading.spreading(graph)
        elif choice=='7':
            print ("Exit")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            input("Wrong option selection. Enter any key to try again.. \n")




start = timeCount.startTime()

graph = buildGraph.chooseGraph()

mainMenu()



    
