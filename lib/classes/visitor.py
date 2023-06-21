class Visitor:

    def __init__(self, name):
        self.name = name
        self._trips = [] #remember to bring in _ if it's not being brought in as a constructor
        self._national_parks = []

    @property
    def name(self):
        return self._name  

    @name.setter
    def name (self, new_name):
        if isinstance(new_name, str) and 1 <= len(new_name) <= 15 and not hasattr(self,'name'):
            #read me didnt say visitor names could not be changed. the error message did
            self._name = new_name
        else:
            raise Exception
        

    def trips(self, new_trip=None):
        from classes.trip import Trip
        if new_trip and isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips
        
    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        if new_national_park and isinstance(new_national_park, NationalPark) and new_national_park not in self._national_parks:
            #to find the unique list you need to tell the system to check that the new park is not in the original park array
            self._national_parks.append(new_national_park)
        return self._national_parks