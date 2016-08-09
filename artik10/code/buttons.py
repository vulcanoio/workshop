#!/usr/bin/env python

import workshop
import plug
import time

##### Configuration

# Pins 8,9 map to GPIO 2,3 on the a10
button = 8
led = 9


##### Main code

workshop.setup_pin(button, "in") # set up the button for input
workshop.setup_pin(led, "out")   # set up the led for output
cloud = workshop.setup_cloud()   # set up the Artik Cloud connection
presses = 0                      # start with the button pressed 0 times


print "Starting the application..."

# Loop forever checking the button every second
while True:
  if workshop.is_pushed(button):
    print "Button pushed!"
    presses = presses + 1
    plug.toggle_light("192.168.5.111")
    # Uncomment the next line to work with the cloud!
    #workshop.send_pressed_message(cloud, presses)
    workshop.toggle(led)
    time.sleep(.25)
