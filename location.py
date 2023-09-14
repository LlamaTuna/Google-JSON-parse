import json
import csv
import datetime

def load_location_data(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)["locations"]

def format_location_data(locations):
    formatted_data = []
    for loc in locations:
        lat = float(loc["latitudeE7"]) * .0000001
        lng = float(loc["longitudeE7"]) * .0000001
        time = datetime.datetime.fromtimestamp(int(loc["timestampMs"]) / 1000).strftime('%Y-%m-%d %H:%M:%S')
        formatted_data.append((lat, lng, time))
    return formatted_data

def write_to_csv(data, outfile):
    with open(outfile, "w", newline='') as output:
        writer = csv.writer(output)
        writer.writerow(["Latitude", "Longitude", "Time"])
        writer.writerows(data)

def main():
    json_filepath = "../user/Home/Location.json"
    csv_filepath = "user/Home/loc_data.csv"
    
    location_data = load_location_data(json_filepath)
    formatted_data = format_location_data(location_data)
    write_to_csv(formatted_data, csv_filepath)

if __name__ == '__main__':
    main()
