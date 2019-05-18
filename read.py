import serial
import time
 
# Open a serial connection to Roomba
ser = serial.Serial(port='/dev/serial0', baudrate=115200)

print("connected to: " + ser.portstr)

#this will store the line
line = []

while True:
    for c in ser.read():
        line.append(c)
        if c == '\n':
            print("Line: " + ''.join(line))
            line = []
            break

ser.close()
