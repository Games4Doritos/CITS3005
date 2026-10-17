# CITS3005 Project - Report

## Design Choices

The data used was the units.json, majors.json and degrees.json files provided. They had many errors, many of which where fixed first in transform.py: 

*Unit Majors*  
Some titles of majors listed under "majors" in units in units.json were missing their last character. Empirical data retrieval was done to map each incorrect major title to its correct one, using the incorrectMajors and correctMajors lists.  
These majors were only known to exist by their titles, so they were instantiated via the default incremental UID 'classX' name instead of a unknown code. These instances didn't have any property instances, and so they exist for the property completeness of the units that relate to them.

*Unit and Major Outcomes*  
Outcomes for units and majors had a varying number of trailing full stops (0-2). All outcomes were normalised to have on trailing full stop.

*Assessments*  
Unit assessment names contained leading/trailing 'and' words. These were stripped.

*Unit Contact Requirements*  
Unit Contact Requirement names contained leading '/' or 'of' words, or leading/trailing 'and' words. These were stripped.

Many choices were made in the generation of the knowledge graph in kg.py as well:

*Instance Naming*  
Instances of Degree, Major and Unit were named by their codes.  
Instances of Location, UnitMode and TeachingPeriod were named by their name/description in the data.  
However, Outcome, Assessment, ContactRequirement and ContactType are isntantiated without a supplied name, bearing the default incremental UID 'classX' name. This was due the spaces, slashes and other characters being in the data represented by those classes, which violates the xml format the ontology is saved to. Those strings are instead pointed to as a property such as 'hasAssessmentDescription".

*XML Character Sanitisation*  
Strings in the data used for major and unit descriptions were sanitised to remove an characters not allowed in the rdfxml format.  

*Missing Attribute*  
Any missing a key:value in the json files that would represent a property was skipped, meaning the instance of that property was discarded.

*Degree Types*  
Only Bachelor, Honours and Combined Bachelor degrees were present in degrees.json, though there were majors in majors.json that related to Masters and Combined Bachelor Masters degrees (empirically deduced by code formats). These degrees only exist in the data by their code, and so they were instantaited, only with their code as their name and without relating to any other properties, as for the completeness of the majors as described before.

*Prerequisite Unit disjoint list structure*  
The 'prerequisite_units' attribute of units in units.json conformed to a list containing lists of units. Though this may have been an attempt to separate the prerequisite units into disjunct clauses, this will be ignored due to nondeterminism. All units listed under a 'prerequisite_units' are equally counted as prerequsiites.

*Unit Types*  
The only modelled types of units relative to a major are Core Units and Bridging Units, interpretted from 'units' and 'bridging' in units.json Elective Units were not explicitly modelled and so are defined as any unit that is not part of a major (relative to it).

*Advisable Prior Study*  
'advisable_prior_study' was assumed to only refer to units. Some of the data in units.json listed degrees under it, though from empirical research it was due to the function of the web scraper used. So any non-unit codes were ignored.

Other design choices:

*All level 1 units were assumed to have 6 credit points*  

*Data Property Inference was not achieved, and so functionality involving aggregation, such as for total credit points, is not present in this ontology*

## Tools Used

- No GUI tools were used, only CLI  
- Standard Python Libraries like json and re (regex) were used for simplicity  

I would recommend people to at least try Protege at the start to see if the visual aid would be beneficial.

I used assistants only to help debug code, understand owlready2 and swrl concepts and syntax, and to suggest approaches to small parts of the design. This will only with Gemini and Google AI Summaries

*Time Estimates*  
- Ontology - 5h  
- Knowledge Graph Generation 10h
- Data Processing 5h
- Rules and Constraints 2h
- Iterative Tweaking, Debugging 10h
- Application 2h
- User Manual and Report 2h
