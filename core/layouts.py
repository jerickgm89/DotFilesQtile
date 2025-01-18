from libqtile import layout

from utils.match import title, wm_class
from utils.palette import palette

config = {
    "border_focus": palette.sapphire,
    "border_normal": palette.base,
    "border_width": 0,
    "margin": 10,
    "single_border_width": 2,
    "single_margin": 10,
}

configTreeTab = {
    "active_bg": palette.crust,
    "active_fg": palette.mauve,
    "bg_color": palette.base,
    "border_width": 0,
    "font": "SF Pro Rounded",
    "fontsize": 14,
    "inactive_bg": palette.base,
    "inactive_fg": palette.subtext1,
    "level_shift": 0,
    "margin_left": 0,
    "margin_y": 10,
    "padding_left": 10,
    "padding_x": 10,
    "padding_y": 10,
    "panel_width": 200,
    "section_bottom": 8,
    "section_fg": palette.red,
    "section_fontsize": 16,
    "section_left": 8,
    "section_padding": 8,
    "section_top": 8,
    "sections": ["JErickDev"],
    "urgent_bg": palette.red,
    "urgent_fg": palette.text,
}

layouts = [
    layout.MonadTall(
        **config,
        change_ratio=0.02,
        min_ratio=0.30,
        max_ratio=0.70,
    ),
    layout.Max(**config),
    layout.MonadWide(**config),
    layout.Matrix(**config),
    layout.MonadThreeCol(**config),
]

floating_layout = layout.Floating(
    border_focus=palette.subtext1,
    border_normal=palette.base,
    border_width=0,
    fullscreen_border_width=0,
    float_rules=[
        *layout.Floating.default_float_rules,
        *wm_class(
            "confirmreset",
            "Display",
            "floating",
            "flameshot",
            "gpicview",
            "lxappearance",
            # "makebranch",
            # "maketag",
            "pavucontrol",
            "pinentry-gtk-2",
            # "psterm",
            "qt5ct",
            "ssh-askpass",
            "steam",
            "thunar",
            "Thunar",
            # "Xephyr",
            "xfce4-about",
        ),
        *title(
            "branchdialog",
            "minecraft-launcher",
            "pinentry",
        ),
    ],
)
