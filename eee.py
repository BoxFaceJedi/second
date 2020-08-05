# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:54:01 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import time
x,y,z=mc.player.getTilePos()

try:
    block=int(input('要放啥'))
    mc.setBlock(x,y,z,block)
except:
    mc.postToChat('error error')
    time.sleep(0.3)
    mc.postToChat('error')
    mc.postToChat('eeEeeEeRrooOrRrr')
    mc.postToChat("Gaster joined the game")
    mc.postToChat('Gaster:I seee you =>')