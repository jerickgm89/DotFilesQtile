#!/bin/bash

MONITORS=("HDMI-0" "DP-5")
STEP=${2:-5}  # Porcentaje por defecto: 5%

get_brightness() {
    xrandr --verbose | grep -A 5 "$1" | grep -i brightness | head -1 | cut -f2 -d ' '
}

for monitor in "${MONITORS[@]}"; do
    CURRENT=$(get_brightness "$monitor")
    
    case $1 in
        down)
            NEW=$(echo "scale=2; $CURRENT - ($STEP / 100)" | bc)
            if (( $(echo "$NEW < 0.1" | bc -l) )); then NEW="0.1"; fi
            ;;
        up)
            NEW=$(echo "scale=2; $CURRENT + ($STEP / 100)" | bc)
            if (( $(echo "$NEW > 1.0" | bc -l) )); then NEW="1.0"; fi
            ;;
    esac
    
    xrandr --output "$monitor" --brightness "$NEW"
done