# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:54:01 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()

time.sleep(5)

x,y,z=mc.player.getTilePos()

mc.player.setTilePos(x,y,z)
x+=10
time.sleep(0.5)
