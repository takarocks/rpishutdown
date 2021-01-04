# RPi Button Shutdown and Boot
Raspberry Pi (RPi) button shutdown python3 script. The button shuts down RPi safely by executing `sudo shutdown -h now` command if the button is keep pressed more than 3 seconds. This button also works as RPi power on if the power outlet is connected and RPi is in shutdown state. You do not need to unplug/plug power outlet.

* Version 0.2
* January 4, 2021
* Taka Kitazume


## Prerequisites

* Raspberry Pi (2, 3B, 3B+, Zero) x 1
  * Raspberry Pi OS (Lite)
  * git
* Tacticle button x 1
* Resister 330Ω~680Ω x 1
* Breadboard x 1
* Jumper wires Male/Female x 2


## Diagram
<kbd>
<img src="assets/rpishutdowndetector.png" />
</kbd>


## Setup

1. Assemble your kit as you see in the diagram. You must use GPIO3 for one side of the tacticle button. You can use any ground pin.
2. Create **services** directory under `pi` user home directory, move to that directory.
  ```
  cd ~
  mkdir services
  cd services
  ```
3. Git clone this project
  ```
  git clone https://github.com/takarocks/rpishutdowndetector.git
  ```
4. Change to project directory `rpishutdowndetector`
  ```
  cd rpishutdowndetector
  ```
4. Copy the shutdowndtector.service file into **/etc/systemd/system/** directory.
  ```
  sudo cp shutdowndtector.service /etc/systemd/system/shutdowndtector.service
  ```
5. Start and enable the shutdowndetector.service.
  ```
  sudo systemctl start shutdowndetector.service
  sudo systemctl enable shutdowndetector.service
  ```
6. Press the tacticle button longer than 3 seconds. RPi should shutdown.
7. Keep the outlet connected, press the tacticle button again when RPi is in shutdown state. The power is on and RPI boots.
8. Execute `systemctl` and confirm shutdowndetector.service is loaded, active and running.
  ```
  systemctl

  UNIT                        LOAD   ACTIVE SUB       DESCRIPTION              
  shutdowndetector.service    loaded active running   Button shutdown detector  
  ```




## References
[systemd](https://www.raspberrypi.org/documentation/linux/usage/systemd.md) [www.raspberrypi.org]
