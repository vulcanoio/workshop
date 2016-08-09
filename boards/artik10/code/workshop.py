#!/usr/bin/env python

import time
import os
import artikcloud

token = os.getenv('ARTIKCLOUD_DEVICE_TOKEN')
sdid = os.getenv('ARTIKCLOUD_DEVICE_ID')

last_status = {}

def setup_pin(pin, direction = "in"):
  # Make the pin available
  try:
    pinctl = open("/sys/class/gpio/export", "wb", 0)
    pinctl.write(str(pin))
    print "Pin ", str(pin), " is now exported."
  except:
    print "Pin ", str(pin), " was already exported."
  pinctl.close()

  # Set pin I/O mode
  pinctl = open("/sys/class/gpio/gpio%d/direction" % pin, "wb", 0)
  pinctl.write(direction)
  pinctl.close()

  if direction == "in":
    # Track status of input pins so we can avoid 'bounce' on buttons
    last_status[pin] = 0


def setup_cloud():
  api_client = artikcloud.ApiClient()
  api_client.set_default_header(header_name="Authorization", header_value="Bearer {}".format(token))
  return artikcloud.MessagesApi(api_client)

def send_pressed_message(cloud, presses):
  message = artikcloud.MessageAction()
  message.type = "message"
  message.sdid = "{}".format(sdid)
  message.ts = int(round(time.time() * 1000))  # timestamp, required
  message.data = {'presses': presses}
  response = cloud.send_message_action(message)
  print(response)

def get_pin(pin):
  pf = open("/sys/class/gpio/gpio%d/value" % pin, "rb", 0)
  val = pf.read().strip()
  pf.close()
  return val

def set_pin(pin, value=1):
  pf = open("/sys/class/gpio/gpio%d/value" % pin, "wb", 0)
  pf.write(str(value))
  pf.close()

def is_pushed(pin):
  # Check if a pin has been activated and was not previously
  global last_status
  current_status = get_pin(pin)
  if last_status[pin] != current_status:
    if current_status == "1":
      # last == 0, current == 1
      last_status[pin] = 1
      return True
    else:
      # last == 1, current == 0
      last_status[pin] = 0
  return False

def toggle(pin):
  cur = get_pin(pin)
  val = "1"
  if cur == "1":
    val = "0"
  set_pin(pin, val)
