# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:54:01 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()

while True:

    x,y,z=mc.player.getTilePos()
    
    a=mc.getBlock(x+1,y-1,z)
    b=mc.getBlock(x-1,y-1,z)
    c=mc.getBlock(x,y-1,z+1)
    d=mc.getBlock(x,y-1,z-1)
    
    if a==2 or b==2 or c==2 or d==2:
        mc.setBlock(x,y-1,z,5)