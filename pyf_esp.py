import pyfirmata

RELAY_PIN = 5 #D1 ESP8226 NODEMCU 12E
comport = 'COM3'
board = pyfirmata.Arduino(comport)
print("Board Connected")

def relay_trigger(finger_up):
    if finger_up==[0,1,0,0,0]:
        board.digital[RELAY_PIN].write(1)
        print('ON')

    elif finger_up==[0,1,1,0,0]:
        board.digital[RELAY_PIN].write(0)
        print('OFF')
    
def board_exit():
    board.exit()
    print("Board Disconnected")