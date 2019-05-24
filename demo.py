from irobot.robots.create2 import Create2
from irobot.openinterface.constants import MODES
# instantiate robot
robot = Create2(port='/dev/serial0')
robot.set_baud(115200)
# read sensor
# print(robot.left_encoder_counts)
# change mode to drive (SAFE|FULL)
robot.oi_mode = MODES.SAFE
robot.drive_straight(50)
# stop driving
robot.drive_straight(0)
# return to passive mode
robot.oi_mode = MODES.PASSIVE
# shutdown OI
robot.stop()
