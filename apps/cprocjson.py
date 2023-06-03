from datetime import date, timedelta
import json

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

# host
#start_date = date(2022, 6, 26)
start_date = date(2022, 8, 4)
end_date = date(2023, 6, 2)

domain = dict()
f = open('apps.json')
domain = json.load(f)
for i in domain:
    domain[i]["counts"] = len(domain[i]["rank"])

dcounts = dict()
for i in domain:
    dcounts[i] = domain[i]["counts"]

dcounts = {k: v for k, v in sorted(dcounts.items(), key=lambda item: item[1], reverse=True)}
for i in dcounts:
    t = i.replace(",",";")
    #print(t+",",dcounts[i])
    print(str(dcounts[i])+","+t)






'''
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
'''