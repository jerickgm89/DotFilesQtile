#!/bin/bash

# Ejecuta la configuracion de Picom

picom --config /home/erick/.config/qtile/picom/picom.conf &
polychromatic-cli -e JErickDev &

# Configura los monitores
xrandr --output DVI-I-1 --mode 2560x1080 --pos 0x0 --primary --output HDMI-0 --mode 1366x768 --left-of DVI-I-1 &

