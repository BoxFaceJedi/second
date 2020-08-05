#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:34:07 2017

@author: sam0225
"""

import time
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z=mc.player.getPos()

a=0

time.sleep(5)

while a<10:
    mc.spawnEntity(x,y,z,33)
    z+=1
    a+=1
    time.sleep(0.01)