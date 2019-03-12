import csv
import wget
from datetime import datetime

# Time setting
now = datetime.utcnow()
utc_year = str(now).split()[0][0:4]
utc_month = str(now).split()[0][5:7]
utc_day = str(now).split()[0][8:10]
utc_hour = int(str(now).split()[1][0:2])
utc_minute = str(now).split()[1][3:5]

# Get most current csv file for KMSN from Iowa State
# https://mesonet.agron.iastate.edu/mos/csv.php?station=KMSN
station = "KMSN"
runtime = "2019-03-1212:00:00"
model = "GFS"
url = "https://mesonet.agron.iastate.edu/mos/csv.php?station=" + station + "&runtime=" + runtime + "&model=" + model
wget.download(url, '/Users/dschumacher4/Documents/GitHub/GLWS-Obs/' + station + ".csv")
# Calculate most recent cycle
if utc_hour < 20:
    cycle = 6
gfs = []
file_name = "KMSN.csv"
with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0
    for row in csv_reader:
        if line_count >= 1:
            gfs.append(row[5])
        line_count += 1
    
print(gfs)