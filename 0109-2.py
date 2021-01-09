from mcpi.minecraft import Minecraft
mc=Minecraft.create()
mc.executeCommand("time set 1000")
import time
while True:
    mc.executeCommand("time add 50")
    time.sleep(0.05)
    