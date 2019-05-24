# Project Imports
import puppypi_config
import puppypi_util
import puppypi_aws
import puppypi_servo
import puppypi_video
import RPi.GPIO as GPIO
import datetime
import time

def button_setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(puppypi_config.gpio_button_green, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(puppypi_config.gpio_button_yellow, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button_is_green():
    return GPIO.input(puppypi_config.gpio_button_green) == False

def button_is_yellow():
    return GPIO.input(puppypi_config.gpio_button_yellow) == False

def do_button():
    puppypi_util.printmsg("Button Press Mode")
    button_setup()

    while True:
        time.sleep(0.2)

        if button_is_yellow():
            print('Button Pressed Yellow')
            puppypi_servo.servo_on()
            puppypi_video.process_livevideo()
            puppypi_servo.servo_off()
            time.sleep(0.2)

        if button_is_green():
            print('Button Pressed Green')
            file_string='./tmp/snapped_{}'.format(datetime.datetime.today().strftime('%Y%m%d-%H%M%S'))
            puppypi_aws.mainAWS(file_string)
            time.sleep(0.2)

def do_button_debug():
    puppypi_util.printmsg("Debug Button Press Mode")
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(puppypi_config.gpio_button_pcb, GPIO.IN)

    while True:
        input_state = GPIO.input(puppypi_config.gpio_button_pcb)
        if input_state == False:
            print('Button Pressed')
            time.sleep(0.2)


