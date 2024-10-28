import math

def drawText(char, x, y, R, G, B):
    print("drawchar " + str(char) + " " + str(x) + " " + str(y) + " " + str(R) + " " + str(G) + " " + str(B))
    
def drawHealthBar(left, top, right, bottom, R, G, B):
    print("drawrect " + str(left) + " " + str(top) + " " + str(right) + " " + str(bottom) + " " + str(R) + " " + str(G) + " " + str(B))

def drawPlayer(x, y):
    print("drawentity player1", str(x), str(y))

def drawMountainSlime(x, y):
    print("drawentity mountainslime", str(x), str(y))

def drawBronzeChest(x, y):
    print("drawentity bronze", str(x), str(y))
    
def drawSilverChest(x, y):
    print("drawentity silver", str(x), str(y))

def drawApple(x, y):
    print("drawitem small apple", str(x), str(y))

def drawGolfClub(x, y):
    print("drawitem small golf_club", str(x), str(y))

def swingGolfClub():
    for i in range(40):
        print("#frame")
        print("clear 156 76 9")
        drawGolfClub(i * 15, i * 10)

def drawSword(x, y):
    print("drawitem large sword", str(x), str(y))

def swingSword():
    for i in range(40):
        print("#frame")
        print("clear 156 76 9")
        drawSword(i * 15, i * 10)

def mapRange(s):
    a1 = -1
    a2 = 1
    b1 = 100
    b2 = 300
    t = round(b1 + (((s - a1)*(b2 - b1))/(a2 - a1)))
    return t

def backgroundFade(R, G, B):
    print("clear " + str(R) + " " + str(G) + " " + str(B))

""" for i in range(50):
    print("#frame")
    backgroundFade(math.floor(i * 3.12), math.floor(i * 1.52), math.floor(i * 0.18)) """

""" for i in range(100):
    print("#frame")
    print("clear 156 76 9")
    drawPlayer(320, i * 2)
    drawText("S", 500, 200, 255, 255, 255)

for i in range(100):
    print("#frame")
    print("clear 156 76 9")
    drawPlayer(320 - i * 2, 198)
    drawText("A", 500, 200, 255, 255, 255)

for i in range(100):
    print("#frame")
    print("clear 156 76 9")
    drawPlayer(120, 198 - i * 2)
    drawText("W", 500, 200, 255, 255, 255)
    
for i in range(100):
    print("#frame")
    print("clear 156 76 9")
    drawPlayer(120 + i * 2, 0)
    drawText("D", 500, 200, 255, 255, 255)"""
    
""" for i in range(100):
    print("#frame")
    print("clear 156 76 9")
    drawPlayer(320 - i * 2, i * 2)
    if i % 2 == 0:
        drawText("A", 495, 200, 255, 255, 255)
    else:
        drawText("S", 505, 200, 255, 255, 255) """

""" for i in range(100):
    print("#frame")
    print("clear 156 76 9")
    drawPlayer(120 + i * 2, 198 + i * 2)
    if i % 2 == 0:
        drawText("S", 495, 200, 255, 255, 255)
    else:
        drawText("D", 505, 200, 255, 255, 255)

for i in range(10):
    print("#frame")
    print("clear 156 76 9")
    drawPlayer(320, 396 + i * 2)
    drawText("S", 500, 200, 255, 255, 255) """

""" for i in range(60):
    print("#frame")
    print("clear 156 76 9")
    drawPlayer(320, i * 2)
    drawBronzeChest(320, 200)
    drawText("S", 495, 200, 255, 255, 255)

text = "Loot"
for i in range(40):
    print("#frame")
    if i == 0:
        print("clear 156 76 9")
    if i % 10 == 0:
        drawText(text[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 200, 255, 255, 255) """

""" swingGolfClub()

print("#frame")
print("clear 156 76 9")
drawPlayer(320, 118)
drawGolfClub(400, 118)
drawApple(320, 200)

for i in range(20):
    print("#frame")

for i in range(30):
    print("#frame")
    print("clear 156 76 9")
    drawPlayer(320, 118 + i * 2)
    drawGolfClub(400, 118 + i * 2)
    if i < 25:
        drawApple(320, 200)

text = "Picked"
for i in range(60):
    print("#frame")
    if i % 10 == 0:
        drawText(text[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 200, 255, 255, 255)

text = "up"
for i in range(20):
    print("#frame")
    if i % 10 == 0:
        drawText(text[math.floor(i / 10)], 375 + math.floor(i / 10) * 10, 200, 255, 255, 255)

for i in range(125):
    print("#frame")
    print("clear 156 76 9")
    drawPlayer(320, 178 + i * 2)
    drawGolfClub(400, 178 + i * 2)
    drawText("S", 500, 200, 255, 255, 255) """

""" print("#frame")
print("clear 156 76 9")
drawPlayer(320, 0)
drawGolfClub(400, 0)
drawMountainSlime(320, 400) """
""" 
for i in range(80):
    print("#frame")
    print("clear 156 76 9")
    drawPlayer(320, 0)
    drawGolfClub(400, 0)
    drawMountainSlime(320, 400 - i * 2)
 """
""" for i in range(20):
    print("#frame")
    print("clear 156 76 9")
    drawPlayer(320, 0 - i * 2)
    drawGolfClub(400, 0 - i * 2)   
    drawMountainSlime(320, 240 - i * 2)    

for i in range(100):
    print("#frame")
    print("clear 156 76 9")
    drawPlayer(320, 400 - i * 5)
    drawGolfClub(400, 400 - i * 5)  
    drawMountainSlime(320, 600 - i * 4)

for i in range(60):
    print("#frame")
    print("clear 156 76 9")
    drawPlayer(320, 400 - i * 2)
    drawGolfClub(400, 400 - i * 2)
    drawSilverChest(320, 200) """

""" text = "LMB"
for i in range(30):
    print("#frame")
    if i == 0:
        print("clear 156 76 9")
    if i % 10 == 0:
        drawText(text[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 200, 255, 255, 255)""" 

""" swingGolfClub()

print("#frame")
print("clear 156 76 9")
drawPlayer(320, 282)
drawGolfClub(400, 282)
drawSword(320, 200)

for i in range(20):
    print("#frame")

for i in range(30):
    print("#frame")
    print("clear 156 76 9")
    drawPlayer(320, 282 - i * 2)
    drawGolfClub(400, 282 - i * 2)
    if i < 25:
        drawSword(320, 200)

text = "Picked"
for i in range(60):
    print("#frame")
    if i % 10 == 0:
        drawText(text[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 200, 255, 255, 255)

text = "up"
for i in range(20):
    print("#frame")
    if i % 10 == 0:
        drawText(text[math.floor(i / 10)], 375 + math.floor(i / 10) * 10, 200, 255, 255, 255) """

""" for i in range(120):
    print("#frame")
    print("clear 156 76 9")
    if i < 30:
        drawText("E", 500, 200, 255, 255, 255)
    elif i > 60 and i < 90:
        drawText("E", 500, 200, 255, 255, 255)

    drawPlayer(320, 222)

    if i < 60:
        drawApple(400, 222)
    elif i < 120:
        drawSword(400, 222) """

""" for i in range(100):
    print("#frame")
    print("clear 156 76 9")
    drawPlayer(320, 222)
    drawSword(400, 222)
    drawMountainSlime(320, 500 - i * 2)
    drawHealthBar(250, 170, 450, 190, 156 + i, math.floor(76 - i * 0.76), math.floor(9 - i * 0.09)) 
    drawHealthBar(300, 450 - i * 2, 400, 470 - i * 2, 0, 255, 0)

for i in range(30):
    print("#frame")
    print("clear 156 76 9")
    drawPlayer(320, 222)
    drawSword(400, 222)
    if i < 15:
        drawMountainSlime(320, 300 - i * 2)
        drawHealthBar(250, 170, 450, 190, 255, 0, 0) 
        drawHealthBar(300, 250 - i * 2, 400, 270 - i * 2, 0, 255, 0)   
    else:
        drawMountainSlime(320, 272)
        drawHealthBar(250, 170, 450, 190, 0, 0, 0)
        drawHealthBar(250, 170, 450 - i * 2, 190, 255, 0, 0)
        drawHealthBar(300, 222, 400, 242, 0, 255, 0)   

text = "Attack"
for i in range(60):
    print("#frame")
    if i == 0:
        print("clear 156 76 9")
    if i % 10 == 0:
        drawText(text[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 200, 255, 255, 255) """

""" text = "LMB"
for i in range(30):
    print("#frame")
    if i % 10 == 0:
        drawText(text[math.floor(i / 10)], 300 + math.floor(i / 10) * 20, 220, 255, 255, 255)

swingSword() """

""" for i in range(50):
    print("#frame")
    if i < 22:
        print("clear 156 76 9")
        drawPlayer(320, 222)
        drawSword(400, 222)  
        drawHealthBar(250, 170, 450, 190, 0, 0, 0)
        drawHealthBar(250, 170, 392, 190, 255, 0, 0)
        if i < 21:
            drawMountainSlime(320, 272)
            drawHealthBar(300, 222, 400, 242, 0, 0, 0)
            drawHealthBar(300, 222, 400, math.floor(242 - i * 12.1), 0, 255, 0)  

for i in range(60):
    print("#frame")
    print("clear 156 76 9")
    if i < 30:
        drawText("Q", 500, 200, 255, 255, 255)
    drawPlayer(320, 222)
    drawHealthBar(250, 170, 450, 190, 0, 0, 0)
    drawHealthBar(250, 170, 392, 190, 255, 0, 0)
    if i < 30:
        drawSword(400, 222)
    elif i < 60:
        drawApple(400, 222)

text = "Heal"
for i in range(40):
    print("#frame")
    if i % 10 == 0:
        drawText(text[math.floor(i / 10)], 305 + math.floor(i / 10) * 10, 100, 255, 255, 255) """

text = "LMB"
""" for i in range(30):
    print("#frame")
    if i % 10 == 0:
        drawText(text[math.floor(i / 10)], 310 + math.floor(i / 10) * 10, 120, 255, 255, 255)

for i in range(58):
    print("#frame")
    print("clear 156 76 9")
    drawPlayer(320, 222)
    drawHealthBar(250, 170, 450, 190, 0, 0, 0)
    drawHealthBar(250, 170, 392 + i, 190, 255, 0, 0)
"""
""" for i in range(100):
    print("#frame")
    print("clear 156 76 9")
    if i < 30:
        drawText("Q", 500, 200, 255, 255, 255)
    else:
        drawGolfClub(400, 222)
    drawPlayer(320, 222)
    drawHealthBar(250, 170, 450, 190, 255 - i, math.floor(0 + i * 0.76), math.floor(0 + i * 0.09))  """

text = "to"
text2 = "Throw"
for i in range(80):
    print("#frame")
    drawGolfClub(400, 222)
    drawPlayer(320, 222)
    if i == 0:
        drawText("T", 320, 120, 255, 255, 255)
    elif i % 10 == 0 and i < 30:
        drawText(text[math.floor((i - 10) / 10)], 335 + math.floor((i - 10) / 10) * 10, 120, 255, 255, 255)
    elif i % 10 == 0 and i < 80:
        drawText(text2[math.floor((i - 30) / 10)], 370 + math.floor((i - 30) / 10) * 10, 120, 255, 255, 255)

for i in range(30):
    print("#frame")
    if i == 0:
        print("clear 156 76 9")
        drawGolfClub(500, 100)
        drawPlayer(320, 222)

for i in range(50):
    print("#frame")
    backgroundFade(math.floor(156 - i * 3.12), math.floor(76 - i * 1.52), math.floor(9 - i * 0.18))

""" for i in range(50):
    print("#frame")
    if i != 0:
        print("clear 0 0 0")
    if math.floor(i / 5) < len(text[0]):
        drawText(text[math.floor(i / 5)], 100 + math.floor(i / 5) * 5, 100, 255, 255, 255)
    drawHealthBar(270, 0, (i + 2) * 3, -120, 255, 0, 0)
    drawPlayer((i + 2) * 3)
    drawHealthBar(250, 0, -(i + 2) * 3, 390, 0, 255, 0)
    drawMountainSlime(i * 3) """



