'''
-----------------------------------------------------------------------------------------------
Author: Justin Ray, VDGIF
Date: May 29, 2014 (start)
Purpose: To append the telemetry updates for all of the Virginia Elk Herd to the master dataset
-----------------------------------------------------------------------------------------------
'''

# Import necessary modules
import arcpy, sys

# Error handling
try:
    # Set workspace - MODIFY THIS FOR FINAL DELIVERABLE (or allow user input)
    workspace = arcpy.env.workspace = "K:\\projects\\Justin_Ray\\JeremyNicholson\\ElkData.gdb"
    arcpy.env.overwriteOutput = True

    # Create variables
    inputfile = sys.argv[1] # Must enclude entire path - enclose in quotes if spaces exist
    masterdataset = arcpy.GetParameterAsText(0) # Doesn't need entire path - only anything after the workspace
    outputtable = 'temptable'
    outputlayer = 'tempXYlayer'
    sr = arcpy.SpatialReference('WGS 1984')
    xfield = 'Longitude'
    yfield = 'Latitude'
    outputfc = 'tempfeatures'
    targetfc = 'All_Elk_Data'

    arcpy.AddMessage("Initial setup complete")

    # Convert text file to geodatabase table
    arcpy.TableToTable_conversion(inputfile,workspace,outputtable)
    arcpy.AddMessage("Table conversion complete")

    # Create XY event layer from geodatabase table
    arcpy.MakeXYEventLayer_management(outputtable,xfield,yfield,outputlayer,sr)
    arcpy.AddMessage("XY event layer creation complete")

    # Create new feature class based on the XY event layer
    arcpy.CopyFeatures_management(outputlayer,outputfc)
    arcpy.AddMessage("Feature class creation complete")

    # Create the field maps
    fmcollar = arcpy.FieldMap()
    fmyear = arcpy.FieldMap()
    fmday = arcpy.FieldMap()
    fmhour = arcpy.FieldMap()
    fmminute = arcpy.FieldMap()
    fmactivity = arcpy.FieldMap()
    fmtemp = arcpy.FieldMap()
    fmlat = arcpy.FieldMap()
    fmlong = arcpy.FieldMap()
    fmhdop = arcpy.FieldMap()
    fmnumsats = arcpy.FieldMap()
    fmfixtime = arcpy.FieldMap()
    fm2d3d = arcpy.FieldMap()

    # Assign fields from the temp feature class to the field maps
    fmcollar.addInputField(outputfc,'CollarSerialNumber')
    fmyear.addInputField(outputfc,'Year')
    fmday.addInputField(outputfc,'Julianday')
    fmhour.addInputField(outputfc,'Hour')
    fmminute.addInputField(outputfc,'Minute')
    fmactivity.addInputField(outputfc,'Activity')
    fmtemp.addInputField(outputfc,'Temperature')
    fmlat.addInputField(outputfc,'Latitude')
    fmlong.addInputField(outputfc,'Longitude')
    fmhdop.addInputField(outputfc,'HDOP')
    fmnumsats.addInputField(outputfc,'NumSats')
    fmfixtime.addInputField(outputfc,'FixTime')
    fm2d3d.addInputField(outputfc,'F2D_3D')

    # Assign fields from the master feature class to the field maps
    fmcollar.addInputField(targetfc, 'CollarSerialNumber')
    fmyear.addInputField(targetfc, 'Year_')
    fmday.addInputField(targetfc, 'Julianday')
    fmhour.addInputField(targetfc, 'Hour_')
    fmminute.addInputField(targetfc, 'Minute_')
    fmactivity.addInputField(targetfc, 'Activity')
    fmtemp.addInputField(targetfc, 'Temperature')
    fmlat.addInputField(targetfc, 'Latitude')
    fmlong.addInputField(targetfc, 'Longitude')
    fmhdop.addInputField(targetfc, 'HDOP')
    fmnumsats.addInputField(targetfc, 'NumSats')
    fmfixtime.addInputField(targetfc, 'FixTime')
    fm2d3d.addInputField(targetfc, 'F2D_3D')

    # Create the field mapping object and add the field maps to it
    fieldmapping = arcpy.FieldMappings()
    fieldmapping.addFieldMap(fmcollar)
    fieldmapping.addFieldMap(fmyear)
    fieldmapping.addFieldMap(fmday)
    fieldmapping.addFieldMap(fmhour)
    fieldmapping.addFieldMap(fmminute)
    fieldmapping.addFieldMap(fmactivity)
    fieldmapping.addFieldMap(fmtemp)
    fieldmapping.addFieldMap(fmlat)
    fieldmapping.addFieldMap(fmlong)
    fieldmapping.addFieldMap(fmnumsats)
    fieldmapping.addFieldMap(fmfixtime)
    fieldmapping.addFieldMap(fm2d3d)

    arcpy.AddMessage("Field mapping complete")

    # Append the new features into the master dataset
    arcpy.Append_management(outputfc,targetfc,"NO_TEST",fieldmapping)
    arcpy.AddMessage("Append complete")

    # Clean up the XY event layer & table & temp feature class
    arcpy.Delete_management(outputlayer)
    arcpy.Delete_management(outputtable)
    arcpy.Delete_management(outputfc)
    arcpy.AddMessage("Cleanup complete")

    arcpy.AddMessage("The appendation (fun word, right?) job has completely succeeded")

# Error handling
except:
    arcpy.AddMessage("Something went wrong - contact justin.ray@dgif.virginia.gov for troubleshooting")
    arcpy.AddMessage(arcpy.GetMessages(2))
    arcpy.AddMessage(arcpy.GetMessages(3))