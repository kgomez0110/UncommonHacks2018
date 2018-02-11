# |-----------------|-----------------|-----------------|-----------------|
# |-----------------|-----------------|-----------------|-----------------|
# |-7-7---7---------|-7-7---7---------|-------------7---|-------------7---|
# |---------9---7---|---------9---7---|-6-6---6-9-------|-6-6---6-9-------|
# |-----------------|-----------------|-----------------|-----------------|
# |-----------------|-----------------|-----------------|-----------------|
#
# Format:
#     EBGDAE (corresponds to lines)
#     each line has 17 spots where something could be
#     seems to range from 0-15 but could also be an x
#     Do it like nico
#
#   If the whole song is 4 count, then the sheet and tab will be 1-1

import numpy as np



class actual_measure:
    def __init__(self, e, b, g, d, a, ee):
        self.Em = e
        self.Bm = b
        self.Gm = g
        self.Dm = d
        self.Am = a
        self.em = ee

class tab_measure:

    global measures
    measures = []
    def __init__(self, tabs) :
        self.E, self.B, self.G, self.D, self.A, self.e = [[],[],[],[],[],[]]
        ii = 0

        for line in tabs:
            if ii == 0:
                self.E.append(line.split('|'))
            elif ii == 1:
                self.B.append(line.split('|'))
            elif ii == 2:
                self.G.append(line.split('|'))
            elif ii == 3:
                self.D.append(line.split('|'))
            elif ii == 4:
                self.A.append(line.split('|'))
            elif ii == 5:
                self.e.append(line.split('|'))
            ii += 1
            if ii == 6:
                ii = 0

        for jj in range(0, min(len(self.E), len(self.B), len(self.G), len(self.D), len(self.A), len(self.e))):
            if not((self.E[jj] == '') or (self.E[jj] == '\n')) :
                tib = actual_measure(self.E[jj], self.B[jj], self.G[jj], self.D[jj], self.A[jj], self.e[jj])
                measures.append(tib)


    def print_sheet(self):
        print(self.E)
        print(self.B)
        print(self.G)
        print(self.D)
        print(self.A)
        print(self.e)

def split_tab(file_name):
    with open(file_name, "r") as tabb:
        lines = tabb.readlines()
    sheet = tab_measure(lines)
# file_name = "./tabs/mississippi_tabs.txt"
# with open(file_name, "r") as tabb :
#     lines = tabb.readlines()
#
# test_sheet = tab_measure(lines)
#
# print(measures)
