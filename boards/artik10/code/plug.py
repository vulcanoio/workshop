#!/usr/bin/env python

# Functions for working with TP-Link HS100 smart plugs
# based on the work by George Georgovassilis:
# https://georgovassilis.blogspot.com/2016/05/controlling-tp-link-hs100-wi-fi-smart.html

import base64
import socket

# Payloads to control plug functionality
payload_on = base64.b64decode("AAAAKtDygfiL/5r31e+UtsWg1Iv5nPCR6LfEsNGlwOLYo4HyhueT9tTu36Lfog==")
payload_off = base64.b64decode("AAAAKtDygfiL/5r31e+UtsWg1Iv5nPCR6LfEsNGlwOLYo4HyhueT9tTu3qPeow==")
payload_query = base64.b64decode("AAAAI9Dw0qHYq9+61/XPtJS20bTAn+yV5o/hh+jK8J7rh+vLtpbr")
payload_emeter = base64.b64decode("AAAAJNDw0rfav8uu3P7Ev5+92r/LlOaD4o76k/6buYPtmPSYuMXlmA==")

light = False

def control(host, payload, port=9999):
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(payload)
    s.shutdown(socket.SHUT_WR)
    retval = ""
    while True:
      data = s.recv(4096)
      if not data:
        break
      retval = retval + data
    s.close()
    return retval
  except:
    print "ERROR: Unable to send data to", host, "on port", port

def toggle_light(host):
  global light
  if light:
    print "Turning off light", host
    payload = payload_off
    light = False
  else:
    print "Turning on light", host
    payload = payload_on
    light = True
  control(host, payload)
