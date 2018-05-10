# Libraries
from microbit import *

#Global variables
state=0
time_point=0
led_brigth=7
pomodoro_time=1200000 #Milliseconds

#uart initialization
uart.init(baudrate=9600, bits=8, parity=None, stop=1, tx=None, rx=None)

while True:

    #Reading data from UART
    echo=str(uart.readline())
    echo=echo.replace("b","",1)
    echo=echo.replace("\'","")

    #Transitions events
    if(echo!="None"):
        uart.write(echo)
        #display.scroll(echo)
        if echo=="heart":
            display.show(Image.HEART)
    elif (button_a.is_pressed()):
        if state>=4:
            state=0
        else:
            state=state+1
        sleep(200)
    elif (button_b.is_pressed()):
        time_point=running_time()
        state=-1
        sleep(200)

    #State machine
    if state==0:
        display.clear()
    elif state==1:
        display.show(Image.YES)
    elif state==2:
        display.show(Image.NO)
    elif state==3:
        display.scroll("Comiendo")
    elif state==4:
        display.scroll("T: "+str(temperature()))
    elif state==-1:
        #display.scroll("Pomodoro")
        # display.show(range(4,-1,-1))

        #Fill the screen
        for y in range(4,-1,-1):
            for x in range (4,-1,-1):
                display.set_pixel(x, y, led_brigth)
                #sleep(5000)

        for y in range(0,5,1):
            for x in range (0,5,1):
                display.set_pixel(x, y, 0)
                sleep((pomodoro_time/25))

    sleep(50)
