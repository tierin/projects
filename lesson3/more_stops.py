import csv
import json
import math

import logging

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='stops.log'
                    )

with open('data-398-2019-09-18.csv') as stops, open('data-397-2019-08-27.json', 'r') as stations:

    fields = stops.readline().replace('"', '').split(';')[:-1]
    stops_reader = csv.DictReader(stops, fieldnames=fields, delimiter=';')
    all_stops_coords = {}
    for row in stops_reader:
        stop_coords = {'longitude': row['Longitude_WGS84'], 'latitude': row['Latitude_WGS84']}
        all_stops_coords[row['Name']] = stop_coords

    stations_data = json.load(stations)
    all_stations_coords = {}
    for station in stations_data:
        station_coords = {'longitude': station['Longitude_WGS84'], 'latitude': station['Latitude_WGS84']}
        all_stations_coords[station['NameOfStation']] = station_coords

stations_with_stops = {}
for station in all_stations_coords:
    num = 0
    for stop in all_stops_coords:
        try:
            station_coords = all_stations_coords[station]
            stop_coords = all_stops_coords[stop]
            stop_dist = []
            diff_latitude = math.radians(float(station_coords['latitude'])) - math.radians(float(stop_coords['latitude']))
            x = (math.sin(diff_latitude/2))**2
            diff_longitude = math.radians(float(station_coords['longitude'])) - math.radians(float(stop_coords['longitude']))
            y = math.cos(float(station_coords['latitude'])) * math.cos(float(stop_coords['latitude'])) * ((math.sin(diff_longitude/2))**2)
            radius = 6371
            distance = 2 * radius * math.asin(math.sqrt(x +y))
            stop_dist.append(distance)
            if distance <= 0.5:
                num += 1
        except ValueError:
            # Это потому что данные кривые или почему?
            logging.info(station)
    stations_with_stops[station] = num

max_stops = 0
max_stops_station = ''
for station in stations_with_stops:
    if stations_with_stops[station] > max_stops:
        max_stops = stations_with_stops[station]
        max_stops_station = station

print(max_stops_station)

print(stations_with_stops)
