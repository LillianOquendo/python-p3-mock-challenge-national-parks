class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name (self, new_name):
        if not hasattr(self, 'name') and isinstance(new_name, str):
            self._name = new_name
        else:
            raise Exception


    def trips(self, new_trip=None):
        from classes.trip import Trip
        if new_trip and isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        if new_visitor and isinstance(new_visitor, Visitor) and new_visitor not in self._visitors:
            self._visitors.append(new_visitor)
        return self._visitors

    
    def total_visits(self):
        return len(self._trips) #this gets the size of the trips array AKA the total # of visits
    
    def best_visitor(self):
        max_visitor = None
        max_visits = 0

        for visitor in self._visitors:
            visits = 0
            for trip in self._trips:
                if visitor == trip.visitor:
                    visits += 1
            if visits > max_visits:
                max_visitor = visitor
                max_visits = visits

        return max_visitor