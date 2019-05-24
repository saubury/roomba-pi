from  pycreate2 import Create2
import time

# Create a Create2.
bot = Create2(port='/dev/serial0')

# Start the Create 2
bot.start()

# Put the Create2 into 'safe' mode so we can drive it
# This will still provide some protection
bot.safe()

# You are responsible for handling issues, no protection/safety in
# this mode ... becareful
# bot.full()

# directly set the motor speeds ... easier if using a joystick
bot.drive_direct(100, 100)


bot.drive_straight(50)
time.sleep(1)


bot.drive_straight(-50)
time.sleep(1)


# turn an angle [degrees] at a speed: 45 deg, 100 mm/sec
bot.turn_angle(10, 50)

time.sleep(2)

bot.turn_angle(-10, 50)

time.sleep(2)




# Stop the bot
bot.drive_stop()

# Close the connection
bot.close()


