#bunch of imports
from pyfirmata import Arduino, util
from time import sleep

#If this communication port doesent work, choose another one.
board = Arduino("COM4")

#Bunch of variables
digitalpin = board.digital
analogpin = board.analog
iterate = util.Iterator(board)
delay = sleep



#Helpful tips 
#If you wanna read digital pin do 
#analogpin[0].enable_reporting()
#analogpin[4].read()
#digitalpin[0].enable_reporting()
#digitalpin[4].read()
#Documentation: https://pyfirmata.readthedocs.io/en/latest/index.html (Actually Helps)
# My code has abseloutly no licence what so ever so feel free to use it

def ezfirmata_instructions():
    print("The variables that you will need  delay/sleep, Iterate, analogpin and digitalpin")


# a sample code
def blinktest():
    while True:
        # digitalpin[4].write(1) 1 = on 0 = off 
        # digitalpin = pin selector on arduino
        digitalpin[13].write(1)
        sleep(1)
        digitalpin[13].write(0)
        sleep(1)

def analogreadtest():
    iterate.start()
    while True:
        analogpin[0].enable_reporting()
        print(analogpin[0].read())
        sleep(1)
