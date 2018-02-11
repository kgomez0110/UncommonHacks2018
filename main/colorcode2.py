from PIL import Image
im = Image.open("./notecharts/take.png") #Can be many different formats.
pix = im.load()
#print(im.size) #Get the width and hight of the image for iterating over
#pix[x,y] = value # Set the RGBA Value of the image (tuple)
#im.save("alive_parrot.png") # Save the modified pixels as png

# RGB Values
# yellow = (255,235, 0, 255)
# red = (255, 0, 0, 255)
# blue = (0, 0, 255, 255)
# orange = (255, 170, 0, 255)

class measure():
    def __init__(self, green, red, yellow, blue, orange):
        self.green = green
        self.red = red
        self. yellow = yellow
        self.blue = blue
        self.orange = orange

    def printGreen(self):
        print(self.green)

    def printRed(self):
        print(self.red)

    def printYellow(self):
        print(self.yellow)

    def printBlue(self):
        print(self.blue)

    def printOrange(self):
        print(self.orange)

    def printMeasure(self):
        print(self.green)
        print(self.red)
        print(self.yellow)
        print(self.blue)
        print(self.orange)




green = []
red = []
yellow = []
blue = []
orange = []
songs = []

for y in range (111, im.size[1]-135, 112): #jump from staff to staff
    for m in range(16, 976, 80): #jump from measure to measure
        for x in range (m, m+80, 10): #jump from 1/8th to 1/8th

            if (pix[x, y] == (0, 130, 0, 255)):
                if pix[x+4,y] == (0, 130, 0, 255) and pix[x-4,y] != (0, 130, 0, 255):
                    green.append("hold_start")
                elif pix[x+4,y] == (0, 130, 0, 255) and pix[x-4,y] == (0, 130, 0, 255):
                    green.append("hold")
                else: green.append("tap")
            else: green.append(False)

            if (pix[x, y + 12] == (255, 0, 0, 255)):
                if pix[x+4,y + 12] == (255, 0, 0, 255) and pix[x-4,y + 12] != (255, 0, 0, 255):
                    red.append("hold_start")
                elif pix[x+4,y + 12] == (255, 0, 0, 255) and pix[x-4,y + 12 ] == (255, 0, 0, 255):
                    red.append("hold")
                else: red.append("tap")
            else: red.append(False)

            if (pix[x, y + 24] == (255,235, 0, 255)):
                if pix[x+4,y + 24] == (255,235, 0, 255) and pix[x-4,y + 24 ] != (255,235, 0, 255):
                    yellow.append("hold_start")
                elif pix[x+4,y + 24] == (255,235, 0, 255) and pix[x-4,y + 24 ] == (255,235, 0, 255):
                    yellow.append("hold")
                else: yellow.append("tap")
            else: yellow.append(False)

            if (pix[x, y + 36] == (0, 0, 255, 255)):
                if pix[x+4,y + 36 ] == (0, 0, 255, 255) and pix[x-4,y + 36] != (0, 0, 255, 255):
                    blue.append("hold_start")
                elif pix[x+4,y + 36] == (0, 0, 255, 255) and pix[x-4,y + 36] == (0, 0, 255, 255):
                    blue.append("hold")
                else: blue.append("tap")
            else: blue.append(False)

            if (pix[x, y +48] == (255, 170, 0, 255)):
                if pix[x+4,y + 48] == (255, 170, 0, 255) and pix[x-4,y + 48] != (255, 170, 0, 255):
                    orange.append("hold_start")
                elif pix[x+4,y + 48] == (255, 170, 0, 255) and pix[x-4,y + 48] == (255, 170, 0, 255):
                    orange.append("hold")
                else: orange.append("tap")
            else: orange.append(False)

            # red.append(pix[x, y + 12] == (255, 0, 0, 255))
            # yellow.append(pix[x, y + 24] == (255,235, 0, 255))
            # blue.append(pix[x, y + 36] == (0, 0, 255, 255))
            # orange.append(pix[x, y + 48] == (255, 170, 0, 255))

        songs.append(measure(green, red, yellow, blue, orange))

        green = []
        red = []
        yellow = []
        blue = []
        orange = []


######### WHITE SHEET to NOTE CHARTS ###########




