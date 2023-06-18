#3. What are the health outcomes experienced by Covid 19 patients?
from pprint import pprint

from conditions import filter_conditions, conditions_file

covid_patients = filter_conditions(condition="COVID-19")
covid_patients_patient_id = []
for covid_patient in covid_patients:
    covid_patients_patient_id.append(covid_patient[2])

covid_patient_comorbidities_dict = {}
conditions_list = conditions_file()
for condition in conditions_list:
    if condition[2] not in covid_patients_patient_id:
        continue
    if condition[2] not in covid_patient_comorbidities_dict.keys():
        covid_patient_comorbidities_dict[condition[2]] = set()
    covid_patient_comorbidities_dict[condition[2]].add(condition[5])


assert len(covid_patient_comorbidities_dict.keys()) == len(filter_conditions(condition="COVID-19"))
comorbidities_set = set()
for value in covid_patient_comorbidities_dict.values():
    comorbidities_set = comorbidities_set.union(value)

#This question answers ALL events before and after COVID-19 event
#TODO filter by after COVID event
pprint(comorbidities_set)
