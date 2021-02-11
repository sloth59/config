# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os, subprocess

home = os.path.expanduser('~')
@hook.subscribe.startup_once
def autostart():
    subprocess.call([home + '/.config/qtile/autostart.sh'])


mod = "mod4"
terminal = guess_terminal()

keys = [
    Key([mod], "h",
        lazy.layout.left()),
    
    Key([mod], "j",
        lazy.layout.down()),
    
    Key([mod], "k",
        lazy.layout.up()),
    
    Key([mod], "l",
        lazy.layout.right()),

    
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down()),
    
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up()),

    
    Key([mod], "t",
        lazy.window.toggle_floating()),
    
    Key([mod], "f",
        lazy.window.toggle_fullscreen()),

    
    Key([mod], "space",
        lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    Key([mod], "Return",
        lazy.spawn(terminal),
        desc="Launch terminal"),

    Key([mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"),

    Key([mod], "w",
        lazy.window.kill(),
        desc="Kill focused window"),

    Key([mod, "control"], "r",
        lazy.restart(),
        desc="Restart qtile"),

    Key([mod, "control"], "q",
        lazy.shutdown(),
        desc="Shutdown qtile"),

    Key([mod], "r", # lazy.spawncmd(),
        lazy.spawn("rofi -show drun"),
        desc="Spawn a command using a prompt widget"),


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
        lazy.spawn("scrot "+home+"/Pictures/'shot_%Y_%m_%d_%H_%M_%S.png'"),
        lazy.spawn("notify-send SCREEN_SHOT")),


    ## MONAD LAYOUT
    Key([mod, "shift"], "space",
        lazy.layout.flip()),
    
    Key([mod], "i",
        lazy.layout.grow()),
    
    Key([mod], "d",
        lazy.layout.shrink()),
    
    Key([mod], "m",
        lazy.layout.maximize()),
    
    Key([mod], "n",
        lazy.layout.normalize()),

    
    ## TILE LAYOUT
    Key([mod, "shift"], "h",
        lazy.layout.decrease_ratio()),
    
    Key([mod, "shift"], "l",
        lazy.layout.increase_ratio()),
    
    Key([mod], "equal",
        lazy.layout.increase_nmaster()),
    
    Key([mod], "minus",
        lazy.layout.decrease_nmaster()),
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


kwargs = {
    "margin": 5
}

layouts = [
    layout.Tile(shift_windows=True,
                ratio=0.51,
                **kwargs),
    layout.MonadWide(**kwargs),
    layout.Max(),
    # layout.MonadTall(),
    # layout.Stack(),
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    # layout.RatioTile(),
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
                widget.Clipboard(
                    fmt='  {} ',
                ),
                widget.Cmus(),
                widget.Systray(),
                widget.CapsNumLockIndicator(),
                widget.Volume(
                    fmt='   {} ',
                ),
                #widget.Wlan(       # requires iwlib
                #    interface='wlp4s0',
                #    format='{essid}',
                #    fmt='   {} ',
                #),
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
                #widget.Wallpaper(
                #    directory='/usr/share/backgrounds/',
                #    random_selection=True,
                #    fmt='   ',
                #),
                widget.QuickExit(
                    countdown_start=1,
                    fmt='   ',
                ),

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
bring_front_click = False
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
