from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse
import time
import cv2
import sys
import imutils
import RPi.GPIO as GPIO
import time

# Project Imports
import puppypi_config
import puppypi_util
import puppypi_servo
import puppypi_video
import puppypi_aws
import puppypi_button


def main():
    parser = argparse.ArgumentParser(description='Face processing puppy.')


    parser.add_argument("-x", "--servo_x", type=int, help="servo x setting")
    parser.add_argument("-y", "--servo_y", type=int, help="servo y setting")
    parser.add_argument("--videofile", help="pre recorded video file")
    parser.add_argument("--aws", help="test AWS")
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    parser.add_argument("-b", "--button", help="wait for external button press", action="store_true")
    parser.add_argument("-db", "--debugbutton", help="print a debug message on PCB button press", action="store_true")
    parser.add_argument("--noservo", help="surpress the servo", action="store_true")
    parser.add_argument("--livevideo", help="live video", action="store_true")
    parser.add_argument("--servodemo", help="demonstrate the servo", action="store_true")
    parser.add_argument("--showvideoframe", help="Display a video frame via XWindows", action="store_true")
    parser.add_argument("--novideo", help="Surpress a video frame via XWindows", action="store_true")
    
    args = parser.parse_args()

    puppypi_config.verbosemode= args.verbose
    puppypi_config.showvideoframe= args.showvideoframe
    puppypi_config.novideo= args.novideo

    if args.noservo:
        puppypi_config.servousage = False
        puppypi_util.printmsg("Servo turned off")

    if (args.livevideo):
        puppypi_servo.servo_on()
        puppypi_video.process_livevideo()
        puppypi_servo.servo_off()

    elif (args.button):
        puppypi_button.do_button()

    elif (args.aws):
        puppypi_aws.mainAWS(args.aws)

    elif args.videofile:
        puppypi_config.servousage = False
        puppypi_video.process_video(args.videofile)
 
    elif (args.servo_x >0 and args.servo_y >0):
        puppypi_servo.servo_on()
        puppypi_servo.servo_xy(args.servo_x, args.servo_y)
        puppypi_servo.servo_off()
        
    elif args.servodemo:
        puppypi_util.printmsg("Servo Demo")
        puppypi_servo.servo_on()
        puppypi_servo.servo_demo()
        puppypi_servo.servo_off()

    elif (args.debugbutton):
        puppypi_button.do_button_debug()



if __name__ == "__main__":
    try:
        main()

    finally:
        puppypi_servo.servo_off()
        puppypi_util.printmsg ("Cleanup and exit")


