# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:54:01 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()

mc.setBlocks(x+10,y-1,z,x-10,y-10,z,35)
mc.setBlocks(x,y-1,z+10,x,y-10,z-10,35)
mc.setBlocks(x-10,y-1,z,x+10,y-10,z,35)
mc.setBlocks(x,y-1,z-10,x,y-10,z+10,35)