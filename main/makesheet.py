import colorcode2
from PIL import Image
def createsheet(measurelist):
    sheet = Image.open("./whitebg.png") #Can be many different formats.
    pix = sheet.load()


    songlength = len(measurelist)
    count = 0

    for y in range (111, sheet.size[1]-135, 112): #jump from staff to staff
        if count == songlength: break
        for m in range(16, 976, 80): #jump from measure to measure
            i = 0
            if count == songlength: break
            for x in range (m, m+80, 10): #jump from 1/8th to 1/8th
                if measurelist[0].green[i] != False: pix[x, y] = (0, 130, 0, 255)
                if measurelist[0].red[i] != False: pix[x, y + 12] = (255, 0, 0, 255)
                if measurelist[0].yellow[i] != False: pix[x, y + 24] = (255,235, 0, 255)
                if measurelist[0].blue[i] != False: pix[x, y + 36] = (0, 0, 255, 255)
                if measurelist[0].orange[i] != False: pix[x, y + 48] = (255, 170, 0, 255)
                i += 1
            del measurelist[0]
            count += 1




    sheet.save("newsheet.png") # Save the modified pixels as png


createsheet(colorcode2.songs)