from datetime import date, timedelta
import requests

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

# host
#start_date = date(2022, 6, 26)
start_date = date(2022, 8, 4)
end_date = date(2023, 6, 2)


for single_date in daterange(start_date, end_date):
    dd = single_date.strftime("%Y-%m-%d") + ".csv"
    uri = "https://planet.openstreetmap.org/tile_logs/apps-"+dd
    print(dd)
    try:
        r = requests.get(uri, allow_redirects=True)
        open(dd, 'wb').write(r.content)
    except Exception as e:
        print(e)
        pass


