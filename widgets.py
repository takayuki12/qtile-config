import socket
from libqtile import widget, qtile
import os
import socket
import colors
from custom import battery

colors = colors.get_colors()


sep = widget.Sep(
    linewidth=0,
    # padding=6,
    # foreground=colors[0],
    # background=colors[0]
)

bat = battery.CustomBattery(format='{char} {percent:2.0%} {hour:d}:{min:02d}')
bat.poll()

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())


def get_widget_list():
    return [
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            # background=colors[0]23
        ),
        widget.Image(
            filename="~/Pictures/debian.svg",
            scale="False",
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn("rofi -show drun")}
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            # foreground=colors[2],
            # background=colors[0]
        ),
        widget.GroupBox(
            font="Ubuntu Bold",
            fontsize=9,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            active=colors[2],
            inactive=colors[7],
            rounded=False,
            highlight_color=colors[1],
            highlight_method="line",
            this_current_screen_border=colors[6],
            this_screen_border=colors[4],
            other_current_screen_border=colors[6],
            other_screen_border=colors[4],
            foreground=colors[2],
            # background=colors[0]
        ),
        widget.Prompt(
            prompt=prompt,
            font="Ubuntu Mono",
            padding=10,
            foreground=colors[3],
            background=colors[1]
        ),

        widget.Sep(
            linewidth=0,
            padding=40,
            # foreground=colors[2],
            # background=colors[0]
        ),
        widget.WindowName(
            # foreground=colors[6],
            # background=colors[0],
            foreground='#e5e9f0',
            padding=0
        ),
        widget.Systray(
            background=colors[0],
            padding=5
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            # foreground=colors[0],
            # background=colors[0]
        ),
        bat,
        sep,
        widget.Net(
            interface="wlp2s0",
            # format='{down} ↓↑ {up}',
            format='  {up}',
            foreground=colors[2],
            background=colors[4],
            padding=5
        ),
        sep,
        widget.TextBox(
            text=" 🖬",
            foreground=colors[2],
            background=colors[5],
            padding=0,
            fontsize=14
        ),
        widget.Memory(
            foreground=colors[2],
            background=colors[5],
            #    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm)},
            padding=5
        ),
        sep,
        widget.TextBox(
            text="墳",
            foreground=colors[2],
            background=colors[5],
            padding=10,
            fontsize=25
        ),
        widget.Volume(
            foreground=colors[2],
            background=colors[5],
            padding=5
        ),
        sep,
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser(
                "~/.config/qtile/icons")],
            foreground=colors[0],
            background=colors[4],
            padding=0,
            scale=0.7
        ),
        widget.CurrentLayout(
            foreground=colors[2],
            background=colors[4],
            padding=5
        ),
        sep,
        widget.Clock(
            foreground=colors[2],
            background=colors[5],
            format="%A, %B %d - %H:%M ",
        ),
    ]
