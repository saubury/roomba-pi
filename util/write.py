import serial
import time
 
# Open a serial connection to Roomba
ser = serial.Serial(port='/dev/serial0', baudrate=115200)
 
# Assuming the robot is awake, start safe mode. Note that 0x83 in hexadecimal corresponds to 131.
ser.write('\x83')
 
time.sleep(.1)
 
# Start cleaning - 135
ser.write('\x87')
 
# Stop (back to off mode) - 173
time.sleep(3.0)
ser.write('\xAD')
 
# Close the serial port; we're done for now.
ser.close()
