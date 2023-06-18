# 4.c.1. What medications are COVID-19 patients using?
from pprint import pprint

import cross_reference
from utils import load_csv
import conditions

covid_patients = conditions.filter_conditions(condition="COVID-19")
covid_patient_ids_set = set()
for covid_patient in covid_patients:
    covid_patient_ids_set.add(covid_patient[2])


def medications(path="data/medications.csv"):
    medications_list = load_csv(path)
    return medications_list


covid_medications = dict()
_medications = medications()
for medication in _medications:
    if medication[2] in covid_patient_ids_set:
        covid_medications[medication[5]] = medication[6]

print("All medications COVID patients are taking:")
print(covid_medications)

# 4.c.2. What medications do COVID, ICU patients take?


covid_icu_medications = dict()
_icu_covid_patients = cross_reference.icu_covid_patients()
for medication in _medications:
    if medication[2] in _icu_covid_patients:
        covid_icu_medications[medication[5]] = medication[6]

print("All medications ICU COVID patients are taking:")
print(covid_icu_medications)
