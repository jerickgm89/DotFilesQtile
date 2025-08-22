#!/bin/bash

# Ejecuta la configuracion de Picom

picom --config /home/erick/.config/qtile/picom/picom.conf &
# polychromatic-cli -e JErickDev &

# Configura los monitores
xrandr --output HDMI-0 --mode 1920x1080 --pos 0x0 --output DP-5 --mode 2560x1080 --right-of HDMI-0 --primary &

