import spreadingSI
import spreadingSIS
import spreadingSIR

# Graph menu
def spreading_menu():      
    print (10 * "-" , "MENU" , 10 * "-")
    print ("1. SI")
    print ("2. SIS")
    print ("3. SIR")
    print ("4. Exit")
    print (27 * "-")
  

def spreading(graph):

    loop=True      

    while loop:          
        spreading_menu()   
        choice = input("Enter your choice [1-4]: ")
        
        if choice=='1':
            n = input("Enter number of iteration: ")
            iteration = int(n)
            spreadingSI.siModel(graph, iteration)
        elif choice=='2':
            n = input("Enter number of iteration: ")
            iteration = int(n)
            spreadingSIS.sisModel(graph, iteration)
        elif choice=='3':
            n = input("Enter number of iteration: ")
            iteration = int(n)
            spreadingSIR.sirModel(graph, iteration)
        elif choice=='4':
            print ("Exit")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            input("Wrong option selection. Enter any key to try again.. \n")
