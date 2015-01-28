'''
Name: Justin Ray
Date: 6/5/2014
Purpose: Add Layers to Active Data Frame
Version: ArcGIS 10.2
'''

# error handling:
try:
    def add_layer(layer_name):
        import arcpy
        # set map document variable
        mxd = arcpy.mapping.MapDocument("CURRENT")
        # set layer variable
        add_layer = arcpy.mapping.Layer(layer_name)
        # add layer to bottom of map document
        arcpy.mapping.AddLayer(mxd.activeDataFrame, add_layer, "BOTTOM")
        # refresh map
        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()
        # clear memory
        del mxd, add_layer
        print 'success'
except:
    print "Something went awry.  Email justin.ray@dgif.virginia.gov"
