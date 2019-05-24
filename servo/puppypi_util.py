# Project Imports
import puppypi_config

def printmsg(mymsg):
    if (puppypi_config.verbosemode):
        print (">> {}".format(mymsg))
