# CITS3005 Project - User Manual

## Ontology Overview

This ontology models the UWA handbook, including Degrees, Majors, Units, Locations, Assessments, Contact Requirements and more.

**Base IRI: https://www.handbooks.uwa.edu.au/onto.owl#**

### Schema

**Class Inheritance Trees**
```
            |   - Degree -  |                                      
UndergraduateDegree     PostgraduateDegree
| - BachelorDegree          | - MastersDegree
| - HonoursDegree           | - CombinedBachelorMastersDegree
| - CombinedBachelorDegree
| - CombinedBachelorMastersDegree

UnitSet                 
| - Major
| - Minor

Outcome
Location
TeachingPeriod
UnitMode
Assessment
ContactRequirement
ContactType
```

**Properties by Class**  
Degree  
```
hasMajor
hasDegreeCode
hasDegreeTitle
hasDegreeSchool
hasTotalCreditPoints
hasStandardFullTimeDuration
hasDegreeLocaton
```
CombinedBachelorDegree
```
comprisesDegree
```
Major
```
hasMajorCode
hasMajorTitle
hasMajorSchool
hasMajorDescription
hasMajorOutcome
isAvailableInDegree
hasCoreUnit
hasBridgingUnit
```
Unit
```
hasUnitCode
hasUnitTitle
hasUnitLevel
hasUnitDescription
hasCreditPoints
hasTeachingPeriod
hasUnitLocation
hasUnitMode
isInMajor
hasUnitOutcome
hasUnitAssessment
hasPrerequisiteText
hasPrerequisiteDegree
hasPrerequsiteUnit
hassAdvisablePriorStudy
hasContactRequirement
```
Location
```
hasDegreeAvailable
hasUnitAvailable
```
Outcome
```
hasOutcomeDescription
```
Assessment
```
hasAssessmentDescription
```
ContactRequirement
```
hasContactType
hasContactHours
```
hasContactType
```
hasContactTypeDescription
```

### Rules/Constraints
**Ontology Constraints**
- A degree must have at least one major
- A CombinedBachelorDegree comprises of exactly two degrees (Bachelors or Honours) 

**SWRL Rules**
- An outcome of a major's core unit is an outcome of the major
- Any major in an UndergraduateDegree is a major in the Bachelor of Philosophy (Honours) (BH005)
- For a unit B which is a prerequisite of unit C, a prerequsite A of B is also a prerequisite of C
- For a degree comprising a CombinedBachelorDegree, any major it has will also be a major of the combined degree

## Setup

### Project Structure
```
| - transform.py
| - onto.py
| - kg.py
| - onto.owl
| - app.py
| - finalData/...
| - rawData/...
```

**Generate Data**  
```python transform.py```  
*Transforms the raw data and outputs to the ./finalData directory*
(Already exists)

**Initialise Ontology**  
```python onto.py```  

**Generate Knowledge Graph**  
```python kg.py```  
*Requires the ontology to be initialised first*  
*The query running function is called by default, it can be disabled within the file*

**Run Application**  
```python app.py```  
*This will first run the reasoner and then start the input line showing a ':'*

*Note: The Java Developer Kit used for the pellet reasoner was set to JDK 25.0.4.1 (latest release of JDK 25)*
```owlready2.JAVA_EXE = r"C:\Program Files\Java\jdk-25.0.4.1\bin\java.exe"```
*This may be changed as required**

## Syntax
### Data Retrieval
```
*get *class <className>
     *prop  <propName>
     *inst *<instName> <propName>
```
'*' -> required, other arguments are optional for different functionality


- get class/prop retrieves all instances of classes/properties
- get class/prop <...Name> retrieves all instances of the specific class/property
- get inst <...Name> retrieves the name of that instance
- get inst <...Name> <...propName> retrieves all things connected to the instance by that property
### Queries

### Data Addition/Modification

```
*add *<className> *<instName>

```




