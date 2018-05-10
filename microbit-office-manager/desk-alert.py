import serial, time
port = "/dev/ttyACM0"
baud = 115200
s = serial.Serial(port)
s.baudrate = baud
while True:
    data = s.readline()
    #data = int(data[0:4])
    print(data)
    time.sleep(1)
