from conditions import covid_patient_ids_set, conditions_file
from encounters import encounters_file, inpatient_patients_ids





def icu_covid_patients():
    icu_covid_patients_id = []
    encounters = encounters_file()
    _inpatient_covid_ids = inpatient_covid_ids()
    for encounter in encounters:
        if encounter[3] in _inpatient_covid_ids and encounter[8] == "305351004":
            icu_covid_patients_id.append(encounter[3])
    return icu_covid_patients_id


def inpatient_covid_ids():
    inpatient_covid_ids_list = []
    _covid_patient_ids_set = covid_patient_ids_set()
    _inpatient_patients_ids = inpatient_patients_ids()
    for covid_patient_id in _covid_patient_ids_set:
        if covid_patient_id in _inpatient_patients_ids:
            inpatient_covid_ids_list.append(covid_patient_id)
    return inpatient_covid_ids_list
