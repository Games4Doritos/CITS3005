from rdflib import Graph, Literal, RDF, BNode, Namespace
from rdflib.namespace import FOAF, XSD

g = Graph()

base = "http://cits3005.RE.org/"

RE = Namespace(base)
Character = Namespace(f"{base}character/")
Location = Namespace(f"{base}location/")
Place = Namespace(f"{base}place/")
Organisation = Namespace(f"{base}organisation/")
Virus = Namespace(f"{base}virus/")
BioOrganicWeapon = Namespace(f"{base}bioOrganicWeapon/")
IrregularMutant = Namespace(f"{base}irregularMutant/")

g.bind("re", RE)
g.bind("character", Character)
g.bind("location", Location)
g.bind("place", Place)
g.bind("organisation", Organisation)
g.bind("virus", Virus)
g.bind("b.o.w", BioOrganicWeapon)
g.bind("irregularMutant", IrregularMutant)
g.bind("foaf", FOAF)
g.bind("rdf", RDF)

leonK = Character.leonKennedy
claireR = Character.clairRedfield
marvinB = Character.marvinBranagh
williamB = Character.williamBirkin
sherryB = Character.sherryBirkin
adaW = Character.adaWong
brianI = Character.brianIrons
benB = Character.benBertolucci 
robertK = Character.robertKendo
emmaK = Character.emmaKendo
annetteB = Character.annetteBirkin

uncertainAge = BNode()
uncertainOutcome = BNode()

g.add((leonK, RDF.type, RE.character))
g.add((leonK, FOAF.name, Literal("Leon Scott Kennedy")))
g.add((leonK, FOAF.age, Literal(21, datatype=XSD.integer)))
g.add((leonK, RE.occupation, Literal("Rookie Police Officer")))
g.add((leonK, RE.outcome, Literal("Survived and Escaped")))

g.add((claireR, RDF.type, RE.character))
g.add((claireR, FOAF.name, Literal("Claire Redfield")))
g.add((claireR, FOAF.age, Literal(19, datatype=XSD.integer)))
g.add((claireR, RE.occupation, Literal("College Student")))
g.add((claireR, RE.outcome, Literal("Survived and Escaped")))

g.add((marvinB, RDF.type, RE.character))
g.add((marvinB, FOAF.name, Literal("Marvin Branagh")))
g.add((marvinB, FOAF.age, uncertainAge))
g.add((marvinB, RE.occupation, Literal("Police Lieutenant")))
g.add((marvinB, RE.outcome, Literal("Turns into a zombie")))

g.add((williamB, RDF.type, RE.character))
g.add((williamB, FOAF.name, Literal("William Birkin")))
g.add((williamB, FOAF.age, Literal(36, datatype=XSD.integer)))
g.add((williamB, RE.occupation, Literal("Chief Virologist and Researcher")))
g.add((williamB, RE.outcome, Literal("Killed as G")))

g.add((sherryB, RDF.type, RE.character))
g.add((sherryB, FOAF.name, Literal("Sherry Birkin")))
g.add((sherryB, FOAF.age, Literal(12, datatype=XSD.integer)))
g.add((sherryB, RE.outcome, Literal("Survived and Escaped")))

g.add((adaW, RDF.type, RE.character))
g.add((adaW, FOAF.name, Literal("Ada Wong")))
g.add((adaW, FOAF.age, uncertainAge))
g.add((adaW, RE.occupation, Literal("Spy")))
g.add((adaW, RE.outcome, uncertainOutcome))

g.add((brianI, RDF.type, RE.character))
g.add((brianI, FOAF.name, Literal("Brian Irons")))
g.add((brianI, FOAF.age, uncertainAge))
g.add((brianI, RE.occupation, Literal("Chief of Police")))
g.add((brianI, RE.outcome, Literal("Dies to G-Virus parasites")))

g.add((benB, RDF.type, RE.character))
g.add((benB, FOAF.name, Literal("Ben Bertolucci")))
g.add((benB, FOAF.age, Literal(26, datatype=XSD.integer)))
g.add((benB, RE.occupation, Literal("Freelance Investigative Journalist")))
g.add((benB, RE.outcome, Literal("Killed by T-00")))

g.add((robertK, RDF.type, RE.character))
g.add((robertK, FOAF.name, Literal("Robert Kendo")))
g.add((robertK, FOAF.age, Literal(40, datatype=XSD.integer)))
g.add((robertK, RE.occupation, Literal("Gun Shop Owner")))
g.add((robertK, RE.outcome, uncertainOutcome))

g.add((emmaK, RDF.type, RE.character))
g.add((emmaK, FOAF.name, Literal("Emma Kendo")))
g.add((emmaK, FOAF.age, Literal(10, datatype=XSD.integer)))
g.add((emmaK, RE.outcome, uncertainOutcome))

g.add((annetteB, RDF.type, RE.character))
g.add((annetteB, FOAF.name, Literal("Annette Birkin")))
g.add((annetteB, FOAF.age, uncertainAge))
g.add((annetteB, RE.occupation, Literal("Researcher")))
g.add((annetteB, RE.outcome, Literal("Becomes G after G-Virus injection")))

rc = Location.raccoonCity

g.add((rc, RDF.type, RE.location))
g.add((rc, FOAF.name, Literal("Raccoon City, USA")))

rPS = Place.rPS
kGS = Place.kendoGunShop
rORP = Place.rORP
sewers = Place.sewers
nest = Place.nest

g.add((rPS, RDF.type, RE.place))
g.add((rPS, FOAF.name, Literal("Raccoon City Police Station")))
g.add((rPS, RE.locatedAt, rc))

g.add((kGS, RDF.type, RE.place))
g.add((kGS, FOAF.name, Literal("Kendo Gun Shop")))
g.add((kGS, RE.locatedAt, rc))

g.add((rORP, RDF.type, RE.place))
g.add((rORP, FOAF.name, Literal("Raccoon City Orphanage")))
g.add((rORP, RE.locatedAt, rc))

g.add((sewers, RDF.type, RE.place))
g.add((sewers, FOAF.name, Literal("The Sewers")))
g.add((sewers, RE.locatedAt, rc))

g.add((nest, RDF.type, RE.place))
g.add((nest, FOAF.name, Literal("NEST")))
g.add((nest, RE.locatedAt, rc))

rpd = Organisation.rpd
umbrella = Organisation.umbrella

g.add((rpd, RDF.type, RE.organisation))
g.add((rpd, FOAF.name, Literal("Raccoon City Police Department")))
g.add((rpd, FOAF.status, Literal("Dismantled")))
g.add((rpd, FOAF.based_near, rPS))

g.add((umbrella, RDF.type, RE.organisation))
g.add((umbrella, FOAF.name, Literal("Umbrella Corporation")))
g.add((umbrella, FOAF.status, Literal("Operational")))
g.add((umbrella, FOAF.based_near, nest))

uncertainOrg = BNode()

g.add((leonK, FOAF.member, rpd))
g.add((marvinB, FOAF.member, rpd))
g.add((williamB, FOAF.member, umbrella))
g.add((adaW, FOAF.member, uncertainOrg))
g.add((brianI, FOAF.member, rpd))
g.add((annetteB, FOAF.member, umbrella))

g.add((robertK, FOAF.based_near, kGS))
g.add((brianI, FOAF.based_near, rORP))

tVirus = Virus.tVirus
gVirus = Virus.gVirus

g.add((tVirus, RDF.type, RE.virus))
g.add((tVirus, FOAF.name, Literal("Tyrant Virus")))
g.add((tVirus, FOAF.nick, Literal("T-Virus")))
g.add((tVirus, RE.producedBy, umbrella))

g.add((gVirus, RDF.type, RE.virus))
g.add((gVirus, FOAF.name, Literal("Golgotha Virus")))
g.add((gVirus, FOAF.nick, Literal("G-Virus")))
g.add((gVirus, RE.producedBy, umbrella))

g.add((marvinB, RE.infectee, tVirus))
g.add((emmaK, RE.infectee, tVirus))

g.add((williamB, RE.infectee, gVirus))
g.add((sherryB, RE.infectee, gVirus))

t_00 = BioOrganicWeapon.t_00
licker = BioOrganicWeapon.licker
plant43 = BioOrganicWeapon.plant43

g.add((t_00, RDF.type, RE.bioOrganicWeapon))
g.add((t_00, FOAF.name, Literal("T-00")))
g.add((t_00, FOAF.nick, Literal("Mr. X")))
g.add((t_00, RE.formedFrom, tVirus))
g.add((t_00, RE.producedBy, umbrella))
g.add((t_00, RE.outcome, Literal("Killed")))

g.add((licker, RDF.type, RE.bioOrganicWeapon))
g.add((licker, FOAF.name, Literal("Licker")))
g.add((licker, RE.formedFrom, tVirus))
g.add((licker, RE.producedBy, umbrella))

g.add((plant43, RDF.type, RE.bioOrganicWeapon))
g.add((plant43, FOAF.name, Literal("Plant 43")))
g.add((plant43, RE.formedFrom, tVirus))
g.add((plant43, RE.producedBy, umbrella))

zombie = IrregularMutant.zombie
G = IrregularMutant.G
zombieDog = IrregularMutant.zombieDog
gCreature = IrregularMutant.gCreature
ivy = IrregularMutant.ivy

g.add((zombie, RDF.type, RE.irregularMutant))
g.add((zombie, FOAF.name, Literal("Zombie")))
g.add((zombie, RE.formedFrom, tVirus))

g.add((G, RDF.type, RE.irregularMutant))
g.add((G, FOAF.name, Literal("G")))
g.add((G, RE.formedFrom, gVirus))
g.add((G, RE.former, williamB))
g.add((G, RE.outcome, Literal("Decimated in an explosion")))

g.add((zombieDog, RDF.type, RE.irregularMutant))
g.add((zombieDog, FOAF.name, Literal("Zombie Dog")))
g.add((zombieDog, RE.formedFrom, tVirus))

g.add((gCreature, RDF.type, RE.irregularMutant))
g.add((gCreature, FOAF.name, Literal("G-Creature")))
g.add((gCreature, RE.formedFrom, gVirus))

g.add((ivy, RDF.type, RE.irregularMutant))
g.add((ivy, FOAF.name, Literal("Ivy")))
g.add((ivy, RE.formedFrom, plant43))

q1 = """
SELECT ?e
WHERE {
    ?e re:formedFrom ?v.
    ?v rdf:type re:virus.
}"""

q2 = """
SELECT ?p
WHERE {
    {
        SELECT (MIN(?age) AS ?minAge) 
        WHERE {
            ?pSub rdf:type re:character.
            ?pSub foaf:age ?age.
            FILTER ( ! isBLANK(?age) ).
            ?pSub re:occupation ?oSub.
        }
    }
    ?p rdf:type re:character .
    ?p foaf:age ?minAge .
    ?p re:occupation ?o .
}
"""

q3 = """
SELECT ?e
WHERE {
    {
        ?e rdf:type re:bioOrganicWeapon.
        ?e re:formedFrom virus:tVirus.
    }
    UNION
    {
        ?e rdf:type re:irregularMutant.
        ?e re:formedFrom virus:tVirus.
    }
}
"""

q4 = """
SELECT ?v (COUNT(?e) AS ?numFormed) 
WHERE {
    ?v rdf:type re:virus .
    ?e re:formedFrom ?v .
}
GROUP BY ?v
ORDER BY DESC(?numFormed)
LIMIT 1
"""

q5 = """
SELECT ?p
WHERE {
    ?p rdf:type re:character.
    ?p foaf:name ?n.
    FILTER REGEX(?n, "Birkin$")  
}
"""

q6 = """
SELECT (COUNT(?p) as ?numChar)
WHERE {
    ?p rdf:type re:character.
    ?p foaf:member ?o.
    ?o foaf:status "Operational".
}
"""


#Queries

q1Res = g.query(q1)
q2Res = g.query(q2)
q3Res = g.query(q3)
q4Res = g.query(q4)
q5Res = g.query(q5)
q6Res = g.query(q6)

# For query printing (change q number)
for i in q1Res:
    print(i)


# XML file generator
#g.serialize("RE2.xml", format="xml")

"""
#Visualisation

import matplotlib.pyplot as plt
import networkx as nx

grap = nx.DiGraph()

for s, p, o in g:
    s_label = s.split('/')[-1] or str(s)
    o_label = o.split('/')[-1] or str(o)
    p_label = p.split('#')[-1].split('/')[-1] or str(p)

    
    grap.add_edge(s_label, o_label, label=p_label)

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(grap) 

colours = [("skyblue" if grap.adj[s] == {} else "red") for s in grap.adj]

nx.draw(grap, pos, with_labels=True, node_color=colours, node_size=2000, font_size=10, font_weight="bold", arrows=True)

edge_labels = nx.get_edge_attributes(grap, 'label')
nx.draw_networkx_edge_labels(grap, pos, edge_labels=edge_labels, font_color='red')

plt.show()
"""