import csv

with open('data-398-2019-09-18.csv') as f:
    fields =f.readline().replace('"', '').split(';')[:-1]

    reader = csv.DictReader(f, fieldnames=fields, delimiter=';')

    count_stops = {}
    for row in reader:
        a = row['Street']
        if count_stops.get(row['Street']):
            count_stops[row['Street']] += 1
        else:
            count_stops[row['Street']] = 1

    sorted_dict = sorted(count_stops.items(), key = lambda x: x[1])
    street_most_stops = sorted_dict[-1]

