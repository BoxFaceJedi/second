  # -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:54:01 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc=Minecraft.create()

def plantTree(x,y,z):
    mc.setBlocks(x+2,y+3,z+2,x-2,y+3,z-2,14)
    mc.setBlocks(x+1,y+4,z,x-1,y+4,z,14)
    mc.setBlocks(x,y+4,z+1,x,y+4,z-1,14)
    mc.setBlocks(x+1,y+5,z,x-1,y+5,z,14)
    mc.setBlocks(x,y+5,z+1,x,y+5,z-1,14)
    mc.setBlocks(x,y,z,x,y+3,z,17)
a,b,c=mc.player.getTilePos()

for i in range(20):
    for j in range(5):
        for k in range(5):
            plantTree(a+i*7,b+i*j,c+i*k)