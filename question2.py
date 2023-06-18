# How many patients were diagnosed with Covid-19 and admitted to the hospital
# (inpatient)?
from encounters import filter_encounters
from conditions import filter_conditions

covid_patients = filter_conditions(condition="COVID-19")
inpatient_patients = filter_encounters(encounter_class='inpatient')
covid_patients_patient_id = []
for covid_patient in covid_patients:
    covid_patients_patient_id.append(covid_patient[2])
inpatient_patients_patient_id = []
for inpatient in inpatient_patients:
    inpatient_patients_patient_id.append(inpatient[3])

covid_inpatient_patient_ids = list(set(covid_patients_patient_id).intersection(inpatient_patients_patient_id))
print("Total number of COVID-19 patients with an inpatient event: ", len(covid_inpatient_patient_ids))
print("Percent of COVID-19 patients with an inpatient event: ",
      (len(covid_inpatient_patient_ids) / len(filter_conditions(condition="COVID-19"))) * 100)
