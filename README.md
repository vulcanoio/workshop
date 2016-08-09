Resin Workshop Infrastructure
=============================

________________

Purpose
-------
To enable workshops that allow people with a moderately technical background to understand and use Resin successfully within a 3-8 hour window.

________________

Quick information
-----------------

|                         |                                                |
|-------------------------|------------------------------------------------|
| Radio frequency         | 2.4GHz (smart switches cannot connect to 5GHz) |
| Wireless SSID           | ResinNetwork                                   |
| Wireless authentication | none                                           |
| Router IP address       | 192.168.5.1                                    |
| Router username         | root                                           |
| Router password         | resin                                          |

________________


Workshop Contents
-----------------


| Count | Item                     | Model             | Description                                                          | Link                                      |
|-------|--------------------------|-------------------|----------------------------------------------------------------------|-----------------------------------------------------------|
| 1     | Flight case              | Generic           | Interior dimensions 12.375" x 12.25" x 6.625"                        | [Amazon](https://www.amazon.com/gp/product/B00HRC5N0G) |
| 1     | Wireless router          | TP-Link TL-MR3020 | Custom firmware (see setup in [Appendix 1] below)                    | [Amazon](https://www.amazon.com/gp/product/B00634PLTW) |
| 12    | Breadboards              | Generic           | Small (400 tie points)                                               | [Amazon](https://www.amazon.com/gp/product/B01DDI54II) |
| 12    | Smart outlet switches    | TP-Link HS110     |                                                                      | [Amazon](https://www.amazon.com/gp/product/B0178IC734) |
| 12    | LED plug-in night lights | Maxxima MLN-16    | AC powered; large plastic shields removed and photo sensors disabled | [Amazon](https://www.amazon.com/gp/product/B00IXWYR42) |
| ~100  | 10k Ohm resistors        | Generic           |                                                                      | [Amazon](https://www.amazon.com/gp/product/B0185FGYQA) |
| ~100  | Breadboard wires         | Generic           | Assorted colors and lengths                                          | [Amazon](https://www.amazon.com/gp/product/B005TZJ0AM) |
| ~300  | LEDs                     | Generic           | Assorted colors and voltages                                         | [Amazon](https://www.amazon.com/gp/product/B00UWBJM0Q) |


________________


Prerequisites
-------------

### Site
* Network
   * Connection for host system
* Power
   * Power for each device
   * Power for smart switches (NB: power strips are not ideal for these as they are chunky and take up a lot of space)


### Attendee
* A device with GPIO and WiFi
* An SD card or USB stick for flashing (as required by the device)
* A laptop with git installed
* (Optional) A resin.io account

Using the workshop
------------------
** TODO: **
* Circuit diagrams
* GPIO information
* Resin for workshops information


[Appendix 1]: Setup
-------------------

This describes the initial setup process and should only be necessary for new equipment.  Normal use of the workshop should not require additional setup.


Set up access point
1. Flash firmware: https://wiki.openwrt.org/toh/tp-link/tl-mr3020#installation
   1. NB: You will need an ethernet connection as the firmware will deactivate the radios by default!  It will start a DHCP server on the ethernet port when it boots.
1. Set up password: root/resin
2. Apply config: https://drive.google.com/open?id=0B6cDFLPz_SL-c2FaeWZWX1hTenc
   1. This will activate the radios; you should now share your internet connection over the ethernet port


Set up smart switches
1. Add MAC address from back of switch to router (Network - DHCP and DNS - Advanced Settings - Static Leases)
   1. Use hostname of wsXX and IP address of 192.168.1.1xx (in order)
   2. Save and apply
   3. Label the switch with the hostname and IP address
1. Plug smart switch into power
2. Add the new switch via the Kasa app
   1. Give it the same name (wsXX) as entered in the router
   2. Connect it to ResinWorkshop network


Controlling switches: https://georgovassilis.blogspot.com/2016/05/controlling-tp-link-hs100-wi-fi-smart.html