## Justin Ray
## 7/10/14
## Elk Telemetry Points To Lines

import arcpy
arcpy.env.overwriteOutput = True

# Create variables
workspace = arcpy.env.workspace = r'C:\Elk\ElkData.gdb'
txt_file = arcpy.GetParameterAsText(0)
id_field = 'CollarSN'
update_fields = (id_field, "SHAPE@")
spatial_ref = arcpy.SpatialReference(4269)
fc_name = arcpy.GetParameterAsText(1)

# Create the line feature class to be populated
try:
    feature_class = arcpy.CreateFeatureclass_management(workspace, fc_name, 'POLYLINE', '', '', '', spatial_ref)
    arcpy.AddField_management(feature_class, id_field, 'LONG')
except:
    arcpy.AddMessage('Feature class creation failed')

# Open the text file
observation_file = open(txt_file,"r")

# Read the header line
headers = observation_file.readline()

# Determine indices of the Collar Serial Number, Julian Day, Year, Lat, and Long
header_list = headers.split(",")
elk_index = header_list.index("CollarSerialNumber")
lat_index = header_list.index("Latitude")
long_index = header_list.index("Longitude")

# Create a dictionary to hold the elk information
elk_dictionary = {}

try:
    # Loop through the rest of the records in the file
    for line in observation_file.readlines():
        split_line = line.split(",")
        elk = split_line[elk_index]
        lat = split_line[lat_index]
        long = split_line[long_index]

        # Create a point object to store the coordinates
        coords = arcpy.Point(long,lat)

        # If the elk SN isn't in the dictionary:
        if not elk in elk_dictionary:

            # Create a new Array object & add the point to it, put the array into the dictionary using the SN
            coord_array = arcpy.Array()
            coord_array.add(coords)
            elk_dictionary[elk] = coord_array

        else:
            # Retrieve the existing Array and add the new point for that elk
            coord_array = elk_dictionary[elk]
            coord_array.add(coords)
except:
    arcpy.AddMessage('Dictionary setup and/or population failed')

try:
    # Loop through the elk in the dictionary to...
    for key in elk_dictionary:
        # Create an insert cursor
        with arcpy.da.InsertCursor(feature_class,update_fields) as cursor:
            # Create a polyline
            polyline = arcpy.Polyline(elk_dictionary[key],spatial_ref)
            row = (str(key),polyline)
            # Insert a new row into the feature class for each elk
            cursor.insertRow(row)
except:
    arcpy.AddMessage('Inserting the records into a polyline failed')

arcpy.AddMessage(arcpy.GetMessages(2))
arcpy.AddMessage(arcpy.GetMessages(3))