from owlready2 import *
from rdflib import OWL, RDFS, Namespace
import owlready2
import json
import re

owlready2.JAVA_EXE = r"C:\Program Files\Java\jdk-25.0.4.1\bin\java.exe"

invalidChars = re.compile(u'[^\u0009\u000A\u000D\u0020-\uD7FF\uE000-\uFFFD\U00010000-\U0010FFFF]')

def invalidXML(string):
    return bool(invalidChars.search(string))

def sanitise(string):
    return invalidChars.sub('', string)

def parseData():
    onto = get_ontology("onto.owl").load()
    
    with onto:
        degreeMap = {} # key - code
        combinedDegreeMap = {} #for combined undergraduate only
        degreeTitleToCodeMap = {} # key - title
        majorMap = {} # key - code
        majorTitleToCodeMap = {} # key - title
        outcomeMap = {} # key - outcome desc
        unitMap = {} # key - code
        locationMap = {} # key - name
        modeMap = {} # key - name
        teachingPeriodMap = {} # key - name
        assessmentMap = {} # key - name
        contactMap = {} # key - "name int"
        contactTypeMap = {} # key - name
        
        with open("finalData/degrees.json", "r") as f:
            data = json.load(f)
            for key in data:
                deg = data[key]
                
                if deg['study_type'] == "Bachelor's course":
                    degreeMap[key] = onto.BachelorDegree(key)
                elif deg['study_type'] == "Honour's courses":
                    degreeMap[key] = onto.HonoursDegree(key)
                else:
                    degreeMap[key] = onto.CombinedBachelorDegree(key)
                    combinedDegreeMap[key] = degreeMap[key]
                # only degree types given in degrees.json are of Bachelors, Honours or Combined Bachelors
                
                cur = degreeMap[key]
                cur.hasDegreeCode = deg['code']
                cur.hasDegreeTitle = deg['title']
                degreeTitleToCodeMap[deg["title"]] = deg["code"]
                cur.hasDegreeSchool = deg['school']
                cur.hasTotalCreditPoints = deg['total_points']
                cur.hasStandardFullTimeDuration = deg['standard_full_time_completion']
                
                locations = deg['locations'].split(", ")
                for loc in locations:
                    if locationMap.get(loc) is None:
                        locInst = onto.Location(loc)
                        locationMap[loc] = locInst
                    cur.hasDegreeLocation.append(locationMap[loc])
        
        with open("finalData/majors.json", "r") as f:
            data = json.load(f)
            for key in data:
                maj = data[key]
                majorMap[key] = onto.Major(key)
                cur = majorMap[key]
              
                cur.hasMajorCode = maj['code']
                cur.hasMajorTitle = maj['title']
                majorTitleToCodeMap[maj['title']] = maj['code']
                cur.hasMajorSchool = maj['school']
                
                if invalidXML(maj['description']):
                    maj['description'] = sanitise(maj['description'])
                # only descriptions are known to contain chars invalid for xml 1.0
                # they are sanitised in the generation of the kg, not the transformation of the data (to preserve integrity where possible)
                cur.hasMajorDescription = maj['description']
                
                for out in maj['outcomes']:
                    if outcomeMap.get(out) is None:
                        outcome = onto.Outcome()
                        outcome.hasOutcomeDescription = out
                        outcomeMap[out] = outcome
                    cur.hasMajorOutcome.append(outcomeMap[out])
                
                for cour in maj['courses']:
                    if degreeMap.get(cour) is None:
                        if cour[:2] == "BP":
                            degreeMap[cour] = onto.BachelorDegree(cour)
                        elif cour[:2] == "BH":
                            degreeMap[cour] = onto.HonoursDegree(cour)
                        elif cour[:2] == "CB":
                            degreeMap[cour] = onto.CombinedBachelorDegree(cour)
                            combinedDegreeMap[cour] = degreeMap[cour]
                        elif cour[:2] == "CM":
                            degreeMap[cour] = onto.CombinedBachelorMastersDegree(cour)
                        else:
                            degreeMap[cour] = onto.MastersDegree(cour)
                        
                    cur.isAvailableInDegree.append(degreeMap[cour])
        
        with open("finalData/units.json", "r") as f:
            data = json.load(f)
            for key in data:
                unit = data[key]
                unitMap[key] = onto.Unit(key)
                cur = unitMap[key]
                
                cur.hasUnitCode = unit['code']
                cur.hasUnitTitle = unit['title']
                cur.hasUnitSchool = unit['school']
                cur.hasUnitLevel = int(unit['level'])
                
                if invalidXML(unit['description']):
                   unit['description'] = sanitise(unit["description"])
                # only descriptions are known to contain chars invalid for xml 1.0
                # they are sanitised in the generation of the kg, not the transformation of the data (to preserve integrity where possible)
                cur.hasUnitDescription = unit['description']
                cur.hasCreditPoints = int(unit['credit'])
                
                for period in unit['semesters']:
                    if period == "Not available in 2026":
                        break
                    if teachingPeriodMap.get(period) is None:
                        periodInst = onto.TeachingPeriod(period)
                        teachingPeriodMap[period] = periodInst
                    cur.hasTeachingPeriod.append(teachingPeriodMap[period])
                
                for loc in unit['locations']:
                    if locationMap.get(loc) is None:
                        locInst = onto.Location(loc)
                        locationMap[loc] = locInst
                    cur.hasUnitLocation.append(locationMap[loc])
                    
                for mode in unit['modes']:
                    if modeMap.get(mode) is None:
                        modeInst = onto.UnitMode(mode)
                        modeMap[mode] = modeInst
                    cur.hasUnitMode.append(modeMap[mode])
                
                if unit.get('majors') is not None:
                    for majTitle in unit['majors']:
                        #flag = True
                        if majorTitleToCodeMap.get(majTitle) is None:
                            newInst = onto.Major()
                            newInst.hasMajorTitle = majTitle
                            majorMap[newInst.name] = newInst
                            majorTitleToCodeMap[majTitle] = newInst.name
                        else:
                            cur.isInMajor.append(majorMap[majorTitleToCodeMap[majTitle]])
                        #Majors that only exist by title in units.json will still be instantiated
                        #Their final-level UID will use the default incremental ID (though this is not added as a major's code)
                    
                for out in unit['outcomes']:
                    if outcomeMap.get(out) is None:
                        outcome = onto.Outcome()
                        outcome.hasOutcomeDescription = out
                        outcomeMap[out] = outcome
                    cur.hasUnitOutcome.append(outcomeMap[out])
                
                for assess in unit['assessment']:
                    if assessmentMap.get(assess) is None:
                        assessment = onto.Assessment()
                        assessment.hasAssessmentDescription = assess
                        assessmentMap[assess] = assessment
                    cur.hasUnitAssessment.append(assessmentMap[assess])
                
                if unit.get("prerequisites_text") is not None:
                    cur.hasPrerequisiteText = unit['prerequisites_text']
                    
                if unit.get("prerequisite_courses") is not None:
                    for cour in unit['prerequisite_courses']:        
                        if degreeMap.get(cour) is None:
                            if cour[:2] == "BP":
                                degreeMap[cour] = onto.BachelorDegree(cour)
                            elif cour[:2] == "BH":
                                degreeMap[cour] = onto.HonoursDegree(cour)
                            elif cour[:2] == "CB":
                                degreeMap[cour] = onto.CombinedBachelorDegree(cour)
                                combinedDegreeMap[cour] = degreeMap[cour]
                            elif cour[:2] == "CM":
                                degreeMap[cour] = onto.CombinedBachelorMastersDegree(cour)
                            else:
                                degreeMap[cour] = onto.MastersDegree(cour)
                        cur.hasPrerequisiteDegree.append(degreeMap[cour])
                # Prerequisite Units added after all units added
                
                if unit.get("contact") is not None: 
                    for cont in unit['contact']:
                        if contactTypeMap.get(cont) is None:
                            contactTypeMap[cont] = onto.ContactType()
                            contactTypeMap[cont].hasContactTypeDescription = cont
                        # unique contact type, then unique contact type - hours pair
                        if contactMap.get(f"{cont} {unit['contact'][cont]}") is None:
                            contact = onto.ContactRequirement()
                            contact.hasContactType = contactTypeMap[cont]
                            contact.hasContactHours = unit['contact'][cont]
                            contactMap[f"{cont} {unit['contact'][cont]}"] = contact
                        cur.hasContactRequirement.append(contactMap[f"{cont} {unit['contact'][cont]}"])
        
        
        #final degree processing 
        with open("finalData/degrees.json", "r") as f:
            data = json.load(f)
            for key in data:
                deg = data[key]
                degInst = degreeMap[key]
                if deg.get("majors") is not None:
                    for maj in deg["majors"]:
                        degInst.hasMajor.append(majorMap[maj])
        
        for cb in combinedDegreeMap:
            cbDeg = combinedDegreeMap[cb]
            if cbDeg.hasDegreeTitle:
                degs = cbDeg.hasDegreeTitle.split(" and ")
                if len(degs) == 2:
                    deg1 = degs[0]
                    deg2 = degs[1]
                    cbDeg.comprisesDegree.append(degreeMap[degreeTitleToCodeMap[deg1]])
                    cbDeg.comprisesDegree.append(degreeMap[degreeTitleToCodeMap[deg2]])
                else:
                    degs = cbDeg.hasDegreeTitle.split("/ ")
                    if len(degs) == 2:
                        deg1 = degs[0]
                        deg2 = degs[1]
                        cbDeg.comprisesDegree.append(degreeMap[degreeTitleToCodeMap[deg1]])
                        cbDeg.comprisesDegree.append(degreeMap[degreeTitleToCodeMap[deg2]])
            # combined degrees without titles are skipped as they are the ones found with only their code
            # (can still reason on and query with their partial instances)
            
        #final unit processing
        with open("finalData/units.json", "r") as f:
            data = json.load(f)
            for key in data:
                unit = data[key]
                cur = unitMap[key]
                if unit.get("prerequisite_units") is not None:
                    prereqs = unit["prerequisite_units"]
                    for division in prereqs:
                        for pre in division:
                            if unitMap.get(pre) is None:
                                unitMap[pre] = onto.Unit(pre)
                            cur.hasPrerequisiteUnit.append(unitMap[pre])
                    #the structure of disjoint lists in prerequisite_units is ignored
                    #all units are assumed to equally be prerequisites
                
                if unit.get("advisable_prior_study") is not None:
                    for adv in unit['advisable_prior_study']:
                        if not(len(adv) != 8 or adv[len(adv)-4:len(adv)].isdigit()):
                            if unitMap.get(adv) is None:
                                unitMap[adv] = onto.Unit(adv)
                            cur.hasAdvisablePriorStudy.append(unitMap[adv])
                        #only units are assumed to be in the range of advisable prior study
                        #the nature of the data has incorrectly set it as majors for some
        
        #final major processing
        with open("finalData/majors.json", "r") as f:
            data = json.load(f)
            for key in data:
                maj = data[key]
                cur = majorMap[key]
                if len(maj["bridging"]) != 0:
                    for bri in maj["bridging"]:
                        cur.hasBridgingUnit.append(unitMap[bri])  
                            
                for unit in maj["units"]:
                    cur.hasCoreUnit.append(unitMap[unit])
                # an elective, in the context of a major, is assumed to be any unit outside of that major
                # 'units' is thus assumed to be core units (optional units are not modelled)
    onto.save("onto.owl", format="rdfxml")
    with onto:
        sync_reasoner_pellet(infer_property_values=True)
        
    onto.save("onto.owl", format="rdfxml")
    
parseData()



def runQueries():
    onto = get_ontology("./onto.owl").load()
    with onto:
        sync_reasoner_pellet(infer_property_values=True)
            
    graph = default_world.as_rdflib_graph()
    
    graph.bind("owl", OWL)
    graph.bind("rdfs", RDFS)
    graph.bind("onto", Namespace("https://www.handbooks.uwa.edu.au/onto.owl#"))
    
    q1 = """   
        
        SELECT DISTINCT ?deg ?unit
        WHERE {
            ?deg onto:hasMajor ?anyMaj .
            ?anyMaj onto:hasUnit ?unit .
          
            FILTER NOT EXISTS {
                ?deg onto:hasMajor ?maj .
                FILTER NOT EXISTS {
                    ?maj onto:hasUnit ?unit. 
                } 
            }
        }
    """
    
    q2 = """
        SELECT ?degType (AVG(?options) AS ?avgMajors)
        WHERE {
            ?degType rdfs:subClassOf onto:UndergraduateDegree .
            {
                SELECT ?degType ?deg (COUNT(?maj) as ?options)
                WHERE {
                    ?deg a ?degType .
                    ?deg onto:hasMajor ?maj .
                    
                }
                GROUP BY ?degType ?deg
            }
        }
        GROUP BY ?degType
    """
    
    q3 = """ 
        SELECT ?maj
        WHERE {
            ?maj a onto:Major .
            FILTER NOT EXISTS {
                ?maj onto:hasUnit ?unit .
                FILTER NOT EXISTS {
                    ?unit onto:hasUnitLocation onto:Albany .
                }
            }
        }
    """
    string = "data"
    
    q4 = f"""
        SELECT ?maj
        WHERE {{
            ?maj a onto:Major .
            ?maj onto:hasMajorOutcome ?out .
            ?out onto:hasOutcomeDescription ?desc .
            FILTER(
                CONTAINS(?desc, "{string}")
            )
        }}  
    """
    
    q1Res = list(graph.query(q1))
    q2Res = list(graph.query(q2))
    q3Res = list(graph.query(q3))
    q4Res = list(graph.query(q4))
    print(q1Res)
    
runQueries()
