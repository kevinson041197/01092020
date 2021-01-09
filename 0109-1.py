import random
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
#前後左右
for i in range(1,21):
    r=random.randrange(1,5)
    if r == 1:#前
        mc.setBlocks(x,y,z,x,y,z+4,46)
        z=z+4
    if r ==2:#後
        mc.setBlocks(x,y,z,x,y,z-4,46)
        z=z-4
    if r ==3:#右
        mc.setBlocks(x,y,z,x-4,y,z,46)
        x=x-4
    if r ==4:#右
        mc.setBlocks(x,y,z,x+4,y,z,46)
        x=x+4