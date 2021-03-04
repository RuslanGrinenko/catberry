#!/usr/bin/python3.7
# -*- coding:utf-8 -*-

import sys
import os
picdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pic')
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in7b
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG, filename="/var/log/catberry.log")

import vlc
from gpiozero import Button

runFlag = True
music = vlc.MediaPlayer("file:///home/pi/catberry/sound/hbsong.mp3")

def handleBtnStartPress():
    global music
    logging.info("Play pressed")
    music.play()

def handleBtnPausePress():
    global music
    logging.info("Pause pressed")
    music.pause()


def handleBtnStopPress():
    global music
    logging.info("Stop pressed")
    music.stop()

def handleBtnTurnOffPress():
    global music
    global runFlag
    logging.info("TurnOff pressed")
    music.stop()
    #runFlag = False
    #os.system("/home/pi/catberry/stop_catberry.py")
    os.system("shutdown -P now")

btnStart = Button(5)
btnPause = Button(6)
btnStop = Button(13)
btnTurnOff = Button(19)

btnStart.when_pressed = handleBtnStartPress
btnPause.when_pressed = handleBtnPausePress
btnStop.when_pressed = handleBtnStopPress
btnTurnOff.when_pressed = handleBtnTurnOffPress


try:
    logging.info("start_CATBERRY start")

    epd = epd2in7b.EPD()
    logging.info("init and Clear")
    epd.init()
    #epd.Clear()
    #time.sleep(1)

    logging.info("Cat eyes ON")
    HBlackimage = Image.open(os.path.join(picdir, 'cat-black-on.bmp'))
    HRedimage = Image.open(os.path.join(picdir, 'cat-red-on.bmp'))
    epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRedimage))

    time.sleep(3)

#    logging.info("Goto Sleep...")
#    epd.sleep()
#    epd.Dev_exit()


except IOError as e:
    logging.info(e)

except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in7b.epdconfig.module_exit()
    exit()

music.play()
while runFlag:
    continue
