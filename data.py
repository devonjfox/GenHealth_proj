def encounters(path="encounters.csv", encounter_class="inpatient"):
    with open(path) as file:
        header = file.readline()
        reader = csv.reader(file)
        # name the df
        inpatients_patients = set()
        # add to df by condition
        for i, row in enumerate(reader):
            if row[7] == encounter_class:
                inpatients_patients.add(row[3])
        covid_inpatients = []
        covid_patients = conditions(condition="COVID-19")
        for inpatient_patient in inpatients_patients:
            if inpatient_patient in covid_patients:
                covid_inpatients.append(inpatient_patient)
        return covid_inpatients
def patient_conditions(patient_id=None, path="conditions.csv"):
    # open the file containing the information for dx
    with open(path) as file:
        header = file.readline()
        # create the df will only pts w/ COVID
        reader = csv.reader(file)
        conditions_set = set()
        for i, row in enumerate(reader):
            if row[2] == patient_id:
                conditions_set.add(row[5])
        return conditions_set
def conditions(condition=None, path="conditions.csv"):
    # open the file containing the information for dx
    with open(path) as file:
        header = file.readline()
        # create the df will only pts w/ COVID
        reader = csv.reader(file)
        indexes = []
        patients = set()
        for i, row in enumerate(reader):
            if row[5] == condition:
                indexes.append(i)
                patients.add(row[2])
        return patients
