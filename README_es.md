# Configuración de Qtile Dotfiles

**[English](README.md)** | **[Español](README_es.md)**

Una configuración integral y personalizada del gestor de ventanas Qtile con estética moderna, atajos de teclado enfocados en productividad e integración perfecta con herramientas de desarrollo esenciales.

## 🎯 Descripción General

Esta configuración está basada en el excelente trabajo de [jx11r](https://github.com/jx11r/qtile), mejorada con personalizaciones para flujos de trabajo de desarrollo y experiencia moderna del escritorio Linux. La configuración incluye temas personalizados, atajos de teclado optimizados y aplicaciones cuidadosamente seleccionadas que trabajan armoniosamente juntas.

## ✨ Características

- **Diseños de Barra Personalizados**: Múltiples configuraciones de barra incluyendo el tema Agatha con formas
- **Integración con Rofi**: Hermoso lanzador, menú de energía y menús de aplicaciones
- **Herramientas de Captura**: Flameshot integrado para capturas rápidas de pantalla
- **Terminal**: WezTerm con tema Catppuccin y configuración basada en Lua
- **Enfoque en Productividad**: Optimizado para desarrollo web y flujos de trabajo de programación
- **Compositor**: Picom para animaciones suaves y efectos de transparencia
- **Soporte Multi-tema**: Varias paletas de colores incluyendo variantes de Catppuccin

## 📦 Dependencias

### Requisitos Principales
- **qtile** - El gestor de ventanas en sí
- **qtile-extras** (AUR) - Widgets y funcionalidad adicional
- **python-psutil** - Información del sistema para widgets
- **python-dbus-next** - Integración D-Bus

### Aplicaciones y Herramientas
- **rofi** - Lanzador de aplicaciones y sistema de menús
- **flameshot** - Utilidad de capturas de pantalla
- **wezterm** - Emulador de terminal moderno
- **brightnessctl** (opcional) - Control de brillo
- **pamixer** - Mezclador de PulseAudio para control de volumen
- **playerctl** (opcional) - Control de reproductor multimedia
- **pacman-contrib** - Utilidades de Pacman

### Fuentes
- **otf-hasklig-nerd** - Fuente de programación con ligaduras
- **ttf-nerd-fonts-symbols-mono** - Fuentes de iconos para la barra de estado
- **ttf-cascadia-code-nerd** - Fuente Cascadia Code N con parches de Nerd Font

## 🚀 Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/jerickgm89/DotFilesQtile.git
   cd DotFilesQtile
   ```

2. **Instalar dependencias:**
   ```bash
   # Arch Linux / Manjaro
   sudo pacman -S qtile python-psutil python-dbus-next rofi flameshot wezterm brightnessctl pamixer playerctl pacman-contrib otf-hasklig-nerd ttf-nerd-fonts-symbols-mono
   
   # Instalar qtile-extras desde AUR
   yay -S qtile-extras
   ```

3. **Desplegar configuración:**
   ```bash
   # Hacer respaldo de la configuración existente si está presente
   mv ~/.config/qtile ~/.config/qtile.backup
   
   # Copiar la configuración de qtile
   cp -r qtile ~/.config/
   ```

4. **Establecer permisos de ejecución para scripts:**
   ```bash
   chmod +x ~/.config/qtile/scripts/*
   ```

## 🎨 Personalizaciones

### Cambios Principales del Original

- **Integración con Rofi**: Integración completa con [temas de Rofi de adi1090x](https://github.com/adi1090x/rofi)
- **Distribución de Teclado**: Atajos optimizados para distribución QWERTY (con consideraciones de aprendizaje Dvorak)
- **Configuración de Terminal**: WezTerm con rendimiento basado en Rust y configuración Lua
- **Enfoque en Desarrollo**: Mejorado para desarrollo web con integración de Neovim
- **Consistencia de Tema**: Esquema de colores Catppuccin en todo el entorno de escritorio

### Configuración de Terminal (WezTerm)

WezTerm fue elegido por sus:
- **Rendimiento**: Escrito en Rust para velocidad óptima
- **Configuración**: Sistema de configuración basado en Lua (ideal para usuarios de Neovim)
- **Características**: Aceleración GPU, multiplexación y personalización extensiva
- **Tema**: [Tema Catppuccin](https://github.com/catppuccin/WezTerm) para estética consistente

## 📁 Estructura del Proyecto

```
qtile/
├── config.py              # Configuración principal de Qtile
├── core/                  # Módulos de funcionalidad principal
│   ├── bar/              # Configuraciones de barra de estado
│   ├── groups.py         # Grupos de espacios de trabajo
│   ├── keys.py           # Atajos de teclado
│   ├── layouts.py        # Diseños de ventanas
│   └── screens.py        # Configuraciones de pantalla
├── scripts/              # Scripts de utilidades
├── theme/                # Temas y estilizado
│   └── rofi/            # Configuraciones de tema Rofi
└── utils/                # Utilidades auxiliares y paletas
```

## ⌨️ Atajos de Teclado

### Gestión de Ventanas
| Combinación de Teclas | Acción |
|----------------------|--------|
| `Mod + h/j/k/l` | Mover foco izquierda/abajo/arriba/derecha |
| `Mod + Shift + h/j/k/l` | Mover ventana izquierda/abajo/arriba/derecha |
| `Mod + -` | Reducir ventana |
| `Mod + =` | Agrandar ventana |
| `Mod + m` | Maximizar ventana |
| `Mod + a` | Cerrar ventana |
| `Mod + Espacio` | Alternar flotante |
| `Mod + c` | Centrar ventana flotante |
| `Mod + s` | Traer ventanas flotantes al frente |
| `Mod + Shift + Espacio` | Voltear diseño |
| `F11` | Alternar pantalla completa |

### Diseño y Sistema
| Combinación de Teclas | Acción |
|----------------------|--------|
| `Mod + Tab` | Siguiente diseño |
| `Mod + .` | Cambiar a siguiente pantalla |
| `Mod + Ctrl + b` | Alternar visibilidad de barra |
| `Mod + Ctrl + r` | Recargar configuración |
| `Mod + Ctrl + s` | Cerrar Qtile |

### Aplicaciones
| Combinación de Teclas | Acción |
|----------------------|--------|
| `Mod + Return` | Abrir terminal |
| `Mod + Shift + Return` | Abrir terminal secundario |
| `Mod + r` | Lanzador de aplicaciones (Tipo 2) |
| `Mod + Shift + r` | Lanzador de aplicaciones (Tipo 1) |
| `Mod + b` | Abrir navegador web |
| `Mod + Shift + e` | Abrir gestor de archivos (Ranger) |
| `Print` | Herramienta de captura (Flameshot) |
| `Mod + Ctrl + Escape` | Menú de energía |

### Controles de Media y Sistema
| Combinación de Teclas | Acción |
|----------------------|--------|
| `XF86AudioMute` | Alternar silencio de audio |
| `XF86AudioLowerVolume` | Disminuir volumen |
| `XF86AudioRaiseVolume` | Aumentar volumen |
| `XF86AudioPlay` | Reproducir/pausar media |
| `XF86AudioPrev` | Pista anterior |
| `XF86AudioNext` | Siguiente pista |
| `Mod + XF86AudioLowerVolume` | Disminuir brillo de pantalla |
| `Mod + XF86AudioRaiseVolume` | Aumentar brillo de pantalla |

> **Nota**: La tecla `Mod` típicamente es la tecla Windows/Super

## 🔧 Configuración

La configuración es modular y fácilmente personalizable:

- **Atajos de Teclado**: Modifica `core/keys.py` para atajos personalizados
- **Temas**: Ajusta paletas de colores en `utils/palette*.py`
- **Diseño de Barra**: Personaliza la barra de estado en `core/bar/`
- **Aplicaciones**: Actualiza inicio automático en `scripts/autostart.sh`

## 🙏 Reconocimientos

- **[jx11r](https://github.com/jx11r/qtile)** - Base de configuración original de Qtile
- **[adi1090x](https://github.com/adi1090x/rofi)** - Hermosos temas de Rofi
- **[Catppuccin](https://github.com/catppuccin)** - Paleta de colores consistente en aplicaciones

## 📄 Licencia

Esta configuración está disponible bajo la misma licencia que el trabajo original. Consulta el archivo LICENSE para más detalles.

---

> **Nota**: Esta configuración está en evolución continua. Siéntete libre de adaptarla a tus necesidades específicas y preferencias de flujo de trabajo.