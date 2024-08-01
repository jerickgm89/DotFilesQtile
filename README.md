# Qtile

![Qtile](/assets/QtileJErickDev.png)

Esta configuración es un fork del repositorio perteneciente al usuario `jx11r`, realmente ha hecho un excelente trabajo aquí te comparto el link:

[Config de jx11r - Qtile](https://github.com/jx11r/qtile)

Solamente lo he personalizado a mi gusto personal aquí te dejo las dependencias necesarias para de usar esta configuración:

## Dependencias

- brightnessctl (optional)
- otf-hasklig-nerd
- pacman-contrib
- pamixer
- playerctl (optional)
- python-dbus-next
- python-psutil
- qtile-extras (AUR)
- qtile
- ttf-nerd-fonts-symbols-mono
- rofi
- flameshot
- Wezterm

## Que es lo que cambio?

Primero le agregue la configuración de Rofi para el launcher y powermenu el usuario `adi1090x` también realizo un excelente trabajo... te dejo link:

[Rofi Config](https://github.com/adi1090x/rofi)

y lo demás son solo cambio de algunos shorcuts para el layout QWERYT (Ando aprendiendo Dvorak 🥲), [flameshot](https://github.com/flameshot-org), [Wezterm](https://wezfurlong.org/wezterm/index.html) (Terminal) con el Shell Zsh, en lo posible explicare cada configuración de cada dependencia.

### Wezterm

La terminal que estoy usando en este momento, el motivo principal es que esta realizado en rust y para configurarlo se usa lua como lenguaje, este ultimo me es muy importante ya que utilizo [neovim](https://neovim.io/) para el desarrollo de mis aplicaciones web.

El tema uso [Catppuccin](https://github.com/catppuccin/WezTerm), me parece muy agradable los colores
