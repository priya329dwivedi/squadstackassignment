class Car(object):
    """
    This is class which represents details of a car.
   
    reg_no = Car Registration Number
    age = Age of Driver 

    """

    def __init__(self):
        self._reg_no = None
        self._age = None

   
    @property
    def Age(self):
        return self._age

    @Age.setter
    def Age1(self, value):
        self.Age1 = value
    
    @property
    def reg_no(self):
        return self._reg_no

    @reg_no.setter
    def reg_no(self, value):
        self._reg_no = value


    @classmethod
    def create(cls, RegistrationNo, Age):
        CarObj = cls()
        CarObj.reg_no = RegistrationNo
        CarObj.age = Age
        return CarObj
