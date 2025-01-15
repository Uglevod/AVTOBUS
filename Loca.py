import androidhelper 



class Loca():
    def __init__(self):
       
  
        self.areas = [
            
            { "arr":"dacha", "loc":{ 'lat': 56.186042, 'lng': 93.414396 }, "rad":5 },
            
            { "arr":"dom"  , "loc":{ 'lat': 56.251276, 'lng': 93.528958 }, "rad":10 },
            { "arr":"gorod", "loc":{ 'lat': 56.239433, 'lng': 93.516394 }, "rad":15 },
            
            { "arr":"kras" , "loc":{ 'lat': 56.011688, 'lng': 92.865071 }, "rad":20 }
        ]

    def get_area(self):
        
        self.droid = androidhelper.Android()
        
        location = self.droid.getLastKnownLocation().result
        
        location = location.get("gps") or location.get('network')
        
        if location is not None :
        
            for area in self.areas:
                
                res = self.is_in_radius( area['loc']['lat'], area['loc']['lng'], location['latitude'], location['longitude'], area["rad"] )
                
                if res[0]:
                    print( res[1] )
                    return area['arr'] , res[1]

        
        
        
    def is_in_radius( self , lat1, lon1 , lat2 , lon2 , rad ):
        
        import math
        
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        
        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a)) 
        
        r = 6371 # Radius of earth in kilometers. Use 3956 for miles
        return c * r <=rad , c * r

        #dlat = lat2 - lat1
        #dlon = lon2 - lon1

        #a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        #c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        #return radius_m * c <= rad

 