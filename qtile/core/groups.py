from libqtile.config import Group, Key
from libqtile.lazy import lazy

from core.keys import keys, mod
from utils.match import wm_class

groups: list[Group] = []

for key, label, layout, matches in [
    ("1", "", None, wm_class("alacritty", "kitty", "wezterm")),
    ("2", "", "max", wm_class("code", "nvim")),
    ("3", "", "max", wm_class("google-chrome-stable", "microsoft-edge-stable")),
    ("8", "", None, wm_class("Settings Manager")),
    ("9", "󰇮", "max", wm_class("discord", "telegram-desktop", "Slack")),
    ("0", "", "max", wm_class("spotify", "vlc")),
]:
    groups.append(Group(key, matches, label=label, layout=layout))

    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], key, lazy.group[key].toscreen(toggle=True)),

        # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], key, lazy.window.togroup(key)),
    ])  # fmt: skip
