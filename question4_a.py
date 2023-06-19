#4.a. How many patients had ONLY suspected COVID?

from conditions import filter_conditions

covid_patients = filter_conditions(condition="COVID-19")
covid_patient_ids_set = set()
for covid_patient in covid_patients:
    covid_patient_ids_set.add(covid_patient[2])

suspected_covid_patients = filter_conditions(condition="Suspected COVID-19")
suspected_covid_patient_id_set = set()
for suspected_covid_patient in suspected_covid_patients:
    suspected_covid_patient_id_set.add(suspected_covid_patient[2])

only_suspected_covid = []
for patient_id in suspected_covid_patient_id_set:
    if patient_id not in covid_patient_ids_set:
        only_suspected_covid.append(patient_id)

print("4. Unique Inquiry: How many patients had ONLY suspected COVID?")
print("Only suspected COVID-19: ", len(only_suspected_covid))
#TODO add statistics



