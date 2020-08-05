# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:54:01 2020

@author: SCE
"""
import time
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()

whdith=2.5
height=6
length=2.5

mc.setBlocks(x+whdith,y+height,z+length,x-whdith,y,z-length,5)
time.sleep(0.5)
mc.setBlocks(x+whdith-1,y+height-1,z+length-1,x-whdith-1,y-1,z-length-1,0)
time.sleep(0.5)
mc.setBlocks(x+2,y+height,z+2,x-2,y+height,z-2,17)
time.sleep(0.5)