import csv
import wget
import datetime

# Current time setting
now = datetime.datetime.utcnow()
utc_year = int(str(now).split()[0][0:4])
utc_month = int(str(now).split()[0][5:7])
utc_day = int(str(now).split()[0][8:10])
utc_hour = int(str(now).split()[1][0:2])
utc_minute = int(str(now).split()[1][3:5])

# Yesterday time setting
yesterday = datetime.datetime.utcnow() - datetime.timedelta(days=1)
utc_yesterday_year = int(str(now).split()[0][0:4])
utc_yesterday_month = int(str(now).split()[0][5:7])
utc_yesterday_day = int(str(now).split()[0][8:10])
utc_yesterday_hour = int(str(now).split()[1][0:2])
utc_yesterday_minute = int(str(now).split()[1][3:5])

# Selection of runtime
if (utc_hour <= 5):
    run_hour = "18:00:00"
    run_day = str(utc_yesterday_year) + "-" + str(utc_yesterday_month) + "-" + str(utc_yesterday_day)
elif(utc_hour <= 11):
    run_hour = "00:00:00"
    run_day = str(utc_year) + "-" + str(utc_month) + "-" + str(utc_day)
elif (utc_hour <= 17):
    run_hour = "06:00:00"
    run_day = str(utc_year) + "-" + str(utc_month) + "-" + str(utc_day)
elif (utc_hour <= 23):
    run_hour = "12:00:00"
    run_day = str(utc_year) + "-" + str(utc_month) + "-" + str(utc_day)
runtime = run_day + run_hour

# Get most current csv file for KMSN from Iowa State
# https://mesonet.agron.iastate.edu/mos/csv.php?station=KMSN
station = "KMSN"
model = "GFS"
url = "https://mesonet.agron.iastate.edu/mos/csv.php?station=" + station + "&runtime=" + runtime + "&model=" + model
wget.download(url, '/Users/dschumacher4/Documents/GitHub/GLWS-Obs/' + station + "_" + model + "_" + runtime + ".csv")

gfs = []
file_name = station + "_" + model + "_" + runtime + ".csv"
with open(file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    line_count = 0
    for row in csv_reader:
        print(row)
        if line_count >= 1:
            gfs.append(row[5])
        line_count += 1
  
print(gfs)