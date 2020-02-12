import json
import csv
import datetime 

with open("..user/Home/Location.json") as f: # define absolute path with location of json file
    loc_data = json.load(f)

in_list = loc_data["locations"] # dictionary value specific to Google output

def lat_long(lst):
    lat = [d["latitudeE7"] for d in in_list]
    lat_dec = [(float(i) * .0000001) for i in lat] # adjust decimal place for proper coordinate format
    lng = [d["longitudeE7"] for d in in_list ] 
    long_dec = [(float(i) * .0000001) for i in lng] # adjust decimal place for proper coordinate format
    time = [d["timestampMs"]  for d in in_list] 
    new_time = []
    for i in time:
        i = datetime.datetime.fromtimestamp(int(i)/1000).strftime('%Y-%m-%d %H:%M:%S') 
        new_time.append(i)

    return  list(zip(lat_dec,long_dec,new_time))

zip_list = (lat_long(in_list))

outfile = ("user/Home/loc_data.csv")

with open(outfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerow(["Latitude", "Longitude", "Time"])
    writer.writerows(zip_list)
