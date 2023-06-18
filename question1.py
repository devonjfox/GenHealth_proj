#1.  How many patients in the dataset were diagnosed with Covid-19?

import conditions
from utils import load_csv


def patients():
    patient_list = load_csv("data/patients.csv")
    return patient_list


def patient_ids():
    patient_ids_set = set()
    for row in patients():
        patient_ids_set.add(row[0])
    return patient_ids_set


covid_patients = conditions.filter_conditions(condition="COVID-19")

print("Total number of patients with diagnosed COVID-19: ", len(covid_patients))
