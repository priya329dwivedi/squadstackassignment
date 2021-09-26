import lot, car

class Parking(object):
    def __init__(self):
        self.slots = {}

    def Create_parking_lot(self, NoOfSlots):
        NoOfSlots = int(NoOfSlots)

        if len(self.slots) > 0:
            print("Parking Lot already created")
            return

        if NoOfSlots > 0:
            for i in range(1, NoOfSlots+1):
                temp_slot = lot.ParkingSlot(SlotNo=i,
                                    Available=True)
                self.slots[i] = temp_slot
            print("Created parking of %s slots" % NoOfSlots)
        else:
            print("Number of slots Is incorrect.")
        return

    def nearest_available_slot(self):
        AvailableSlots = [x for x in list(self.slots.values()) if x.Available]
        if not AvailableSlots:
            return None
        return sorted(AvailableSlots, key=lambda x: x.SlotNo)[0]

    def Park(self, reg_no, driver_age, age):
        

        if not self._do_primary_checks():
            return

        available_slot = self.nearest_available_slot()
        if available_slot:
            # create car object and save in the available slot
            available_slot.car = car.Car.create(reg_no, age)
            available_slot.Available = False
            print("Car with vehicle registration number ",reg_no," has been parked at slot number ",available_slot.SlotNo)
        else:
            print("Sorry, parking lot is full.")

    def Leave(self, SlotNo):
        SlotNo = int(SlotNo)
        if not self._do_primary_checks():
            return

        if SlotNo in self.slots:
            pslot = self.slots[SlotNo]
            if not pslot.Available and pslot.car:
                pslot.car = None
                pslot.Available = True
                print("Slot number ",SlotNo," is vacated")
                # the car with vehicle registration number",car.reg_no,
                #" left the space, the driver of the car was of age ",car.age)
            else:
                print("No car is present at slot number %s" % SlotNo)
        else:
            print("Sorry, slot number does not exist in parking lot.")

    def Status(self):
        if not self._do_primary_checks():
            return

        print("Slot No\tRegistration No\tAge")
        for i in list(self.slots.values()):
            if not i.Available and i.car:
                print("%s\t%s\t%s" % (i.SlotNo, i.car.reg_no, i.car.age))

    def _do_primary_checks(self):
        if len(self.slots) == 0:
            print("Parking Lot not created")
            return False
        return True

    def Vehicle_registration_number_for_driver_of_age(self, age):
        if not self._do_primary_checks():
            return

        reg_nos = ''
        for pslot in list(self.slots.values()):
            if not pslot.Available and pslot.car and \
                pslot.car.age == age:
                reg_nos += '%s ' % pslot.car.reg_no

        if reg_nos:
            print(reg_nos[:-1])
        else:
            print("null")

    def Slot_numbers_for_driver_of_age(self, age):
        """Method to find slot numbers for cars with given age in
        parking.
        Input: age - String Type
        """

        if not self._do_primary_checks():
            return

        slot_nos = ''
        for pslot in list(self.slots.values()):
            if not pslot.Available and pslot.car and \
                pslot.car.age == age:
                slot_nos += '%s ' % pslot.SlotNo

        if slot_nos:
            print(slot_nos[:-1])
        else:
            print("Not found")

    def Slot_number_for_car_with_number(self, reg_no):

        if not self._do_primary_checks():
            return

        slot_no = ''
        for pslot in list(self.slots.values()):
            if not pslot.Available and pslot.car and \
                pslot.car.reg_no == reg_no:
                slot_no = pslot.SlotNo
                break

        if slot_no:
            print(slot_no)
        else:
            print("Not found")

