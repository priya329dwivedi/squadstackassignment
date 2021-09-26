
class ParkingSlot(object):
    """
    This is class which represents parking slot and related operation
    """

    def __init__(self, SlotNo=None, Available=None):
        self.car = None
        self.SlotNo = SlotNo
        self.Available = Available

    @property
    def SlotNo(self):
        return self._slot_no

    @SlotNo.setter
    def SlotNo(self, value):
        self._slot_no = value
    
    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        self._available = value

    @property
    def car(self):
        return self._car

    @car.setter
    def car(self, value):
        self._car = value

   



