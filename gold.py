#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:34:07 2017

@author: sam0225
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

while True:
    X,Y,Z=mc.player.getTilePos()
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        if x>X:
            mc.spawnEntity(x,y+1,z,33)
            mc.spawnEntity(x+1,y+1,z,33)
            mc.spawnEntity(x+2,y+1,z,33)
            mc.spawnEntity(x+3,y+1,z,33)
            mc.spawnEntity(x+4,y+1,z,33)
            mc.spawnEntity(x+5,y+1,z,33)
            mc.spawnEntity(x+6,y+1,z,33)
            mc.spawnEntity(x+7,y+1,z,33)
            mc.spawnEntity(x+8,y+1,z,33)
            mc.spawnEntity(x+9,y+1,z,33)
            mc.spawnEntity(x+10,y+1,z,33)
        if x<X:
            mc.spawnEntity(x,y+1,z,33)
            mc.spawnEntity(x-1,y+1,z,33)
            mc.spawnEntity(x-2,y+1,z,33)
            mc.spawnEntity(x-3,y+1,z,33)
            mc.spawnEntity(x-4,y+1,z,33)
            mc.spawnEntity(x-5,y+1,z,33)
            mc.spawnEntity(x-6,y+1,z,33)
            mc.spawnEntity(x-7,y+1,z,33)
            mc.spawnEntity(x-8,y+1,z,33)
            mc.spawnEntity(x-9,y+1,z,33)
            mc.spawnEntity(x-10,y+1,z,33)
        if z>Z:
            mc.spawnEntity(x,y+1,z,33)
            mc.spawnEntity(x,y+1,z+1,33)
            mc.spawnEntity(x,y+1,z+2,33)
            mc.spawnEntity(x,y+1,z+3,33)
            mc.spawnEntity(x,y+1,z+4,33)
            mc.spawnEntity(x,y+1,z+5,33)
            mc.spawnEntity(x,y+1,z+6,33)
            mc.spawnEntity(x,y+1,z+7,33)
            mc.spawnEntity(x,y+1,z+8,33)
            mc.spawnEntity(x,y+1,z+9,33)
            mc.spawnEntity(x,y+1,z+10,33)
        if z<Z:
            mc.spawnEntity(x,y+1,z,33)
            mc.spawnEntity(x,y+1,z-1,33)
            mc.spawnEntity(x,y+1,z-2,33)
            mc.spawnEntity(x,y+1,z-3,33)
            mc.spawnEntity(x,y+1,z-4,33)
            mc.spawnEntity(x,y+1,z-5,33)
            mc.spawnEntity(x,y+1,z-6,33)
            mc.spawnEntity(x,y+1,z-7,33)
            mc.spawnEntity(x,y+1,z-8,33)
            mc.spawnEntity(x,y+1,z-9,33)
            mc.spawnEntity(x,y+1,z-10,33)