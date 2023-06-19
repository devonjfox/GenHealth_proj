#4.d.1: Survival analysis: What patients have COVID and died?
from conditions import *
from encounters import death_cert_count, death_certs_patient_ids
from cross_reference import icu_covid_patients

covid_patients = filter_conditions(condition="COVID-19")
_covid_patient_ids_set = set()
for covid_patient in covid_patients:
    _covid_patient_ids_set.add(covid_patient[2])

print("4.d.1: Unique Insight: Survival analysis: What patients have COVID and died?")
print("Number of deaths of COVID patients: ", death_cert_count())
print("Percent of deaths of COVID patients: ", ((death_cert_count() / len(covid_patients)) * 100))



#4.d.2: Survival analysis: What patients have COVID and went to the ICU and died?

_icu_covid_patients = icu_covid_patients() # list of icu covid patient ids
_death_certs_patient_ids = death_certs_patient_ids()

mortaility_list = set()
for death_cert_patient_id in _death_certs_patient_ids:
    if death_cert_patient_id in _icu_covid_patients:
        mortaility_list.add(death_cert_patient_id)

print("4.d.2: Unique Insight: Survival analysis: What patients have COVID and went to the ICU and died?")
print("Number of deaths in ICU COVID patients: ", len(mortaility_list))
print("Percent of deaths of ICU COVID patients: ", ((len(mortaility_list) / len(covid_patient_ids_set())) * 100))

