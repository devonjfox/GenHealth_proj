from utils import load_csv

file = None


def death_cert_count():
    return len(death_certs_patient_ids())


def encounters_file(path="data/encounters.csv"):
    return load_csv(path)


def death_certs_patient_ids():
    death_cert_list = []
    encounters = encounters_file()
    for row in encounters:
        if row[8] == "308646001":
            death_cert_list.append(row[3])
    return death_cert_list


def inpatient_patients_ids():
    inpatient_patients_encounters = filter_encounters(encounter_class="inpatient")
    inpatient_patient_ids = set()
    for inpatient_patient in inpatient_patients_encounters:
        inpatient_patient_ids.add(inpatient_patient[3])
    return inpatient_patient_ids


def filter_encounters(encounter_class):
    encounters_list = encounters_file()
    filtered_encounters_list = []
    for encounter in encounters_list:
        if encounter[7] == encounter_class:
            filtered_encounters_list.append(encounter)

    return filtered_encounters_list
