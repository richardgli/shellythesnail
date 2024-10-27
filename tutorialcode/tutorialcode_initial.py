import math
def drawHealthBar(x, dx, y, dy, R, G, B):
    print("drawrect " + str(x + dx) + " " + str(y + dy) + " " + str(x + 160 + dx) + " " + str(y + 10 + dy) + " " + str(R) + " " + str(G) + " " + str(B))

def drawPlayer(x, y):
    print("drawentity player1", str(x), str(y))

def drawMountainSlime(y):
    print("drawentity mountainslime 320", str(400 - y))

def drawBronzeChest(x, y):
    print("drawentity bronze", str(x), str(y))
    
def drawSilverChest(x, y):
    print("drawentity silver", str(x), str(y))

def drawApple(x, y):
    print("drawentity apple", str(x), str(y))

def drawGolfClub(x, y):
    print("drawitem small golfclub", str(x), str(y))

def swingGolfClub():
    for i in range(30):
        print("#frame")
        print("clear 156 76 9")
        drawGolfClub(math.floor(i * 10), math.floor(i * 15))

def drawText(char, x, y, R, G, B):
    print("drawchar " + str(char) + " " + str(x) + " " + str(y) + " " + str(R) + " " + str(G) + " " + str(B))

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

swingGolfClub()

print("#frame")
print("clear 156 76 9")
drawPlayer(320, 118)
drawGolfClub(330, 118)
drawApple(320, 200)

for i in range(20):
    print("#frame")

for i in range(30):
    print("#frame")
    print("clear 156 76 9")
    drawPlayer(320, 118)
    drawGolfClub(330, 118)
    if i < 25:
        drawApple(320, 200)

text = "Picked up"
for i in range(80):
    print("#frame")
    if i % 10 == 0:
        drawText(text[math.floor(i / 10)], 300 + math.floor(i / 10) * 10, 200, 255, 255, 255)

text = "Attack"

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



