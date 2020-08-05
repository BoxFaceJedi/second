  # -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:54:01 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc=Minecraft.create()

x,y,z=mc.player.getTilePos()
mc.setBlocks(x+2,y+3,z+2,x-2,y+3,z-2,14)
mc.setBlocks(x+1,y+4,z,x-1,y+4,z,14)
mc.setBlocks(x,y+4,z+1,x,y+4,z-1,14)
mc.setBlocks(x+1,y+5,z,x-1,y+5,z,14)
mc.setBlocks(x,y+5,z+1,x,y+5,z-1,14)
mc.setBlocks(x,y,z,x,y+3,z,17)