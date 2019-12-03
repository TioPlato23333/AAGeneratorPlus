#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created by orange (@orange23333_)
#
# Copyright (c) 2019 orange. All rights reserved.
#
# This is AA image generator file. Create an image from AA string
# (a vector of UTF-8 characters) and a given character size.

import cv2
import numpy as np
import os
from PIL import Image, ImageDraw, ImageFont

def generate(string, param):
  # character = 255 * np.ones(param.CHARACTER_SIZE, dtype='uint8')
  # cv2.putText(character, '}', (0, param.CHARACTER_SIZE[0]), \
  #   cv2.FONT_HERSHEY_SIMPLEX, 0.5, param.CHARACTER_COLOR)
  # print character
  # cv2.imshow('sample', character)
  # cv2.waitKey()
  # get an image
  current_path, _ = os.path.split(os.path.abspath(__file__))
  base = Image.open(os.path.join(current_path, '../test_asset/fate_astolfo.jpg')).convert('RGBA')

  # make a blank image for the text, initialized to transparent text color
  txt = Image.new('RGBA', base.size, (255,255,255,0))

  # get a font
  fnt = ImageFont.truetype(os.path.join('../resources/SFNSText.ttf'), 100)
  # get a drawing context
  d = ImageDraw.Draw(txt)

  # draw text, half opacity
  d.text((10,10), "Hello", font=fnt, fill=(0,255,255,128))
  # draw text, full opacity
  d.text((10,160), "World", font=fnt, fill=(0,255,255,255))

  out = Image.alpha_composite(base, txt)

  out.show()
