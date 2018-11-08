from MesoPy import Meso
import datetime
m = Meso(token='11b5b4f4d04041cead837493576cdecd')
now = datetime.datetime.now()
twelve_hours_prior = datetime.datetime.now() - datetime.timedelta(days=0.5)
output_string = ""
output_list = []

def main():
    # Time format YYYYMMDDTTTT
    output_list.append("Great Lakes Weather Service Data Viewer, Web Edition, written by Douglas Schumacher")
    output_list.append("The current date and time is " + now.strftime("%Y-%m-%d %H:%M"))
    starttime = twelve_hours_prior.strftime("%Y%m%d%H%M") # Period starts 12 hours prior to current time
    endtime = currenttime() # Period ends at current time
    section_break = "*******************"
    title_break = "~~~~~~~~~~~~~~~~~~~"
    output_list.append(section_break)
    output_list.append("WI CRANBERRY GROWERS")
    output_list.append(title_break)
    cranberries(starttime, endtime)
    output_list.append(section_break)
    output_list.append("WYSOCKI FARMS")
    output_list.append(title_break)
    wysocki(starttime, endtime)
    output_list.append(section_break)
    output_list.append("BUCKLEY TREES")
    output_list.append(title_break)
    buckley(starttime, endtime)
    output_string = ""
    for item in output_list:
        output_string += (item + "\n")
    return output_string

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
        output_list.append("__________________")
        output_list.append("Low Temperatures for Region " + str(i) + " from " + str(starttime) + " to " + str(endtime))
        output_list.append("__________________")
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
        output_list.append("Sorry, data set incomplete for " + station)
        output_list.append("-------")
        return
    station_name = station_climate['NAME'] # Storing station name to output_list.append
    totalPrecip = station_precip['OBSERVATIONS']['total_precip_value_1']
    high_temp = temp_f(station_climate['STATISTICS']['air_temp_set_1']['maximum'])
    low_temp = temp_f(station_climate['STATISTICS']['air_temp_set_1']['minimum'])
    output_list.append("Data for " + station_name + ", from " + str(starttime) + " to " + str(endtime))
    output_list.append("High: " + str(high_temp) + " °F") # High of period
    output_list.append("Low: " + str(low_temp) + " °F") # Low of period
    output_list.append("Total precip: " + str(totalPrecip) + '"') # Total precip of period
    output_list.append("-------")

def low_temp_data(station, starttime, endtime):
    climate = m.time_stats(stid= station, start = starttime, end = endtime, type = 'all')
    try:
        station_climate = climate['STATION'][0]
    except:
        output_list.append("Sorry, data set incomplete for " + station)
        output_list.append("-------")
        return
    station_name = station_climate['NAME'] # Storing station name to output_list.append
    low_temp = temp_f(station_climate['STATISTICS']['air_temp_set_1']['minimum'])
    output_list.append("Data for " + station_name)
    output_list.append("Low: " + str(low_temp) + " °F") # Low of period
    output_list.append("-------")

def temp_f(temp_c):
    return "{0:.4}".format(str(((9.0 / 5.0) * temp_c) + 32.0)) # Formats to decimal place, converts to F

def currenttime():
    return now.strftime("%Y%m%d%H%M")

if __name__ == "__main__":
    main()
