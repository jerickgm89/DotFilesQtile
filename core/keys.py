from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from extras import float_to_front
from utils.config import cfg

if cfg.is_xephyr:
    mod, alt = "mod1", "control"
    restart = lazy.restart()
else:
    mod, alt = "mod4", "mod1"
    restart = lazy.reload_config()

if not cfg.term:
    cfg.term = guess_terminal()

rofi_applets = 'home/erick/.config/qtile/scripts/'

keys = [Key(*key) for key in [  # type: ignore
    # switch between windows
    ([mod], "h", lazy.layout.left()),
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "l", lazy.layout.right()),

    # move windows between columns
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),

    # Switch focus of monitors
    ([mod], "period", lazy.next_screen()),

    # increase/decrease window size
    ([mod], "minus", lazy.layout.shrink()),
    ([mod], "equal", lazy.layout.grow()),

    # window management
    ([mod, "shift"], "space", lazy.layout.flip()),
    ([mod], "m", lazy.layout.maximize()),
    ([mod], "a", lazy.window.kill()),
    ([], "F11", lazy.window.toggle_fullscreen()),

    # floating window management
    ([mod], "space", lazy.window.toggle_floating()),
    ([mod], "s", lazy.function(float_to_front)),
    ([mod], "c", lazy.window.center()),

    # toggle between layouts
    ([mod], "Tab", lazy.next_layout()),

    # qtile stuff
    ([mod, "control"], "b", lazy.hide_show_bar()),
    ([mod, "control"], "s", lazy.shutdown()),
    ([mod, "control"], "r", restart),

    # terminal
    ([mod], "Return", lazy.spawn(cfg.term)),
    ([mod, "shift"], "Return", lazy.spawn(cfg.term2)),

    # app launcher
    ([mod, "shift"], "r", lazy.spawn("rofi -show window -theme \"/home/erick/.config/rofi/launchers/type-1/style-8.rasi\"")),
    ([mod], "r", lazy.spawn("/home/erick/.config/rofi/scripts/launcher_t1")),
    
    
    # web browser
    ([mod], "b", lazy.spawn(cfg.browser)),

    # abri el explorador de archivos en el terminal con ranger
    ([mod, "shift"], "e", lazy.spawn(f"{cfg.term} -e ranger")),

    # screenshot tool
    ([], "Print", lazy.spawn("flameshot gui --delay 1000")),

    # # backlight
    # ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 5%-")),
    # ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set +5%")),

    # Brightness
    ([mod, "control"], "1", lazy.spawn("xrandr --output HDMI-0 --brightness 0.1")),
    ([mod, "control"], "2", lazy.spawn("xrandr --output HDMI-0 --brightness 0.2")),
    ([mod, "control"], "3", lazy.spawn("xrandr --output HDMI-0 --brightness 0.3")),
    ([mod, "control"], "4", lazy.spawn("xrandr --output HDMI-0 --brightness 0.4")),
    ([mod, "control"], "5", lazy.spawn("xrandr --output HDMI-0 --brightness 0.5")),
    ([mod, "control"], "6", lazy.spawn("xrandr --output HDMI-0 --brightness 0.6")),
    ([mod, "control"], "7", lazy.spawn("xrandr --output HDMI-0 --brightness 0.7")),
    ([mod, "control"], "8", lazy.spawn("xrandr --output HDMI-0 --brightness 0.8")),
    ([mod, "control"], "9", lazy.spawn("xrandr --output HDMI-0 --brightness 0.9")),
    ([mod, "control"], "0", lazy.spawn("xrandr --output HDMI-0 --brightness 1.0")),

    # volume
    ([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
    ([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    ([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),

    # player
    ([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    ([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    ([], "XF86AudioNext", lazy.spawn("playerctl next")),


    # change keyboard layout
    ([mod], "t", lazy.spawn("setxkbmap -layout us -variant altgr-intl")),

    # Apagar y reiniciar
    ([mod, "control"], "Escape", lazy.spawn("/home/erick/.config/rofi/scripts/powermenu_t6")),
]]  # fmt: skip
