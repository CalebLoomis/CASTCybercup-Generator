import csv


def loadCSV(file_name):
    items = list()
    with open(file_name) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            row = {x.replace(' ', ''): v
            for x, v in row.items()}

            row = {x.replace('"', ''): v
            for x, v in row.items()}


            for key in row:
                try:
                    row[key] = row[key].strip().strip('"')
                except AttributeError:
                    pass

            items.append(row)
    return items
