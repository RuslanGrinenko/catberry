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

try:
    logging.info("stop_CATBERRY started")

    epd = epd2in7b.EPD()
    logging.info("init and Clear")
    epd.init()
    #epd.Clear()
    #time.sleep(1)

    logging.info("Cat eyes OFF")
    HBlackimage = Image.open(os.path.join(picdir, 'cat-black-off.bmp'))
    HRedimage = Image.open(os.path.join(picdir, 'cat-red-off.bmp'))
    epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRedimage))

    time.sleep(1)

#    logging.info("Goto Sleep...")
#    epd.sleep()
#    epd.Dev_exit()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in7b.epdconfig.module_exit()
    exit()
