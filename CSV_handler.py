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

def verify_csv(infile):
    try:
        with open(infile, newline='') as csvfile:
            start = csvfile.read(4096)

            # isprintable does not allow newlines, printable does not allow umlauts...
            if not all([c in string.printable or c.isprintable() for c in start]):
                return False
            has_header = csv.Sniffer().has_header(start)
            csv.Sniffer.sniff(start)
            return has_header
    except csv.Error:
        # Could not get a csv dialect -> probably not a csv.
        return False
