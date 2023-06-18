from utils import load_csv


def covid_patient_ids_set():
    covid_patients = filter_conditions(condition="COVID-19")
    _covid_patient_ids_set = set()
    for covid_patient in covid_patients:
        _covid_patient_ids_set.add(covid_patient[2])
    return _covid_patient_ids_set


def filter_conditions(condition=None):
    conditions_list = []
    conditions_file_obj = conditions_file()
    for row in conditions_file_obj:
        if row[5] == condition:
            conditions_list.append(row)
    return conditions_list


def conditions_file(path="data/conditions.csv"):
    conditions_list = load_csv(path)
    return conditions_list
