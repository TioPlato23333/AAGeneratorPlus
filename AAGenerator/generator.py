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

def generate(string, param):
  character = 255 * np.ones(param.CHARACTER_SIZE, dtype='uint8')
  cv2.putText(character, '}', (0, param.CHARACTER_SIZE[0]), \
    cv2.FONT_HERSHEY_SIMPLEX, 0.5, param.CHARACTER_COLOR)
  print character
  cv2.imshow('sample', character)
  cv2.waitKey()
