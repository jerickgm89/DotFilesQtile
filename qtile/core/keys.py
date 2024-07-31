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
    ([mod], "comma", lazy.prev_screen()),

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
    #([mod, "control"], "s", lazy.shutdown()),
    #([mod, "control"], "r", restart),

    # terminal
    ([mod], "Return", lazy.spawn(cfg.term)),
    ([mod, "shift"], "Return", lazy.spawn(cfg.term2)),

    # app launcher
    ([mod, "shift"], "r", lazy.spawn("rofi -show window -theme \"/home/jerickdev/.config/rofi/launchers/type-1/style-8.rasi\"")),
    ([mod], "r", lazy.spawn("rofi -show drun -theme \"/home/jerickdev/.config/rofi/launchers/type-1/style-8.rasi\"")),

    # web browser
    ([mod], "b", lazy.spawn(cfg.browser)),

    # abri el explorador de archivos en el terminal con ranger
    ([mod, "shift"], "e", lazy.spawn(f"{cfg.term} -e ranger")),

    # screenshot tool
    ([], "Print", lazy.spawn("flameshot gui")),

    # backlight
    ([mod], "XF86AudioLowerVolume", lazy.spawn("brightnessctl set 5%-")),
    ([mod], "XF86AudioRaiseVolume", lazy.spawn("brightnessctl set +5%")),

    # volume
    ([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
    ([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    ([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),

    # player
    ([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    ([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    ([], "XF86AudioNext", lazy.spawn("playerctl next")),

    # Apagar y reiniciar
    ([mod, "control"], "Escape", lazy.spawn("/home/jerickdev/.config/rofi/scripts/powermenu_t6")),
]]  # fmt: skip
