#!/bin/sh

[[ -f ~/.bashrc ]] && source ~/.bashrc

[[ $(tty) = /dev/tty1 ]] && exec sway
