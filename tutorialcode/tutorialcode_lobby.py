import math

def drawPlayer(x, y):
    print("drawentity player1", str(x), str(y))

def drawCrystalbat(x, y):
    print("drawentity crystalbat", str(x), str(y))

def drawCrystalgolem(x, y):
    print("drawentity crystalgolem", str(x), str(y))

def drawCrystalknight(x, y):
    print("drawentity crystalknight", str(x), str(y))

def drawCrystalscorpion(x, y):
    print("drawentity crystalscorpion", str(x), str(y))

def drawCrystalslime(x, y):
    print("drawentity crystalslime", str(x), str(y))
    
def drawBronzeChest(x, y):
    print("drawentity bronze", str(x), str(y))
    
def drawSilverChest(x, y):
    print("drawentity silver", str(x), str(y))

def drawApple(x, y):
    print("drawitem small apple", str(x), str(y))

def drawWatermelon(x, y):
    print("drawitem small watermelon", str(x), str(y))

def drawCrystal_Armor(x, y):
    print("drawitem small crystal_armor", str(x), str(y))

def drawBasic_Crossbow(x, y):
    print("drawitem medium basic_crossbow", str(x), str(y))

def drawCrystal_Raygun(x, y):
    print("drawitem large crystal_raygun", str(x), str(y))

def drawText(char, x, y, R, G, B):
    print("drawchar " + str(char) + " " + str(x) + " " + str(y) + " " + str(R) + " " + str(G) + " " + str(B))

import math

def drawHealthBar(left, top, right, bottom, R, G, B):
    print("drawrect " + str(left) + " " + str(top) + " " + str(right) + " " + str(bottom) + " " + str(R) + " " + str(G) + " " + str(B))

def drawGolfClub(x, y):
    print("drawitem small golf_club", str(x), str(y))

def mapRange(s):
    a1 = -1
    a2 = 1
    b1 = 100
    b2 = 300
    t = round(b1 + (((s - a1)*(b2 - b1))/(a2 - a1)))
    return t

def backgroundFade(R, G, B):
    print("clear " + str(R) + " " + str(G) + " " + str(B))

biome = "Crystal"
difficulty = "Difficulty"
diff = "Easy"
items = "Items"
chests = "Chests"
apple = "Apple"
crossbow = "Crossbow"
knight = "Knight"
slime = "Slime"
golem = "Golem"
scorpion = "Scorpion"
bronze = "Bronze"
silver = "Silver"
armor = "Armor"
bat = "Bat"
watermelon = "Watermelon"
weapons = "Weapons"
raygun = "Raygun"
enemies = "Enemies"

""" for i in range(50):
    print("#frame")
    backgroundFade(i, math.floor(i * 1.36), i * 2)

for i in range(70):
    print("#frame")
    if i % 10 == 0:
        drawText(biome[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 200, 255, 255, 255)
    
for i in range(60):
    print("#frame")

print("clear 50 58 100")

for i in range(100):
    print("#frame")
    if i % 10 == 0:
        drawText(difficulty[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 200, 255, 255, 255)

print("clear 50 58 100")

for i in range(70):
    print("#frame")
    if i % 10 == 0 and i < 40:
        drawText(diff[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 200, 255, 255, 255)

print("clear 50 58 100")

for i in range(80):
    print("#frame")
    if i % 10 == 0 and i < 50:
        drawText(items[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 200, 255, 255, 255)

for i in range((len(apple) + 3) * 10):
    print("#frame")
    if i == 0:
        print("clear 50 68 100")    
    drawApple(320, 200)
    if i % 10 == 0 and i < len(apple) * 10:
        drawText(apple[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 100, 255, 255, 255)

for i in range((len(watermelon) + 3) * 10):
    print("#frame")
    if i == 0:
        print("clear 50 68 100")    
    drawWatermelon(320, 200)
    if i % 10 == 0 and i < len(watermelon) * 10:
        drawText(watermelon[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 100, 255, 255, 255) """

""" print("clear 50 68 100")

for i in range(70):
    print("#frame")
    if i % 10 == 0:
        drawText(weapons[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 200, 255, 255, 255)

for i in range(30):
    print("#frame")

for i in range((len(crossbow) + 3) * 10):
    print("#frame")
    if i == 0:
        print("clear 50 68 100")    
    drawBasic_Crossbow(320, 200)
    if i % 10 == 0 and i < len(crossbow) * 10:
        drawText(crossbow[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 100, 255, 255, 255)

for i in range((len(raygun) + 3) * 10):
    print("#frame")
    if i == 0:
        print("clear 50 68 100")    
    drawCrystal_Raygun(320, 200)
    if i % 10 == 0 and i < len(raygun) * 10:
        drawText(raygun[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 100, 255, 255, 255) """

""" 
print("clear 50 68 100")
for i in range(60):
    print("#frame")
    if i % 10 == 0:
        drawText(chests[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 200, 255, 255, 255)

for i in range(30):
    print("#frame")

for i in range((len(bronze) + 3) * 10):
    print("#frame")
    if i == 0:
        print("clear 50 68 100")    
    drawBronzeChest(320, 200)
    if i % 10 == 0 and i < len(bronze) * 10:
        drawText(bronze[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 100, 255, 255, 255)

for i in range((len(silver) + 3) * 10):
    print("#frame")
    if i == 0:
        print("clear 50 68 100")    
    drawSilverChest(320, 200)
    if i % 10 == 0 and i < len(silver) * 10:
        drawText(silver[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 100, 255, 255, 255) """

""" for i in range(50):
    print("#frame")
    if i == 0:
        print("clear 50 68 100")
    if i % 10 == 0:
        drawText(armor[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 200, 255, 255, 255)

for i in range(30):
    print("#frame") 

for i in range((len(armor) + 3) * 10):
    print("#frame")
    if i == 0:
        print("clear 50 68 100")    
    drawCrystal_Armor(320, 200)
    if i % 10 == 0 and i < len(armor) * 10:
        drawText(armor[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 100, 255, 255, 255)

for i in range(70):
    print("#frame")
    if i == 0:
        print("clear 50 68 100")
    if i % 10 == 0:
        drawText(enemies[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 200, 255, 255, 255)

for i in range(30):
    print("#frame") 

for i in range((len(bat) + 3) * 10):
    print("#frame")
    if i == 0:
        print("clear 50 68 100")    
    drawCrystalbat(320, 200)
    if i % 10 == 0 and i < len(bat) * 10:
        drawText(bat[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 100, 255, 255, 255) """

for i in range((len(golem) + 3) * 10):
    print("#frame")
    if i == 0:
        print("clear 50 68 100")    
    drawCrystalgolem(320, 200)
    if i % 10 == 0 and i < len(golem) * 10:
        drawText(golem[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 100, 255, 255, 255)

for i in range((len(knight) + 3) * 10):
    print("#frame")
    if i == 0:
        print("clear 50 68 100")    
    drawCrystalknight(320, 200)
    if i % 10 == 0 and i < len(knight) * 10:
        drawText(knight[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 100, 255, 255, 255)

for i in range((len(scorpion) + 3) * 10):
    print("#frame")
    if i == 0:
        print("clear 50 68 100")    
    drawCrystalscorpion(320, 200)
    if i % 10 == 0 and i < len(scorpion) * 10:
        drawText(scorpion[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 100, 255, 255, 255)

for i in range((len(slime) + 3) * 10):
    print("#frame")
    if i == 0:
        print("clear 50 68 100")    
    drawCrystalslime(320, 200)
    if i % 10 == 0 and i < len(slime) * 10:
        drawText(slime[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 100, 255, 255, 255)
