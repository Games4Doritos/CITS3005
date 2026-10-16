from owlready2 import *

"""



"""

def main():
    onto = get_ontology("onto.owl").load()
    
    with onto:
        sync_reasoner()
    
  
    for i in onto.hasMajors.get_relations():
        print(i)





if __name__ == "__main__":
    main()