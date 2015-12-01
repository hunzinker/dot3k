#!/usr/bin/env bash
if [ -z $1 ]; then
    su - pi -c "/home/pi/bin/headless_pianobar" > /dev/null &
    sleep 0.5
    su - pi -c "/bin/pidof pianobar"
else
    su - pi -c "echo -ne \"${1}\" > /home/pi/.config/pianobar/ctl"
fi
