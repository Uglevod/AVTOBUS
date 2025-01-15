import androidhelper 


droid = androidhelper.Android()


location = droid.getLastKnownLocation().result

location = location.get("gps") or location.get('network')

if location is not None :
    print("Your current location is:")
    #print("Latitude: %s" % location.get('latitude'))
    #print("Longitude: %s" % location.get('longitude'))
    
    print("Latitude: %s" % location['latitude'])
    print("Longitude: %s" % location['longitude'])
    
else:
    print("Unable to retrieve your current location.")