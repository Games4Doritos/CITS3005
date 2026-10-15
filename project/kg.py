from owlready2 import *
from rdflib import OWL, RDFS, Namespace
import owlready2
import json

owlready2.JAVA_EXE = r"C:\Program Files\Java\jre1.8.0_503\bin\java.exe"

def parseData():
    onto = get_ontology("./onto.owl").load()
    
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
                    cur.hasDegreeLocations.append(locationMap[loc])
        
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
                cur.hasMajorDescription = maj['description']
                
                for out in maj['outcomes']:
                    outcome = onto.Outcome()
                    outcome.hasOutcomeDescription = out
                    if outcomeMap.get(out) is None:
                        outcomeMap[out] = outcome
                    cur.hasMajorOutcomes.append(outcome)
                
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
                cur.hasUnitDescription = unit['description']
                cur.hasCreditPoints = int(unit['credit'])
                
                for period in unit['semesters']:
                    if period == "Not available in 2026":
                        break
                    if teachingPeriodMap.get(period) is None:
                        periodInst = onto.TeachingPeriod(period)
                        teachingPeriodMap[period] = periodInst
                    cur.hasTeachingPeriods.append(teachingPeriodMap[period])
                
                for loc in unit['locations']:
                    if locationMap.get(loc) is None:
                        locInst = onto.Location(loc)
                        locationMap[loc] = locInst
                    cur.hasUnitLocations.append(locationMap[loc])
                    
                for mode in unit['modes']:
                    if modeMap.get(mode) is None:
                        modeInst = onto.UnitMode(mode)
                        modeMap[mode] = modeInst
                    cur.hasUnitModes.append(modeMap[mode])
                
                if unit.get('majors') is not None:
                    for majTitle in unit['majors']:
                        #flag = True
                        if majorTitleToCodeMap.get(majTitle) is None:
                            newInst = onto.Major()
                            newInst.hasMajorTitle = majTitle
                            majorMap[newInst.name] = newInst
                            majorTitleToCodeMap[majTitle] = newInst.name
                        else:
                            cur.isInMajors.append(majorMap[majorTitleToCodeMap[majTitle]])
                        #Majors that only exist by title in units.json will still be instantiated
                        #Their final-level UID will use the default incremental ID (though this is not added as a major's code)
                    
                for out in unit['outcomes']:
                    outcome = onto.Outcome()
                    outcome.hasOutcomeDescription = out
                    
                    if outcomeMap.get(out) is None:
                        outcomeMap[out] = outcome
                    cur.hasUnitOutcomes.append(outcome)
                
                for assess in unit['assessment']:
                    assessment = onto.Assessment(assess)
                    
                    if assessmentMap.get(assess) is None:
                        assessmentMap[assess] = assessment
                    cur.hasUnitAssessments.append(assessment)
                
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
                        cur.hasPrerequisiteDegrees.append(degreeMap[cour])
                # Prerequisite Units added after all units added
                
                if unit.get("contact") is not None: 
                    for cont in unit['contact']:
                        contact = onto.ContactRequirement()
                        if contactTypeMap.get(cont) is None:
                            contactTypeMap[cont] = onto.ContactType(cont)
                        contact.hasContactType = contactTypeMap[cont]
                        contact.hasContactHours = unit['contact'][cont]
                        cur.hasContactRequirement.append(contact)
        
        
        #final degree processing 
        with open("finalData/degrees.json", "r") as f:
            data = json.load(f)
            for key in data:
                deg = data[key]
                degInst = degreeMap[key]
                if deg.get("majors") is not None:
                    for maj in deg["majors"]:
                        degInst.hasMajors.append(majorMap[maj])
        
        for cb in combinedDegreeMap:
            cbDeg = combinedDegreeMap[cb]
            if cbDeg.hasDegreeTitle:
                degs = cbDeg.hasDegreeTitle.split(" and ")
                if len(degs) == 2:
                    deg1 = degs[0]
                    deg2 = degs[1]
                    cbDeg.comprisesDegrees.append(degreeMap[degreeTitleToCodeMap[deg1]])
                    cbDeg.comprisesDegrees.append(degreeMap[degreeTitleToCodeMap[deg2]])
                else:
                    degs = cbDeg.hasDegreeTitle.split("/ ")
                    if len(degs) == 2:
                        deg1 = degs[0]
                        deg2 = degs[1]
                        cbDeg.comprisesDegrees.append(degreeMap[degreeTitleToCodeMap[deg1]])
                        cbDeg.comprisesDegrees.append(degreeMap[degreeTitleToCodeMap[deg2]])
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
                            cur.hasPrerequisiteUnits.append(unitMap[pre])
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
                        cur.hasBridgingUnits.append(unitMap[bri])  
                            
                for unit in maj["units"]:
                    cur.hasCoreUnits.append(unitMap[unit])
                # an elective, in the context of a major, is assumed to be any unit outside of that major
                # 'units' is thus assumed to be core units (optional units are not modelled)
        
    with onto:
        sync_reasoner(infer_property_values=True)
        
    onto.save("onto.owl", format="rdfxml")
    
parseData()



def runQueries():
    onto = get_ontology("./onto.owl").load()
    with onto:
        sync_reasoner(infer_property_values=True)
            
    graph = default_world.as_rdflib_graph()
    
    graph.bind("owl", OWL)
    graph.bind("rdfs", RDFS)
    graph.bind("onto", Namespace("https://www.handbooks.uwa.edu.au/onto.owl#"))
    
    q1 = """   
        
        SELECT DISTINCT ?deg ?unit
        WHERE {
            ?deg onto:hasMajors ?anyMaj .
            ?anyMaj onto:hasUnits ?unit .
          
            FILTER NOT EXISTS {
                ?deg onto:hasMajors ?maj .
                FILTER NOT EXISTS {
                    ?maj onto:hasUnits ?unit. 
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
                    ?deg onto:hasMajors ?maj .
                    
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
                ?maj onto:hasUnits ?unit .
                FILTER NOT EXISTS {
                    ?unit onto:hasUnitLocations onto:Albany .
                }
            }
        }
    """
    string = "data"
    
    q4 = f"""
        SELECT ?maj
        WHERE {{
            ?maj a onto:Major .
            ?maj onto:hasMajorOutcomes ?out .
            ?out onto:hasOutcomeDescription ?desc .
            FILTER(
                CONTAINS(?desc, "{string}")
            )
        }}  
    """
    
    
    q1Res = list(graph.query(q4))
    
    print(q1Res)
    
runQueries()
