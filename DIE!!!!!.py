# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:54:01 2020

@author: SCE
"""
import time
import random
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

time.sleep(5)

x,y,z=mc.player.getTilePos()
c=random.randrange(8)
mc.setBlock(x,y,z,38,c)
time.sleep(1)
x,y,z=mc.player.getTilePos()
c=random.randrange(8)
mc.setBlock(x,y,z,38,c)
time.sleep(1)
x,y,z=mc.player.getTilePos()
c=random.randrange(8)
mc.setBlock(x,y,z,38,c)
time.sleep(1)
x,y,z=mc.player.getTilePos()
c=random.randrange(8)
mc.setBlock(x,y,z,38,c)
time.sleep(1)
x,y,z=mc.player.getTilePos()
c=random.randrange(8)
mc.setBlock(x,y,z,38,c)
time.sleep(1)
x,y,z=mc.player.getTilePos()
c=random.randrange(8)
mc.setBlock(x,y,z,38,c)
time.sleep(1)
x,y,z=mc.player.getTilePos()
c=random.randrange(8)
mc.setBlock(x,y,z,38,c)
time.sleep(1)
x,y,z=mc.player.getTilePos()
c=random.randrange(8)
mc.setBlock(x,y,z,38,c)
time.sleep(1)