# CITS3005 Homework 2 Descriptions

My Knowledge Graph is being built for the fictional world in the survival horror game: Resident Evil 2 (2019)  
This game entails protagonists Leon S. Kennedy and Claire Redfield trying to survive the T-Virus zombie outbreak in Raccoon City moving through different places and working together with (or conflicting with) other survivors, to ultimately uncover dark secrets and escape.  
It purely touches on a large subset of the setting, and story of what happens within the game, mainly describing properties and associations. Any applicable knowledge from previous or other games in the series will not be regarded.  

## Types
**Character**: A character seen in the game. Can include persons, zombies and bioweapons (enemies that aren’t directly human)  
**Location**: A location seen in the game. This can roughly include a city, state or country  
**Place**: A place seen in the game. Can include specific buildings or facilities  
**Organisation**: Broadly encapsulates any organisation, business or corporation as an umbrella term.  
**Virus**: A virus that is known of or seen within the game.  
**Bio Organic Weapon**: A genetically altered organism created with the intent of either being used as military and paramilitary weapons, or created to further research into military and paramilitary weapons. Only for those that appear within the game.  
**Irregular Mutant**: A creature that has been mutated by exposure to a mutagenic virus or parasite, but which was not an intentional creation of a Bio Organic Weapon project. Only those that appear within the game  

## Relations
(A, RDF.type, B): A is of type B.  
(A, FOAF.name, B): A has name B  
(A, FOAF.age, B): A is age B  
(A, RE.occupation, B): A has occupation B  
(A, RE.outcome, B): The outcome of A is B  
(A, RE.locatedAt, B): A is located at B  
(A, FOAF.status, B): A has status B  
(A, FOAF.based_near, B): A is based near B  
(A, FOAF.member, B): A is a member of B  
(A, FOAF.nick, B): A is nicknamed B  
(A, RE.infectee, B): A has been infected by B during at least some time during the events of the game (as a minimum)  
(A, RE.formedFrom, B): A contains, was produced from, or has mutated from B  
(A, RE.former, B): A was formerly B, in a previous time  
(A, RE.producedBy, B): A was produced by B  

## Useful Queries
(Modelled as q1-6 in REQuery.py)  

Find every entity that is formed from a virus  
Find the youngest character(s) with an occupation and a known age  
Find the total number of Bio Organic Weapons and Irregular Mutants that are formed from the T-Virus  
Find the virus that the maximum number of entities is formed from  
Find every character with last name Birkin  
Find the number of characters that are members of an ‘Operational’ organisation  