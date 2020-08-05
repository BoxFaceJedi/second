# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:54:01 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()

x,y,z=mc.player.getTilePos()
mc.setBlock(x,y,z-1,5)
mc.setBlock(x-1,y,z,5)
mc.setBlock(x+1,y,z,5)
mc.setBlock(x+1,y,z+1,17)
mc.setBlock(x-1,y,z+1,17)
mc.setBlock(x-1,y,z-1,17)
mc.setBlock(x+1,y,z-1,17)
mc.setBlock(x,y+1,z-1,5)
mc.setBlock(x-1,y+1,z,5)
mc.setBlock(x+1,y+1,z,5)
mc.setBlock(x+1,y+1,z+1,17)
mc.setBlock(x-1,y+1,z+1,17)
mc.setBlock(x-1,y+1,z-1,17)
mc.setBlock(x+1,y+1,z-1,17)
mc.setBlock(x,y+2,z-2,17)
mc.setBlock(x-2,y+2,z,17)
mc.setBlock(x+2,y+2,z,17)
mc.setBlock(x+1,y+2,z+1,17)
mc.setBlock(x-1,y+2,z+1,17)
mc.setBlock(x-1,y+2,z-1,17)
mc.setBlock(x+1,y+2,z-1,17)
mc.setBlock(x,y+2,z,17)
mc.setBlock(x,y+2,z+2,17)
mc.setBlock(x+1,y+3,z,17)
mc.setBlock(x-1,y+3,z,17)
mc.setBlock(x,y+3,z+1,17)
mc.setBlock(x,y+3,z-1,17)
mc.setBlock(x,y+4,z,17)