import json

with open('data-397-2019-08-27.json') as f:
    stations_info = json.load(f)

    station_repair_escalators = []

    for station in stations_info:
        if station.get('RepairOfEscalators'):
            station_repair_escalators.append(station.get('NameOfStation'))
    print(station_repair_escalators)
