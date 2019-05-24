import serial
import time
 
# Open a serial connection to Roomba
ser = serial.Serial(port='/dev/serial0', baudrate=115200)


# Assuming the robot is awake, start safe mode so we can hack.
ser.write('\x83')
time.sleep(.1)

# Program a five-note start song into Roomba.
ser.write('\x8c\x00\x05C\x10H\x18J\x08L\x10O\x20')

# Play the song we just programmed.
ser.write('\x8d\x00')
time.sleep(1.6) # wait for the song to complete

# Leave the Roomba in passive mode; this allows it to keep
#  running Roomba behaviors while we wait for more commands.
ser.write('\x80')

ser.write('\x87')
time.sleep(1.0) # wait for the song to complete

# Stop (back to off mode) - 173
ser.write('\xAD')
time.sleep(1.0) # wait for the song to complete

# Close the serial port; we're done for now.
ser.close()
