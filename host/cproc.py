from datetime import date, timedelta
import requests
import csv
import json

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2022, 6, 26)
end_date = date(2023, 6, 2)

domain = dict()

for single_date in daterange(start_date, end_date):
    dd = single_date.strftime("%Y-%m-%d") + ".csv"
    with open(dd) as csv_file:
        print(dd)
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 1
        for row in csv_reader:
            if row[0] not in domain:
                domain[row[0]] = dict()
                domain[row[0]]["c1"] = row[1]
                domain[row[0]]["c2"] = row[2]
                domain[row[0]]["rank"] = list()
                domain[row[0]]["rank"].append(count)
            else:
                domain[row[0]]["c1"] = domain[row[0]]["c1"] + row[1]
                domain[row[0]]["c2"] = domain[row[0]]["c2"] + row[2]
                domain[row[0]]["rank"].append(count)
            count = count + 1


print(json.dumps(domain))