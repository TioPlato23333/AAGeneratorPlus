#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created by orange (@orange23333_)
#
# Copyright (c) 2019 orange. All rights reserved.
#
# This is generator main file. Usage: python main.py [image_name].
# [image_name] is the file name from which you want to generate AA.

import sys

from AAGenerator.generator import *

# you can change the global param setting to get different results
class Param:
  CHARACTER_COLOR = 0
  CHARACTER_SIZE = (10, 5)
  CHARACTER_THICKNESS = 1

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print 'Usage: python main.py [image_name].'
    sys.exit(-1)
  with open(sys.argv[1], 'r') as f:
    generate(f.read(), Param)
