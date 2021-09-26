#!/usr/bin/python
#HELLO EVERYONE
import os, sys
import parking

class ParkingCommands(object):

    def __init__(self):
        self.parking = parking.Parking()

    def process_file(self, GivenFile):
        if not os.path.exists(GivenFile):
            print("Given file %s does not exist" % GivenFile )

        FileObj = open(GivenFile)
        try:
            while True:
                line1 = next(FileObj)
                if line1.endswith('\n'): line1 = line1[:-1]
                if line1 == '': continue
                self.process_command(line1)
        except StopIteration:
            FileObj.close()
        except Exception as ex:
            print("Error occured while processing file %s" % ex)

    def process_input(self):
        try:
            while True:
                StdinInput = input("Enter Input-> ")
                self.process_command(StdinInput)
        #except (KeyboardInterrupt, sys.exit()):
         #   return
        except Exception as ex:
            print("Error occured while running %s" % ex)


    def process_command(self, StdinInput):
        inputs = StdinInput.split()
        command = inputs[0]
        params = inputs[1:]
        if hasattr(self.parking, command):
            CommandFunction = getattr(self.parking, command)
            CommandFunction(*params)
        else:
            print("Got wrong input.")


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        PkCommand = ParkingCommands()
        PkCommand.process_input()
    elif len(args) == 2:
        PkCommand = ParkingCommands()
        PkCommand.process_file(args[1])
    else:
        print("Wrong number of arguments.\n" \
                "Usage:\n" \
                "./parking_lot.py <filename> OR \n" \
                "./parking_lot.py")

