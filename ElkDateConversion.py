# Justin Ray & Jesse Suders
# 2014-08-26
# Elk Julianday Conversion to Month/Day/Year

import arcpy

txt = r'C:\Elk\6-9-14.txt'
newtxt = r'C:\Elk\6-9-14_TESTY.txt'
elk_dictionary = {}
january = '01'
february = '02'
march = '03'
april = '04'
may = '05'
june = '06'
july = '07'
august = '08'
september = '09'
october = '10'
november = '11'
december = '12'

longmonth = [january,march,may,july,august,october,december]
regularmonth = [april,june,september,november]

lgmonth = '31'
regmonth = '30'
leapfeb = '29'
regfeb = '28'

textfile = open(txt,"r")

firstline = textfile.readline()

fieldlist = firstline.split(",")

year = fieldlist.index('Year')
julianday = fieldlist.index('Julianday')
serialno = fieldlist.index('CollarSerialNumber')
hour = fieldlist.index('Hour')

for line in textfile.readlines():
    split_line = line.split(",")
    yr = split_line[year]
    jday = split_line[julianday]
    hr = split_line[hour]
    elk = split_line[serialno]
    
    # If the elk SN isn't in the dictionary:
    if not elk in elk_dictionary:

    # Create a new Array object & add the point to it, put the array into the dictionary using the SN
        coord_array = arcpy.Array()
        elk_dictionary[elk] = coord_array

    else:
    # Retrieve the existing Array and add the new point for that elk
        coord_array = elk_dictionary[elk]

print coord_array
