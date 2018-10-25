from MesoPy import Meso
import datetime
m = Meso(token='11b5b4f4d04041cead837493576cdecd')
now = datetime.datetime.now()

def main():
    menu_input = ""
    # Time format YYYYMMDDTTTT
    print("Great Lakes Weather Service Data Viewer, written by Douglas Schumacher")
    print("The current date and time is " + now.strftime("%Y-%m-%d %H:%M"))
    starttime = "201810241800" # 6 PM yesterday (10/24)
    endtime = currenttime() # Period ends at current time
    while menu_input != "q":
        menu_input = input("Enter 1 for Cranberry data, 2 for Wysocki data, and 3 for Buckley Data, or q to quit: ")
        print("********")
        if menu_input == 'q':
            quit()
        if menu_input == '1':
            cranberries(starttime, endtime)
        if menu_input == '2':
            wysocki(starttime, endtime)
        if menu_input == '3':
            buckley(starttime, endtime)

def cranberries(starttime, endtime):
    # Sparta, AR731 [Cataract]
    # Fort McCoy, KCMY
    # Tomah, NO CURRENT STATION
    # Camp Douglas, KVOK
    # Black River Falls, KBCK
    # Eau Claire, KEAU
    # Augusta, AFWW3
    # Neillsville, KMFI [Marshfield]
    # Mather, NCHW3 [Necedah Wildlife Refuge]
    region1_station_list = ["AR730", "KCMY", "TOMAH NO STATION", "KVOK", "KBCK", "KEAU", "AFWW3", "KMFI", "NCHW3" ]
    # Town of Cranmoor, Elm Lake Cranberry, NOT IN MESOWEST
    # Wisconsin Rapids, KISW
    # Rome, NKAW3
    # Mather, NCHW3 [Necedah Wildlife Refuge]
    # Necedah, NEHW3
    # Plover, PLOW3 [NOT WORKING], KSTE
    # Lake Du Bay, Du Bay Cranberry, NOT IN MESOWEST
    # Hancock, E9270
    # Wautoma, KY50
    region2_station_list = ["KISW", "NKAW3", "NCHW3", "NEHW3","KSTE", "E9270", "KY50"]
    # Siren, KRZN
    # Minong, MRZW3
    # Haugen, HAUW3
    # Barnes, BRNW3
    # Cable, CABW3 [LOTS OF ERRORS RIGHT NOW]
    # Clam Lake, CLRW3
    # Hayward, KHYR
    # Rice Lake, KRPD
    # Bruce, DW1191
    # Ladysmith, KRCX
    region3_station_List = ["KRZN", "MRZW3", "HAUW3", "BRNW3", "CABW3", "CLRW3", "KHYR", "KRPD", "DW1191", "KRCX"]
    # Hurley, KIWD
    # Glidden, GDNW3
    # Fifield, E4088
    # Phillips, KPBH
    # Manitowish Waters [Cranberry], NOT IN MESOWEST
    # Manitowish Waters [Airport], KD25
    # Minocqua, KARV
    # Eagle River, KEGV
    # Three Lakes, Sampson Cranberry, NOT IN MESOWEST
    # Lake Nokomis [Cranberry], NOT IN MESOWEST
    # Rhinelander, KRHI
    # Tomahawk, KTKV
    region4_station_list = ["KIWD", "GDNW3", "KPBH", "KD25", "KARV", "KEGV", "KRHI", "KTKV"]
    master_station_list = [region1_station_list, region2_station_list, region3_station_List, region4_station_list]
    i = 1
    for station_list in master_station_list:
        print("__________________")
        print("Low Temperatures for Region " + str(i) + " from " + str(starttime) + " to " + str(endtime))
        print("__________________")
        i += 1
        for station in station_list:
            low_temp_data(station, starttime, endtime)
    return
def wysocki(starttime, endtime):
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
    station_list = ["AT644", "KISW", "NEHW3", "UR380", "C0617", "KPCZ", "NKAW3", "E9270", "KY50"]
    for station in station_list:
        data(station, starttime, endtime)

def buckley(starttime, endtime):
    station_list = ["KUES", "KMKE", "KMSN"] # Waukesha, Milwaukee, Madison
    for station in station_list:
        data(station, starttime, endtime)

def data(station, starttime, endtime):
    precip = m.precip(stid = station, start = starttime, end = endtime, units='precip|in')
    climate = m.time_stats(stid= station, start = starttime, end = endtime, type = 'all')
    try:
        station_climate = climate['STATION'][0]
        station_precip = precip['STATION'][0]
    except:
        print("Sorry, data set incomplete for " + station)
        print("-------")
        return
    station_name = station_climate['NAME'] # Storing station name to print
    totalPrecip = station_precip['OBSERVATIONS']['total_precip_value_1']
    high_temp = temp_f(station_climate['STATISTICS']['air_temp_set_1']['maximum'])
    low_temp = temp_f(station_climate['STATISTICS']['air_temp_set_1']['minimum'])
    print("Data for " + station_name + ", from " + str(starttime) + " to " + str(endtime))
    print("High: " + str(high_temp) + " °F") # High of period
    print("Low: " + str(low_temp) + " °F") # Low of period
    print("Total precip: " + str(totalPrecip) + '"') # Total precip of period
    print("-------")

def low_temp_data(station, starttime, endtime):
    climate = m.time_stats(stid= station, start = starttime, end = endtime, type = 'all')
    try:
        station_climate = climate['STATION'][0]
    except:
        print("Sorry, data set incomplete for " + station)
        print("-------")
        return
    station_name = station_climate['NAME'] # Storing station name to print
    low_temp = temp_f(station_climate['STATISTICS']['air_temp_set_1']['minimum'])
    print("Data for " + station_name)
    print("Low: " + str(low_temp) + " °F") # Low of period
    print("-------")

def temp_f(temp_c):
    return "{0:.4}".format(str(((9.0 / 5.0) * temp_c) + 32.0)) # Formats to decimal place, converts to F

def currenttime():
    return now.strftime("%Y%m%d%H%M")

if __name__ == "__main__":
    main()
