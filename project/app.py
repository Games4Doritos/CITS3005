from owlready2 import *
import owlready2

owlready2.JAVA_EXE = r"C:\Program Files\Java\jdk-25.0.4.1\bin\java.exe"

def nameList(lis):
    return list(map(lambda x:x.name, lis))

def printVisualList(lis):
    if len(lis) == 0:
        return
    print(lis[0], end="")
    for i in lis:
        if lis.index(i) != 0:
            print(f", {i}", end="")
    print()

def main():
    onto = get_ontology("onto.owl").load()
    
    with onto:
        sync_reasoner_pellet(infer_property_values=True)
    print("[======================================================================================]")
    
    while True:
        
        inp = input(": ")
        expr = inp.split()
    
        if len(expr) < 2:
            print("Error: Too few arguments provided")
            continue
        
        if expr[0] == "q":
            print("Quitting...")
            breakpoint
        
        if expr[0] == "get":
            if expr[1] == "class":
                if len(expr) == 2:
                    printVisualList(nameList(list(onto.classes())))
                elif len(expr) == 3:
                    try:
                        clas = getattr(onto, expr[2])
                        printVisualList(nameList(clas.instances()))
                        
                    except:
                        print('Error: Non-existent class')
                else:
                    print("Error: Too many arguments")
                    
            elif expr[1] == "prop":
                if len(expr) == 2:
                    printVisualList(nameList(list(onto.properties())))
                elif len(expr) == 3:
                    try:
                        prop = getattr(onto, expr[2])
                        printVisualList(list(prop.get_relations()))
                        
                    except:
                        print('Error: Non-existent property')
                else:
                    print("Error: Too many arguments")
            elif expr[1] == "inst":  
                if len(expr) == 2:
                    print("Error: Third argument for instance name not provided")
                elif len(expr) == 3:
                    try:
                        inst = getattr(onto, expr[2])
                        print(inst)
                    except:
                        print('Error: Non-existent instance')
                elif len(expr) == 4:
                    try:
                        instProp = getattr(getattr(onto, expr[2]), expr[3])
                        print(instProp)
                    except:
                        print('Error: Non-existent instance property')
                else:
                    print("Error: Too many arguments")
            else:
                break
            
        elif expr[0] == "add":
            try:
                init = getattr(onto, expr[1])
                newInst = init(expr[2])
                print(newInst)
            
            except:
                print("Error: Invalid Arguments")
        
        else:
            print("Error: Invalid Command")
        
        
        




if __name__ == "__main__":
    main()