from mcpi.minecraft import Minecraft
mc=Minecraft.create()
string="我在外層"
def func():
    string="我在內層"
    
func()    
#1 7 3 4 5