
from typing import List  # noqa: F401
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
import subprocess

@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])

mod = "mod4"
terminal = guess_terminal()

keys = [
    Key([mod], "space",
        lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    Key([mod, "shift"], "space",
        lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    Key([mod, "shift"], "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    Key([mod], "Return", lazy.spawn(terminal),),
    Key([mod], "Tab", lazy.next_layout(),),
    Key([mod], "w", lazy.window.kill(),),
    Key([mod, "control"], "r", lazy.restart(),),
    Key([mod, "control"], "q", lazy.shutdown(),),
    Key([mod], "r", lazy.spawncmd(),),

    Key([mod], "f", lazy.window.toggle_fullscreen(),),
    Key([mod], "t", lazy.window.toggle_floating(),),

    Key([mod], "h", lazy.layout.left()),
    Key([mod], "j", lazy.layout.down(),),
    Key([mod], "l", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up(),),
    Key([mod, "control"], "h", lazy.layout.shuffle_left()),
    Key([mod, "control"], "j", lazy.layout.shuffle_down(),),
    Key([mod, "control"], "k", lazy.layout.shuffle_up(),),
    Key([mod, "control"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "h", lazy.layout.grow_left()),
    Key([mod, "shift"], "j", lazy.layout.grow_down()),
    Key([mod, "shift"], "k", lazy.layout.grow_up()),
    Key([mod, "shift"], "l", lazy.layout.grow_right()),

    Key([], "XF86AudioMute",
        lazy.spawn("amixer -q set Master toggle")),

    Key([], "XF86AudioLowerVolume",
        lazy.spawn("amixer -c 0 sset Master 1- unmute")),

    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("amixer -c 0 sset Master 1+ unmute")),

    Key([], "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl s +5%")),

    Key([], "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl s 5%-")),

    Key([], "Print",
        lazy.spawn("scrot /home/sloth/screenshot/'shot_%Y_%m_%d_%H_%M_%S.png'"),
        lazy.spawn("notify-send SCREEN_SHOT")),

]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        Key([mod], i.name,
            lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        Key([mod, "shift"], i.name,
            lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),

    ])

layouts = [
    layout.Max(),
    layout.Stack(
        num_stacks=2,
        autosplit=True,
        margin=5,
    ),
    # Try more layouts by unleashing below layouts.
    layout.Bsp(
        margin=5,
        fair=False,
    ),
    # layout.Columns(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='sans',
    fontsize=15,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayoutIcon(),
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Systray(),
                widget.Cmus(),
                widget.Clipboard(
                    fmt='  {} ',
                ),
                widget.CapsNumLockIndicator(),
                widget.Volume(
                    fmt='   {} ',
                ),
                widget.Wlan(
                    interface='wlp4s0',
                    format='{essid}',
                    fmt='   {} ',
                ),
                widget.Battery(
                    charge_char=' ',
                    discharge_char='',
                    format='{char}{percent:2.0%}',
                    fmt='   {} ',
                ),
                widget.ThermalSensor(
                    fmt='  {} ',
                    update_interval=10,
                ),
                widget.Clock(
                    format='%a %I:%M %p  ',
                    fmt='   {} ',
                    update_interval=10,
                ),
                widget.Wallpaper(
                    directory='/usr/share/backgrounds/archlinux/',
                    random_selection=True,
                    fmt='   ',
                ),
                widget.QuickExit(
                    countdown_start=1,
                    fmt='   ',
                ),
                #widget.Notify(),
            ],
            30,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1",
         lazy.window.set_position_floating(),
         start=lazy.window.get_position()),

    Drag([mod], "Button3",
         lazy.window.set_size_floating(),
         start=lazy.window.get_size()),

    Click([mod], "Button2",
          lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"


wmname = "LG3D"