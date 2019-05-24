from  pycreate2 import Create2
import time

# Create a Create2.
bot = Create2(port='/dev/serial0')

# Start the Create 2
bot.start()

# Put the Create2 into 'safe' mode so we can drive it
# This will still provide some protection
bot.safe()

bot.turn_angle(-50, +250)

# time.sleep(2)




# Stop the bot
bot.drive_stop()

# Close the connection
bot.close()


