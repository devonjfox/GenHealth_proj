#4.b How many COVID patients had a ICU event
from conditions import filter_conditions
from encounters import filter_encounters, encounters_file

covid_patients = filter_conditions(condition="COVID-19")
covid_patient_ids_set = set()
for covid_patient in covid_patients:
    covid_patient_ids_set.add(covid_patient[2])

inpatient_patients = filter_encounters(encounter_class="inpatient")
inpatient_patient_ids = set()
for inpatient_patient in inpatient_patients:
    inpatient_patient_ids.add(inpatient_patient[3])

inpatient_covid_ids = []
for covid_patient_id in covid_patient_ids_set:
    if covid_patient_id in inpatient_patient_ids:
        inpatient_covid_ids.append(covid_patient_id)

icu_covid_patients = []
encounters = encounters_file()
for encounter in encounters:
    if encounter[3] in inpatient_covid_ids and encounter[8] == "305351004":
        icu_covid_patients.append(encounter[3])




print("4.b Unique Insight: How many COVID patients had a ICU event")
print("Number of COVID-19 patients with ICU event: ", len(icu_covid_patients))
print("Percent of COVID-19 patients with ICU event: ", ((len(icu_covid_patients))/(len(covid_patient_ids_set)))*100)
