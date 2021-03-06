# Name: Justin Ray
# Date: 8/4/11
# Purpose: Add Counties Shapefile
# Version: ArcGIS 10+

# error handling:
try:
    import arcpy
# defined workspace
    arcpy.env.workspace = r'K:\GISData\boundaries'
# set map document variable
    mxd = arcpy.mapping.MapDocument("CURRENT")
# set dataframe variable
    df = arcpy.mapping.ListDataFrames(mxd,'Layers')[0]
# set layer variable
    addLayer = arcpy.mapping.Layer(r'K:\GISData\boundaries\Counties.lyr')
# add layer to map document
    arcpy.mapping.AddLayer(df, addLayer, "BOTTOM")
# refresh map
    arcpy.RefreshActiveView()
    arcpy.RefreshTOC()
# clear memory
    del mxd, addLayer
except:
    print "Script failt contact JAWR"