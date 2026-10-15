import json

incorrectMajors = ['Anthropolog', 'Applied Human Geograph', 
                'Archaeolog', 'Asian Studie', 'CHNSA Chinese Studie', 'CHNSB Chinese Studie', 'CHNSI Chinese Studie', 
                'CHNSP Chinese Studie', 'Classics and Ancient Histor', 'Media and Communicatio', 'Criminology and Criminal Justic', 
                'Law and Societ', 'English and Literary Studie', 'Gender Studie', 'Fine Art', 'Art History and Curatorial Studie', 
                'FRNHA French Studie', 'FRNHB French Studie', 'FRNHI French Studie', 'Work and Employment Relation', 
                'Social and Environmental Sustainabilit', 'GRMNA German Studie', 'GRMNB German Studie', 'GRMNI German Studie', 
                'Histor', 'Human Right', 'History of Ar', 'INDNB Indonesian Studie', 'INDNI Indonesian Studie', 'INDNP Indonesian Studie', 
                'Indigenous Knowledge, History and Heritag', 
                'ITLNA Italian Studie', 'ITLNB Italian Studie', 'ITLNI Italian Studie', 'JPNSB Japanese Studie', 'JPNSI Japanese Studie', 
                'JPNSP Japanese Studie', 'Korean Studie', 'Linguistic', 'Music: Electronic Music and Sound Desig', 'Music General Studie', 
                'Music and Societ', 'Contemporary Popular Musi', 'Music Theatr', 'Human Sciences and Data Analytic', 'Philosoph', 
                'Philosophy, Politics and Economic', 'Artificial Intelligenc','Anatomy and Human Biolog', 'Human Science and Neuroscienc',  
                'Chemistr', 'Geochemistr', 'Data Scienc', 'Genetic', 'Microbiology and Immunolog', 
                'Physic', 'Frontier Physic', 'Wildlife Conservatio', 'Statistic', 'Mathematic', 'Accountin', 'Business La', 'Global Busines', 
                'Financial Economic', 'Economic', 'Financ', 'Human Resource Managemen', 'Managemen', 'Business Managemen', 
                'Enterprise and Innovatio', 'Marketin','Business Analytic', 'Quantum Computin', 'Automation and Robotics Engineerin', 
                'Biomedical Engineerin', 'Chemical Engineerin', 'Civil Engineerin', 'Environmental Engineerin', 
                'Electrical and Electronic Engineerin', 'Mechanical Engineerin', 'Mining Engineerin', 'Software Engineerin', 
                'Biodiversity and Evolutio', 'Spanish Studie'] 

correctMajors = ['Anthropology', 'Applied Human Geography', 
                'Archaeology', 'Asian Studies', 'CHNSA Chinese Studies', 'CHNSB Chinese Studies', 'CHNSI Chinese Studies', 
                'CHNSP Chinese Studies', 'Classics and Ancient History', 'Media and Communication', 'Criminology and Criminal Justice', 
                'Law and Society', 'English and Literary Studies', 'Gender Studies', 'Fine Arts', 'Art History and Curatorial Studies', 
                'FRNHA French Studies', 'FRNHB French Studies', 'FRNHI French Studies', 'Work and Employment Relations', 
                'Social and Environmental Sustainability', 'GRMNA German Studies', 'GRMNB German Studies', 'GRMNI German Studies', 
                'History', 'Human Rights', 'History of Art', 'INDNB Indonesian Studies', 'INDNI Indonesian Studies', 'INDNP Indonesian Studies', 
                'Indigenous Knowledge, History and Heritage', 
                'ITLNA Italian Studies', 'ITLNB Italian Studies', 'ITLNI Italian Studies', 'JPNSB Japanese Studies', 'JPNSI Japanese Studies', 
                'JPNSP Japanese Studies', 'Korean Studies', 'Linguistics', 'Music: Electronic Music and Sound Design', 'Music General Studies', 
                'Music and Society', 'Contemporary Popular Music', 'Music Theatre', 'Human Sciences and Data Analytics', 'Philosophy', 
                'Philosophy, Politics and Economics', 'Artificial Intelligence','Anatomy and Human Biology', 'Human Science and Neuroscience',  
                'Chemistry', 'Geochemistry', 'Data Science', 'Genetics', 'Microbiology and Immunology', 
                'Physics', 'Frontier Physics', 'Wildlife Conservation', 'Statistics', 'Mathematics', 'Accounting', 'Business Law', 'Global Business', 
                'Financial Economics', 'Economics', 'Finance', 'Human Resource Management', 'Management', 'Business Management', 
                'Enterprise and Innovation', 'Marketing','Business Analytics', 'Quantum Computing', 'Automation and Robotics Engineering', 
                'Biomedical Engineering', 'Chemical Engineering', 'Civil Engineering', 'Environmental Engineering', 
                'Electrical and Electronic Engineering', 'Mechanical Engineering', 'Mining Engineering', 'Software Engineering',
                'Biodiversity and Evolution', 'Spanish Studies'] 

missedMajors = [ 'Environmental Geography and Planning', 'Geographical and Spatial Science', 'Social and Environmental Sustainability', 
                'Wildlife Conservation', 'Environmental Science and Management', 'Marine Science', 'Agribusiness and Agricultural Science', 
                'Environmental Science and Ecology','International Relations', 'Media and Communication', 'Human Rights', 
                'Philosophy, Politics and Economics','Criminology and Criminal Justice', 'Psychology', 'Human Science and Neuroscience', 
                'Humanities in Health and Medicine', 'Art History and Curatorial Studies', 'Human Sciences and Data Analytics',
                'Business Management', 'Enterprise and Innovation', 'Global Business', 'Financial Economics', 'Economics', 
                'Music','Integrated Earth and Marine Sciences', 'Geochemistry', 'Biodiversity and Evolution', 'Plant Biology', 
                'Molecular Life Sciences', 'Human Genomics', 
                'Human Sciences (Anatomy and Physiology)', 'Pharmaceutical Health', 'Biochemistry of Nutrition', 
                'Pathology and Laboratory Medicine', 'Pharmacology and Toxicology','Frontier Physics', 
                'Integrated Medical Sciences and Clinical Practice', 'Integrated Dental Sciences', 'Sport Science, Exercise and Health',
                'Podiatric Health and Medical Sciences', 'Medical Science', 'Aboriginal Health and Wellbeing [not available in 2026]'
                ]

with open("rawData/degrees.json", "r") as f:
    data = f.read()
    with open("finalData/degrees.json", "w") as out:
        out.write(data)
    # no changes needed to degrees.json
    # extra degrees only listed in majors.json and units.json as prerequisites or courses are created on occurrence
    
with open("rawData/majors.json", "r") as f:
    data = json.load(f)
    for key in data:
        maj = data[key]
        n = len(maj["outcomes"])
        for i in range(n):
            out = maj["outcomes"][i]
            if out[-2:] == "..":
                maj["outcomes"][i] = out[:-1]
            elif out[-1] != ".":
                maj["outcomes"][i] = out + "."
            #assert that each outcomes ends with exactly one full stop
            #raw data ranged from 0 - 2 full stops at the end
                
    with open("finalData/majors.json", "w") as out:
        json.dump(data, out, indent=2)
        
count = 0
with open("rawData/units.json", "r") as f:
    data = json.load(f)
    
    for key in data:
        unit = data[key]
        if unit.get("majors") is not None:
            majs = unit["majors"]
            n = len(majs)
            for i in range(n):
                maj = majs[i]
                for j in range(len(incorrectMajors)):
                    if incorrectMajors[j] == maj:
                        majs[i] = correctMajors[j]
                        break
        #replace one of a unit's majors with its correct version if it has its last character missing
                    
        n = len(unit["outcomes"])
        for i in range(n-1, -1, -1):
            out = unit["outcomes"][i]
            if len(out) < 2:
                unit["outcomes"].pop(i)
            elif out[-2:] == "..":
                unit["outcomes"][i] = out[:-1]
            elif out[-1] != ".":
                unit["outcomes"][i] += "."
            #assert that each outcomes ends with exactly one full stop
            #raw data ranged from 0 - 2 full stops at the end
        
        n = len(unit["assessment"])
        for i in range(n-1, -1, -1):
            assess = unit["assessment"][i]
            if len(assess) < 2:
                unit["assessment"].pop(i)
            elif assess.removeprefix("and").removesuffix("and").strip() != assess:
                new = assess.removeprefix("and").removesuffix("and").strip()
                if len(new) == 0:
                    unit["assessment"].pop(i)
                else: 
                    unit["assessment"][i] = new
            #assert assessment is at least one reasonable word longer than 1 character
            #strip any 'and' trailing either end of an assessment
       
        if unit.get("contact") is not None:
            for cont in list(unit["contact"]):
                if cont.removeprefix("of").strip() != cont:
                    new = cont.removeprefix("of").strip()
                    hours = unit["contact"][cont]
                    unit["contact"].pop(cont)
                    unit["contact"][new] = hours
                elif cont.removeprefix("and").removesuffix("and").strip() != cont:
                    new = cont.removeprefix("and").removesuffix("and").strip()
                    hours = unit["contact"][cont]
                    unit["contact"].pop(cont)
                    unit["contact"][new] = hours
            #strip any 'and' trailing either end of a contact type
            #strip any 'of' at the start of a contact type
                    
    with open("finalData/units.json", "w") as out:
        json.dump(data, out, indent=2)