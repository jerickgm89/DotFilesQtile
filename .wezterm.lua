-- Pull in the wezterm API
local wezterm = require("wezterm")

-- This Weill hold the configuration
local config = {}

config.color_scheme = "Catppuccin Mocha"
config.font = wezterm.font("Cascadia Code NF", {
	weight = "Regular",
	italic = false,
})
config.font_size = 14.0
config.enable_tab_bar = false
config.use_fancy_tab_bar = false
config.font_shaper = "Harfbuzz"
config.warn_about_missing_glyphs = false

return config
