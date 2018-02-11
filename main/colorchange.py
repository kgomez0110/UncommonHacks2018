from PIL import Image
im = Image.open("./notecharts/take.png") #Can be many different formats.
pix = im.load()
print(im.size[1])

for y in range (111, im.size[1]-135, 112): #jump from staff to staff
    for m in range(16, 976, 80): #jump from measure to measure
        for x in range (m, m+80, 10): #jump from 1/8th to 1/8th

            if pix[x, y] == (0, 130, 0, 255): pix[x,y] = (234, 14, 223, 255)
            if pix[x, y + 12 ] == (255, 0, 0, 255): pix[x,y+12] = (234, 14, 223, 255)
            if pix[x, y + 24 ] == (255,235, 0, 255): pix[x,y+24] = (234, 14, 223, 255)
            if pix[x, y + 36] == (0, 0, 255, 255): pix[x,y+36] = (234, 14, 223, 255)
            if pix[x, y + 48] == (255, 170, 0, 255): pix[x,y+48] = (234, 14, 223, 255)

im.save("postchange.png") # Save the modified pixels as png