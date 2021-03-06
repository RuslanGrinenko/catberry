#!/usr/bin/python3.7
# -*- coding:utf-8 -*-

NOOLITE_API_URL = "http://192.168.8.200/api.htm"
PARAMS_ARRAY = [{'ch':3,'cmd':4},{'ch':3,'cmd':4},{'ch':3,'cmd':4},{'ch':3,'cmd':4},{'ch':3,'cmd':2},{'ch':4,'cmd':4},{'ch':4,'cmd':4},{'ch':4,'cmd':4},{'ch':4,'cmd':4},{'ch':4,'cmd':2},{'ch':3,'cmd':0},{'ch':4,'cmd':0}]

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

import requests

import vlc
from gpiozero import Button

runFlag = True
music = vlc.MediaPlayer("file:///home/pi/catberry/sound/hbsong.mp4")
playInitiated = False



def handleBtnStartPress():
    global music
    global epd
    global playInitiated
    logging.info("Play pressed")
    if not playInitiated:
      try:
        logging.info("Cake to screen")
        HBlackimage = Image.open(os.path.join(picdir, 'cake-black.bmp'))
        HRedimage = Image.open(os.path.join(picdir, 'cake-red.bmp'))
        epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRedimage))
        playInitiated = True

      except IOError as e:
        logging.info(e)

      except KeyboardInterrupt:    
        logging.info("ctrl + c:")
        epd2in7b.epdconfig.module_exit()
        exit()

    music.play()

def handleBtnPausePress():
    global music
    logging.info("Pause pressed")
    music.pause()


def handleBtnStopPress():
    global music
    global epd
    global playInitiated
    logging.info("Stop pressed")
    music.stop()
    if playInitiated:
       logging.info("Back to Cat eyes ON screen")
       HBlackimage = Image.open(os.path.join(picdir, 'cat-black-on.bmp'))
       HRedimage = Image.open(os.path.join(picdir, 'cat-red-on.bmp'))
       epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRedimage))
       playInitiated = False
 
    
def handleBtnTurnOffPress():
    global music
    global runFlag
    logging.info("TurnOff pressed")
    music.stop()
    #runFlag = False 
    os.system("shutdown -P now")

btnStart = Button(5)
btnPause = Button(6)
btnStop = Button(13)
btnTurnOff = Button(19)

btnStart.when_pressed = handleBtnStartPress
btnPause.when_pressed = handleBtnPausePress
btnStop.when_pressed = handleBtnStopPress
btnTurnOff.when_pressed = handleBtnTurnOffPress

while True:
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

#    time.sleep(3)

#    logging.info("Goto Sleep...")
#    epd.sleep()
#    epd.Dev_exit()


  except IOError as e:
      logging.info(e)

  except KeyboardInterrupt:    
      logging.info("ctrl + c:")
      epd2in7b.epdconfig.module_exit()
      exit()

  Ended = 6
  currentState = music.get_state()

  while runFlag and (currentState != Ended):
      #print(currentState)
      currentState = music.get_state()
      continue
  
  for params in PARAMS_ARRAY:
      r = requests.get(url = NOOLITE_API_URL, params = params)
      time.sleep(0.3)
  
  music.stop()