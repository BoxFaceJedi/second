# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:54:01 2020

@author: SCE
"""


from mcpi.minecraft import Minecraft

mc=Minecraft.create()
while True:
    hits=mc.events.pollProjectileHits()
    if len(hits)>0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        mc.player.setTilePos(x,y,z)