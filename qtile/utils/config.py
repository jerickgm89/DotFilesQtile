import json
from dataclasses import asdict, dataclass, field
from os import environ, getcwd
from os.path import exists, expanduser, join
from libqtile.lazy import lazy
from typing import Optional


@dataclass
class Config:
    bar: str = "shapes"
    bar2: str = "shapes"
    browser: str = "microsoft-edge-stable"
    flameshot: str = "flameshot gui"
    term: str | None = "wezterm"
    term2: str = ""
    wallpaper: str = "~/Pictures/montanas.jpg"

    @property
    def is_xephyr(self):
        return int(environ.get("QTILE_XEPHYR", 0)) > 0

    @staticmethod
    def path() -> str:
        xdg = expanduser("~/.config/qtile")
        return xdg if exists(xdg) else getcwd()

    @classmethod
    def load(cls) -> "Config":
        file = join(cls.path(), "cfg.json")
        if not exists(file):
            cls.generate(file)
            return cls()
        with open(file, "r") as f:
            content = json.load(f)
            return cls(**content)

    @classmethod
    def generate(cls, file: str):
        with open(file, "w") as f:
            content = asdict(cls())
            f.write(json.dumps(content, indent=2))

cfg = Config.load()
