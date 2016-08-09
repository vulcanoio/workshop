Create device
-------------
 1. Log into developer.artik.cloud/dashboard
 2. Your device types - New device type
 3. Fill in form
  a. Resin workshop
  b. io.resin.workshop.samsung.artik10 is mine (you might want com.samsung.yourname.whatever)
 4. Create device type
 5. New manifest (button, not dropdown!)
  a. Device fields
   i. Name: presses
   ii. Type: integer
   iii. Save
  b. Device actions
   i. Action: toggleLight
   ii. Description: Toggle the LED on or off
   iii. Save
  c. Activate manifest
   i. Activate manifest
 6. Go to artik.cloud/my
 7. Connect another device
 8. Enter the name you put earlier (e.g. Resin workshop)
 9. Gear on new device
  a. Copy Device ID
  b. Paste Device ID into script
 10. Go to developer.artik.cloud/api-console
  a. Scroll down to "Get Current User Profile"
  b. Click "Try it"
  c. Copy authorization (after "bearer")
  d. Paste token into environment variable -- IMPORTANT: LEAVE THIS TAB OPEN
 11. git push resin master
 12. Go to artik.cloud/my/data
  a. Add a chart for the device
  b. Push the button on the device
  c. Push "play" on the chart


Flashing device
---------------
1. Download and install Etcher. You can also use another image writer of your choice. 
2. Start the writer and select the Device OS .img file in your downloads folder. 
3. Insert your SD card and press "Burn!".
4. Wait until it's finished writing.
5. Safely eject the freshly burnt SD card and insert into the Samsung Artik 10.
6. Set SW2 dip switch to position 1:on, 2:on. Also, make sure jumpers J20 and J36 are set towards the edge of the board.
7. Press the power switch PSW1 to the on position. Press and hold for 1 second the SW3 POWER push button.
8. The device has performed a shutdown. Press the power switch PSW1 to the off position.
9. Remove the resin.io installation media.
10. Set SW2 dip switch to position 1:off, 2:off.
Press the power switch PSW1 to the on position. Press and hold for 1 second the SW3 POWER push button.
Your device should appear here in about 10 minutes. Have fun!

