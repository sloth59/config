#!/bin/sh

alias ls="ls --color=auto"
PS1="\[\e[32m\]\u\[\e[00m\]@\h \[\e[32m\]\w \[\e[00m\]> "
export PS1
