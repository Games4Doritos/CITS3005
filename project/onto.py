from owlready2 import *

onto = get_ontology("https://www.handbooks.uwa.edu.au/onto.owl#")

with onto:
    
    #<================================= Atomic Classes =================================>
    class Degree(Thing):
        pass
    
    class Outcome(Thing):
        pass
    
    class UnitSet(Thing):
        pass
    
    class Unit(Thing):
        pass
    
    class Location(Thing):
        pass
    
    class TeachingPeriod(Thing):
        pass
    
    class UnitMode(Thing):
        pass
    
    class Assessment(Thing):
        pass
    
    class ContactRequirement(Thing):
        pass
    
    class ContactType(Thing):
        pass

    #<================================= 1-Layer Classes =================================>
    class UndergraduateDegree(Degree):
        pass
    
    class PostgraduateDegree(Degree):
        pass
    
    class Major(UnitSet):
        pass
            
    class Minor(UnitSet):
        pass
    
    #<================================= 2-Layer Classes =================================>
    class BachelorDegree(UndergraduateDegree):
        pass
        
    class HonoursDegree(UndergraduateDegree):
        pass
    
    class CombinedBachelorDegree(UndergraduateDegree):
        pass
    
    class MastersDegree(PostgraduateDegree):
        pass
    
    class CombinedBachelorMastersDegree(UndergraduateDegree, PostgraduateDegree):
        pass
    
    #<================================= Base Properties =================================>
    class hasUnits(ObjectProperty):
        domain = [UnitSet]
        range = [Unit]
    
    class hasCode(DataProperty, FunctionalProperty):
        domain = [Thing]
        range = [str]
        
    class hasTitle(DataProperty, FunctionalProperty):
        domain = [Thing]
        range = [str]
    
    class hasSchool(DataProperty, FunctionalProperty):
        domain = [Thing]
        range = [str]
    
    class hasDescription(DataProperty, FunctionalProperty):
        domain = [Thing]
        range = [str]
        
    class hasOutcomeDescription(hasDescription):
        domain = [Outcome]
        range = [str]
    
    class hasOutcomes(ObjectProperty):
        domain = [Thing]
        range = [Outcome]
    
    class hasLocations(ObjectProperty):
        domain = [Thing]
        range = [Location]
    
    class hasPrerequisites(ObjectProperty, TransitiveProperty):
        pass
        
    class hasContactType(ObjectProperty, FunctionalProperty):
        domain = [ContactRequirement]
        range = [ContactType]
        
    class hasContactHours(DataProperty, FunctionalProperty):
        domain = [ContactRequirement]
        range = [int]
    
    #<================================= Major Properties =================================>
    class hasMajorCode(hasCode):
        domain = [Major]
        range = [str]
        
    class hasMajorTitle(hasTitle):
        domain = [Major]
        range = [str]
        
    class hasMajorSchool(hasSchool):
        domain = [Major]
        range = [str]
        
    class hasMajorDescription(hasDescription):
        domain = [Major]
        range = [str]
        
    class hasMajorOutcomes(hasOutcomes):
        domain = [Major]
        range = [Outcome]
    
    class isAvailableInDegree(ObjectProperty):
        domain = [Major]
        range = [Degree]
        
    class hasCoreUnits(hasUnits):
        domain = [Major]
        range = [Unit]
   
    class hasBridgingUnits(hasUnits):
        domain = [Major]
        range = [Unit]
   
    #<================================= Degree Properties =================================>
    class hasMajors(ObjectProperty):
        domain = [Degree]
        range = [Major]
        inverse_property = isAvailableInDegree
        
    class hasDegreeCode(hasCode):
        domain = [Degree]
        range = [str]
        
    class hasDegreeTitle(hasTitle):
        domain = [Degree]
        range = [str]
        
    class hasDegreeSchool(hasSchool):
        domain = [Degree]
        range = [str]
    
    class hasTotalCreditPoints(DataProperty, FunctionalProperty):
        domain = [Degree]
        range = [int]
        
    class hasStandardFullTimeDuration(DataProperty, FunctionalProperty):
        domain = [Degree]
        range = [str]
    
    class hasDegreeLocations(hasLocations):
        domain = [Degree]
        range = [Location]
        
    class comprisesDegrees(ObjectProperty):
        domain = [CombinedBachelorDegree]
        range = [BachelorDegree | HonoursDegree]
        
    #<================================= Unit Properties =================================>
    class hasUnitCode(hasCode):
        domain = [Unit]
        range = [str]
    
    class hasUnitTitle(hasTitle):
        domain = [Unit]
        range = [str]
        
    class hasUnitSchool(hasSchool):
        domain = [Unit]
        range = [str]
    
    class hasUnitLevel(DataProperty, FunctionalProperty):
        domain = [Unit]
        range = [int]
    
    class hasUnitDescription(hasDescription):
        domain = [Unit]
        range = [str]
        
    class hasCreditPoints(DataProperty, FunctionalProperty):
        domain = [Unit]
        range = [int]
            
    class hasTeachingPeriods(ObjectProperty):
        domain = [Unit]
        range = [TeachingPeriod]
        
    class hasUnitLocations(hasLocations):
        domain = [Unit]
        range = [Location]

    class hasUnitModes(ObjectProperty):
        domain = [Unit]
        range = [UnitMode]
        
    class isInMajors(ObjectProperty):
        domain = [Unit]
        range = [Major]
        inverse_property = hasUnits
        
    class hasUnitOutcomes(hasOutcomes):
        domain = [Unit]
        range = [Outcome]
    
    class hasUnitAssessments(ObjectProperty):
        domain = [Unit]
        range = [Assessment]
        
    class hasPrerequisiteText(DataProperty, FunctionalProperty):
        domain = [Unit]
        range = [str]
    
    class hasPrerequisiteDegrees(hasPrerequisites):
        domain = [Unit]
        range = [Degree]
    
    class hasPrerequisiteUnits(hasPrerequisites, TransitiveProperty):
        domain = [Unit]
        range = [Unit]
        
    class hasAdvisablePriorStudy(ObjectProperty):
        domain = [Unit]
        range = [Unit]
    
    class hasContactRequirement(ObjectProperty):
        domain = [Unit]
        range = [ContactRequirement]
        
    #<================================= Location Properties =================================>
        
    class hasDegreesAvailable(ObjectProperty):
        domain = [Location]
        range = [Degree]
        inverse_property = hasDegreeLocations
    
    class hasUnitsAvailable(ObjectProperty):
        domain = [Location]
        range = [Unit]
        inverse_property = hasUnitLocations
        
    #<================================= Rules =================================>
    unitChainRule = Imp()
    unitChainRule.set_as_rule("Unit(?u), Major(?m), hasCoreUnits(?m, ?u), hasUnitOutcomes(?u, ?o) -> hasMajorOutcomes(?m, ?o)")
    
    #B Phil assumed to exist
    bPhil = HonoursDegree("BH005")
    bPhilRule = Imp()
    bPhilRule.set_as_rule("Major(?m), UndergraduateDegree(?d), hasMajors(?d, ?m) -> hasMajors(BH005, ?m)")
    
    majorSharedRule = Imp()
    majorSharedRule.set_as_rule("Major(?m), Degree(?d), hasMajors(?d, ?m), comprisesDegrees(?cb, ?d) -> hasMajors(?cb, ?m)")
    
    
    
    #<================================= Restrictions =================================>
    
    Degree.is_a.append(hasMajors.some(Major))
    CombinedBachelorDegree.is_a.append(comprisesDegrees.exactly(2))
    
    
    
onto.save("onto.owl", format="rdfxml")