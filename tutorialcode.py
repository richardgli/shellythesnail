import math
def drawHealthBar(x, dx, y, dy, R, G, B):
    #print("#frame")
    print("drawrect " + str(x + dx) + " " + str(y + dy) + " " + str(x + 160 + dx) + " " + str(y + 10 + dy) + " " + str(R) + " " + str(G) + " " + str(B))

def drawPlayer(y):
    #print("#frame")
    print("drawentity player1 320", str(y - 100))

def drawMountainSlime(y):
    #print("#frame")
    print("drawentity mountainslime 320", str(400 - y))

def drawText(char, x, y, R, G, B):
    print("drawchar " + str(char) + " " + str(x) + " " + str(y) + " " + str(R) + " " + str(G) + " " + str(B))

text = ["Attack"]

for i in range(50):
    print("#frame")
    if i != 0:
        print("clear")
    if math.floor(i / 5) < len(text[0]):
        drawText(text[0][math.floor(i / 5)], 100 + math.floor(i / 5) * 5, 100, 255, 255, 255)
    drawHealthBar(270, 0, (i + 2) * 2, -120, 255, 0, 0)
    drawPlayer((i + 2) * 2)
    drawHealthBar(250, 0, -(i + 2) * 3, 390, 0, 255, 0)
    drawMountainSlime(i * 3)



