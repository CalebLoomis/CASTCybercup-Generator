import csv


def loadCSV(file_name):
    items = list()
    with open(file_name) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            items.append(row)

    return items
