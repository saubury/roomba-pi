from time import sleep
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(13, GPIO.OUT, initial=GPIO.HIGH) # Set pin 8 to be an output pin and set initial value to low (off)

GPIO.output(13, GPIO.LOW) # Turn off
sleep(1) # Sleep for 1 second
GPIO.output(13, GPIO.HIGH) # Turn on
