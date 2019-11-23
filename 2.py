from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import mcpi.block as block
import time

mc.player.setPos(59,97,800)

x = 57
y = 96
z = 777
sizx = 50
sizy = 6
sizz = 25
        
mc.setBlocks(x,y,z,x+sizx,y+sizy,z+sizz,7)
mc.setBlocks(58,97,778,106,102,801,0)
mc.setBlocks(58,97,797,106,102,797,3)
mc.setBlocks(68,97,797,70,102,797,0)
mc.setBlocks(76,97,797,78,102,797,0)
mc.setBlocks(67,97,797,67,102,778,3)
mc.setBlocks(67,97,779,67,102,778,0)
mc.setBlocks(67,97,788,67,102,787,0)
mc.setBlocks(71,97,789,103,102,789,3)
mc.setBlocks(103,97,778,103,102,797,3)
mc.setBlocks(71,97,781,103,102,781,3)
mc.setBlocks(71,97,797,71,102,781,3)
mc.setBlocks(97,97,781,94,102,781,0)
mc.setBlocks(103,97,791,103,102,790,0)
mc.setBlocks(67,97,789,59,102,789,3)
mc.setBlocks(67,97,786,58,102,786,3)
mc.setBlocks(67,97,780,59,102,780,3)
mc.setBlocks(59,97,780,59,102,784,3)
mc.setBlocks(59,97,784,65,102,784,3)
mc.setBlocks(59,97,789,59,102,795,3)
mc.setBlocks(59,97,795,64,102,795,3)
mc.setBlocks(64,97,795,64,102,791,3)
mc.setBlocks(76,97,797,78,102,797,0)
mc.setBlocks(75,97,797,75,102,792,3)
mc.setBlocks(98,97,781,98,102,787,3)
mc.setBlocks(79,97,797,79,102,792,3)
mc.setBlocks(79,97,792,84,102,792,3)
mc.setBlocks(84,97,792,84,102,795,3)
mc.setBlocks(84,97,795,81,102,795,3)
mc.setBlocks(86,97,797,86,102,792,3)
mc.setBlocks(86,97,792,93,102,792,3)
mc.setBlocks(93,97,792,93,102,795,3)
mc.setBlocks(93,97,795,88,102,795,3)
mc.setBlocks(95,97,797,95,102,792,3)
mc.setBlocks(95,97,792,100,102,792,3)
mc.setBlocks(100,97,792,100,102,795,3)
mc.setBlocks(100,97,795,97,102,795,3)
mc.setBlocks(104,96,782,106,96,782,41)
mc.setBlocks(57,103,802,107,103,777,7)

x1=85
y1=97
z1=793

x2=99
y2=97
z2=796

x3=104
y3=97
z3=782

x4=105
y4=97
z4=782

x5=106
y5=97
z5=782

while True:
    pos=mc.player.getTilePos()
    if pos.x==x1 and pos.y==y1 and pos.z==z1:
        mc.player.setPos(59,97,800)
        mc.postToChat("teleport to start")
    pos=mc.player.getTilePos()
    if pos.x==x2 and pos.y==y2 and pos.z==z2:
        mc.player.setPos(59,97,800)
        mc.postToChat("teleport to start")
    if pos.x==x3 and pos.y==y3 and pos.z==z3:
        mc.postToChat("FINISH!!!")
        mc.setBlocks(x,y,z,x+sizx,y+sizy,z+sizz,41)
        mc.setBlocks(58,97,778,106,102,801,0)
        mc.setBlocks(58,97,797,106,102,797,41)
        mc.setBlocks(67,97,797,67,102,778,41)
        mc.setBlocks(71,97,789,103,102,789,41)
        mc.setBlocks(103,97,778,103,102,797,41)
        mc.setBlocks(71,97,781,103,102,781,41)
        mc.setBlocks(71,97,797,71,102,781,41)
        mc.setBlocks(67,97,789,59,102,789,41)
        mc.setBlocks(67,97,786,58,102,786,41)
        mc.setBlocks(67,97,780,59,102,780,41)
        mc.setBlocks(59,97,780,59,102,784,41)
        mc.setBlocks(59,97,784,65,102,784,41)
        mc.setBlocks(59,97,789,59,102,795,41)
        mc.setBlocks(59,97,795,64,102,795,41)
        mc.setBlocks(64,97,795,64,102,791,41)
        mc.setBlocks(75,97,797,75,102,792,41)
        mc.setBlocks(98,97,781,98,102,787,41)
        mc.setBlocks(79,97,797,79,102,792,41)
        mc.setBlocks(79,97,792,84,102,792,41)
        mc.setBlocks(84,97,792,84,102,795,41)
        mc.setBlocks(84,97,795,81,102,795,41)
        mc.setBlocks(86,97,797,86,102,792,41)
        mc.setBlocks(86,97,792,93,102,792,41)
        mc.setBlocks(93,97,792,93,102,795,41)
        mc.setBlocks(93,97,795,88,102,795,41)
        mc.setBlocks(95,97,797,95,102,792,41)
        mc.setBlocks(95,97,792,100,102,792,41)
        mc.setBlocks(100,97,792,100,102,795,41)
        mc.setBlocks(100,97,795,97,102,795,41)


    if pos.x==x4 and pos.y==y4 and pos.z==z4:
        mc.postToChat("FINISH!!!")
        mc.setBlocks(x,y,z,x+sizx,y+sizy,z+sizz,41)
        mc.setBlocks(58,97,778,106,102,801,0)
        mc.setBlocks(58,97,797,106,102,797,41)
        mc.setBlocks(67,97,797,67,102,778,41)
        mc.setBlocks(71,97,789,103,102,789,41)
        mc.setBlocks(103,97,778,103,102,797,41)
        mc.setBlocks(71,97,781,103,102,781,41)
        mc.setBlocks(71,97,797,71,102,781,41)
        mc.setBlocks(67,97,789,59,102,789,41)
        mc.setBlocks(67,97,786,58,102,786,41)
        mc.setBlocks(67,97,780,59,102,780,41)
        mc.setBlocks(59,97,780,59,102,784,41)
        mc.setBlocks(59,97,784,65,102,784,41)
        mc.setBlocks(59,97,789,59,102,795,41)
        mc.setBlocks(59,97,795,64,102,795,41)
        mc.setBlocks(64,97,795,64,102,791,41)
        mc.setBlocks(75,97,797,75,102,792,41)
        mc.setBlocks(98,97,781,98,102,787,41)
        mc.setBlocks(79,97,797,79,102,792,41)
        mc.setBlocks(79,97,792,84,102,792,41)
        mc.setBlocks(84,97,792,84,102,795,41)
        mc.setBlocks(84,97,795,81,102,795,41)
        mc.setBlocks(86,97,797,86,102,792,41)
        mc.setBlocks(86,97,792,93,102,792,41)
        mc.setBlocks(93,97,792,93,102,795,41)
        mc.setBlocks(93,97,795,88,102,795,41)
        mc.setBlocks(95,97,797,95,102,792,41)
        mc.setBlocks(95,97,792,100,102,792,41)
        mc.setBlocks(100,97,792,100,102,795,41)
        mc.setBlocks(100,97,795,97,102,795,41)
    if pos.x==x5 and pos.y==y5 and pos.z==z5:
        mc.postToChat("FINISH!!!")
        mc.setBlocks(x,y,z,x+sizx,y+sizy,z+sizz,41)
        mc.setBlocks(58,97,778,106,102,801,0)
        mc.setBlocks(58,97,797,106,102,797,41)
        mc.setBlocks(67,97,797,67,102,778,41)
        mc.setBlocks(71,97,789,103,102,789,41)
        mc.setBlocks(103,97,778,103,102,797,41)
        mc.setBlocks(71,97,781,103,102,781,41)
        mc.setBlocks(71,97,797,71,102,781,41)
        mc.setBlocks(67,97,789,59,102,789,41)
        mc.setBlocks(67,97,786,58,102,786,41)
        mc.setBlocks(67,97,780,59,102,780,41)
        mc.setBlocks(59,97,780,59,102,784,41)
        mc.setBlocks(59,97,784,65,102,784,41)
        mc.setBlocks(59,97,789,59,102,795,41)
        mc.setBlocks(59,97,795,64,102,795,41)
        mc.setBlocks(64,97,795,64,102,791,41)
        mc.setBlocks(75,97,797,75,102,792,41)
        mc.setBlocks(98,97,781,98,102,787,41)
        mc.setBlocks(79,97,797,79,102,792,41)
        mc.setBlocks(79,97,792,84,102,792,41)
        mc.setBlocks(84,97,792,84,102,795,41)
        mc.setBlocks(84,97,795,81,102,795,41)
        mc.setBlocks(86,97,797,86,102,792,41)
        mc.setBlocks(86,97,792,93,102,792,41)
        mc.setBlocks(93,97,792,93,102,795,41)
        mc.setBlocks(93,97,795,88,102,795,41)
        mc.setBlocks(95,97,797,95,102,792,41)
        mc.setBlocks(95,97,792,100,102,792,41)
        mc.setBlocks(100,97,792,100,102,795,41)
        mc.setBlocks(100,97,795,97,102,795,41)
