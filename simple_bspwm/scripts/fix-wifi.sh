#!/bin/sh
cd ~/mt7601/src
make clean
make
sudo make install
sudo modprobe mt7601Usta