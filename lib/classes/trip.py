
class Trip:
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = str(start_date)
        self.end_date = str(end_date)
        #Everybody knows where everybody has been
        #vvv this appends this specific trip into visitor
        self.visitor.trips(self)
        #vvv this appends this national_park into visitor
        self.visitor.national_parks(self.national_park)
        #vvv this appends this specific trip into visitor
        self.national_park.trips(self)
        #vvv this appends this national_park into visitor
        self.national_park.visitors(self.visitor)
        
        #trip is being called to do everything so we can consider it to be the single source of truth
        #since its the SoT we need to make sure it inserts itself and visitor and national_park into
        #the other classes. 

    @property
    def visitor (self):
        return self._visitor
    
    @visitor.setter
    def visitor (self, new_visitor):
        from classes.visitor import Visitor
        if new_visitor and isinstance(new_visitor, Visitor):
            self._visitor = new_visitor
        else:
            raise Exception

    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park (self, new_national_park):
        from classes.national_park import NationalPark
        if new_national_park and isinstance(new_national_park, NationalPark):
            self._national_park = new_national_park
        else:
            raise Exception
