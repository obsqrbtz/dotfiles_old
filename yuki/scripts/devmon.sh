#!/bin/sh
devmon --no-gui --exec-on-drive "notify-send --icon=block-device --urgency=low \"Volume %l has been mounted\"" --exec-on-remove "notify-send --icon=block-device --urgency=low \"Volume %l has been removed\""