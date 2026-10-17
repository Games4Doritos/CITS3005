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
    class hasUnit(ObjectProperty):
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
    
    class hasOutcome(ObjectProperty):
        domain = [Thing]
        range = [Outcome]
        
    class hasAssessmentDescription(hasDescription):
        domain = [Assessment]
        range = [str]
    
    class hasLocation(ObjectProperty):
        domain = [Thing]
        range = [Location]
    
    class hasPrerequisite(ObjectProperty):
        pass
        
    class hasContactType(ObjectProperty, FunctionalProperty):
        domain = [ContactRequirement]
        range = [ContactType]
        
    class hasContactTypeDescription(DataProperty, FunctionalProperty):
        domain = [ContactType]
        range = [str]
        
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
        
    class hasMajorOutcome(hasOutcome):
        domain = [Major]
        range = [Outcome]
    
    class isAvailableInDegree(ObjectProperty):
        domain = [Major]
        range = [Degree]
        
    class hasCoreUnit(hasUnit):
        domain = [Major]
        range = [Unit]
   
    class hasBridgingUnit(hasUnit):
        domain = [Major]
        range = [Unit]
   
    #<================================= Degree Properties =================================>
    class hasMajor(ObjectProperty):
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
    
    class hasDegreeLocation(hasLocation):
        domain = [Degree]
        range = [Location]
        
    class comprisesDegree(ObjectProperty):
        domain = [CombinedBachelorDegree]
        range = [BachelorDegree | HonoursDegree]
        
    #<================================= Unit Properties =================================>
    class hasUnitCode(hasCode):
        domain = [Unit]
        range = [str]
    
    class hasUnitTitle(hasTitle):
        domain = [Unit]
        range = [str]
        
    class hasUnitchool(hasSchool):
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
            
    class hasTeachingPeriod(ObjectProperty):
        domain = [Unit]
        range = [TeachingPeriod]
        
    class hasUnitLocation(hasLocation):
        domain = [Unit]
        range = [Location]

    class hasUnitMode(ObjectProperty):
        domain = [Unit]
        range = [UnitMode]
        
    class isInMajor(ObjectProperty):
        domain = [Unit]
        range = [Major]
        inverse_property = hasUnit
        
    class hasUnitOutcome(hasOutcome):
        domain = [Unit]
        range = [Outcome]
    
    class hasUnitAssessment(ObjectProperty):
        domain = [Unit]
        range = [Assessment]
        
    class hasPrerequisiteText(DataProperty, FunctionalProperty):
        domain = [Unit]
        range = [str]
    
    class hasPrerequisiteDegree(hasPrerequisite):
        domain = [Unit]
        range = [Degree]
    
    class hasPrerequisiteUnit(hasPrerequisite):
        domain = [Unit]
        range = [Unit]
        
    class hasAdvisablePriorStudy(ObjectProperty):
        domain = [Unit]
        range = [Unit]
    
    class hasContactRequirement(ObjectProperty):
        domain = [Unit]
        range = [ContactRequirement]
        
    #<================================= Location Properties =================================>
        
    class hasDegreeAvailable(ObjectProperty):
        domain = [Location]
        range = [Degree]
        inverse_property = hasDegreeLocation
    
    class hasUnitAvailable(ObjectProperty):
        domain = [Location]
        range = [Unit]
        inverse_property = hasUnitLocation
        
    #<================================= Rules =================================>
    transitivePrereqRule = Imp()
    transitivePrereqRule.set_as_rule("Unit(?a), Unit(?b), Unit(?c), hasPrerequisiteUnit(?a, ?b), hasPrerequisiteUnit(?b, ?c) -> hasPrerequisiteUnit(?a, ?c) ")
    
    unitChainRule = Imp()
    unitChainRule.set_as_rule("Unit(?u), Major(?m), hasCoreUnit(?m, ?u), hasUnitOutcome(?u, ?o) -> hasMajorOutcome(?m, ?o)")
    
    #B Phil assumed to exist
    bPhil = HonoursDegree("BH005")
    bPhilRule = Imp()
    bPhilRule.set_as_rule(f"Major(?m), UndergraduateDegree(?d), hasMajor(?d, ?m) -> hasMajor({bPhil.name}, ?m)")
    
    majorSharedRule = Imp()
    majorSharedRule.set_as_rule("Major(?m), Degree(?d), hasMajor(?d, ?m), comprisesDegree(?cb, ?d) -> hasMajor(?cb, ?m)")
    
    #<================================= Constraints =================================>
    
    Degree.is_a.append(hasMajor.some(Major))
    CombinedBachelorDegree.is_a.append(comprisesDegree.exactly(2))
    
    
    
onto.save("onto.owl", format="rdfxml")