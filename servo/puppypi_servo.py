import time
import pigpio
import puppypi_config
import puppypi_util

def servo_on():
    pi = pigpio.pi() # Connect to local Pi.


def servo_centre():
    puppypi_util.printmsg('Servo centred')
    puppypi_config.servo_x = puppypi_config.x_mid
    puppypi_config.servo_y = puppypi_config.y_mid    
    servo_update()

def servo_delta(delta_x, delta_y):
    puppypi_config.servo_x += delta_x
    puppypi_config.servo_y += delta_y
    
    if (puppypi_config.servo_x < puppypi_config.x_min):
        puppypi_config.servo_x = puppypi_config.x_min
        
    if (puppypi_config.servo_x > puppypi_config.x_max):
        puppypi_config.servo_x = puppypi_config.x_max

    if (puppypi_config.servo_y < puppypi_config.y_min):
        puppypi_config.servo_y = puppypi_config.y_min
        
    if (puppypi_config.servo_y > puppypi_config.y_max):
        puppypi_config.servo_y = puppypi_config.y_max

    servo_update()

def servo_update():
    servo_xy(puppypi_config.servo_x, puppypi_config.servo_y)

def servo_xy(x, y):
    if (not puppypi_config.servousage):
        puppypi_util.printmsg("Servo Ignored :  x:{} y:{}".format(x, y))
        return
        
    puppypi_util.printmsg("Servo x:{} y:{}".format(x, y))
    pi = pigpio.pi() # Connect to local Pi.
    pi.set_servo_pulsewidth(puppypi_config.gpio_x,  x)
    pi.set_servo_pulsewidth(puppypi_config.gpio_y,  y)


def servo_demo():
    servo_centre()
    time.sleep(0.5)

    servo_delta(+150, 0)
    time.sleep(0.5)
    servo_delta(+150, 0)
    time.sleep(0.5)
    servo_delta(+150, 0)
    time.sleep(0.5)

    servo_delta(0, -150)
    time.sleep(0.5)
    servo_delta(0, -150)
    time.sleep(0.5)
    servo_delta(0, -150)
    time.sleep(0.5)

    servo_delta(-150, 0)
    time.sleep(0.5)
    servo_delta(-150, 0)
    time.sleep(0.5)
    servo_delta(-150, 0)
    time.sleep(0.5)

    time.sleep(0.5)
    servo_centre()

def servo_off():
    # switch servo off
    time.sleep(0.8)
    pi = pigpio.pi() # Connect to local Pi.
    pi.set_servo_pulsewidth(puppypi_config.gpio_x,  0);
    pi.set_servo_pulsewidth(puppypi_config.gpio_y,  0);
    pi.stop()
