# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:54:01 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()

mc.postToChat('I see you =>')

while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat('you are located one X:'+str(x)+',Y:'+str(y)+',Z:'+str(z))
    time.sleep(0.5)