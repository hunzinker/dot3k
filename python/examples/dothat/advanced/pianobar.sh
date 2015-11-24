#!/usr/bin/env bash
su - pi -c "/home/pi/bin/headless_pianobar" > /dev/null &
sleep 0.5
su - pi -c "/bin/pidof pianobar"
