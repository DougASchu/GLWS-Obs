from MesoPy import Meso
import datetime
m = Meso(token='11b5b4f4d04041cead837493576cdecd')
now = datetime.datetime.now()

def main():
    menu_input = ""
    # Time format YYYYMMDDTTTT
    starttime = "201809110000"
    endtime = "201810111200"
    print("Great Lakes Weather Service Data Viewer, written by Douglas Schumacher")
    print("The current date and time is " + now.strftime("%Y-%m-%d %H:%M"))
    starttime = "2018" + input("Enter the desired start time for your records: ") + "0000" # Midnight
    endtime = "2018" + input("Enter the desired start time for your records: ") + "0000" # Midnight
    while menu_input != "q":
        menu_input = input("Enter 1 for Cranberry data, 2 for Wysocki data, and 3 for Buckley Data, or q to quit: ")
        if menu_input == 'q':
            quit()
        if menu_input == '1':
            cranberries(starttime, endtime)
        if menu_input == '2':
            wysocki(starttime, endtime)
        if menu_input == '3':
            buckley(starttime, endtime)

def cranberries(starttime, endtime):
    print("Not done yet.")
def wysocki(starttime, endtime):
    print("Precipitation reports")
    # NOT WORKING YET
    precip = m.precip(stid='AT644, KISW, NEHW3, UR380, C0617, KPCZ, NKAW3, E9270, KY50', start = starttime, end = endtime, units='precip|in')
    # Babcock, AT644 [Nekoosa]
    # Wisconsin Rapids, KISW
    # Nekoosa, AT644
    # Necedah, NEHW3
    # Monroe Center, UR380 [Necedah]
    # Plover, C0617
    # Almond, KPCZ [Waupaca]
    # Rome, NKAW3
    # Hancock, E9270
    # Wautoma, KY50
    for name in precip['STATION']:
        print(name)
    KUES_precip = precip['STATION'][2]
    KMSN_precip = precip['STATION'][1]
    KMKE_precip = precip['STATION'][0]
    # Waukesha, KUES
    station = KUES_precip['STID'] # remember we stored the dictionary in the precip variable
    totalPrecip =  KUES_precip['OBSERVATIONS']['total_precip_value_1']
    print('The total accumulated precip at ' + station + ' was ' + str(totalPrecip) + '"')
    # Lakeshore, KMKE
    station = KMKE_precip['STID'] # remember we stored the dictionary in the precip variable
    totalPrecip =  KMKE_precip['OBSERVATIONS']['total_precip_value_1']
    print('The total accumulated precip at ' + station + ' was ' + str(totalPrecip) + '"')
    # Madison, KMSN
    station = KMSN_precip['STID'] # remember we stored the dictionary in the precip variable
    totalPrecip =  KMSN_precip['OBSERVATIONS']['total_precip_value_1']
    print('The total accumulated precip at ' + station + ' was ' + str(totalPrecip) + '"')
def buckley(starttime, endtime):
    # Getting data
    precip = m.precip(stid='kues, kmsn, kmke', start = starttime, end = endtime, units='precip|in')
    climate = m.time_stats(stid='kues, kmsn, kmke', start = starttime, end = endtime, type = 'all')
    KUES_precip = precip['STATION'][2]
    KMSN_precip = precip['STATION'][1]
    KMKE_precip = precip['STATION'][0]
    KUES_climate = climate['STATION'][2]
    KMSN_climate = climate['STATION'][1]
    KMKE_climate = climate['STATION'][0]
    # Waukesha, KUES
    station = KUES_precip['STID'] # remember we stored the dictionary in the precip variable
    totalPrecip =  KUES_precip['OBSERVATIONS']['total_precip_value_1']
    print('The total accumulated precip at ' + station + ' was ' + str(totalPrecip) + '"')
    print(KUES_climate['STATISTICS']['air_temp_set_1']['maximum'])
    print(KUES_climate['STATISTICS']['air_temp_set_1']['minimum'])
    # Lakeshore, KMKE
    station = KMKE_precip['STID'] # remember we stored the dictionary in the precip variable
    totalPrecip =  KMKE_precip['OBSERVATIONS']['total_precip_value_1']
    print('The total accumulated precip at ' + station + ' was ' + str(totalPrecip) + '"')
    # Madison, KMSN
    station = KMSN_precip['STID'] # remember we stored the dictionary in the precip variable
    totalPrecip =  KMSN_precip['OBSERVATIONS']['total_precip_value_1']
    print('The total accumulated precip at ' + station + ' was ' + str(totalPrecip) + '"')

if __name__ == "__main__":
    main()
