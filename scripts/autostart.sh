#!/bin/bash

# Ejecuta la configuracion de Picom

picom --config /home/erick/.config/qtile/picom/picom.conf &
polychromatic-cli -e JErick &

# Configura los monitores
xrandr --output HDMI-0 --auto --below DP-5 &

