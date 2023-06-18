import csv


def load_csv(path):
    loaded_file = []
    with open(path, encoding="utf8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            loaded_file.append(row)
    return loaded_file
