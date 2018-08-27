# Possible cube moves/rotations
# Bottom (down) clockwise, counter - D, Dc
# Bottom and middle - d, dc
# Top (up) - U, Uc, u, uc
# Right - R, Rc, r, rc
# Left - L, Lc, l, lc
# Front - F, Fc, f, fc
# Back - B, Bc, b, bc

# Perspective shifts
# notated with which axis (x, y, z) it turns around and direction
# yc means the cube rotates around the y-axis (vertical line) counter-clockwise

import random #for scramble function

# List of cube sides
WHITE = 0
GREEN = 1
RED = 2
ORANGE = 3
BLUE = 4
YELLOW = 5

class SideColorPair:
    def __init__(self, inSide, inColor):
        self.side = inSide
        self.color = inColor

class RubiksCube:
    def __init__(self, CubeStateFileName):
        # initialize variables
        self.bot = WHITE
        self.front = GREEN
        self.left = RED
        self.right = ORANGE
        self.back = BLUE
        self.top = YELLOW
        cube_data = "not set"
        self.Edges = []
        self.Corners = []
        
        # read cube state file
        with open(CubeStateFileName, "r") as file:
            cube_data = file.read()
            
        # array for edges (24 SideColorPair objects)
        # edge 1
        self.Edges.append(SideColorPair(0, int(cube_data[1])))
        self.Edges.append(SideColorPair(4, int(cube_data[63])))
        # edge 2
        self.Edges.append(SideColorPair(0, int(cube_data[4])))
        self.Edges.append(SideColorPair(2, int(cube_data[13])))
        # edge 3
        self.Edges.append(SideColorPair(0, int(cube_data[6])))
        self.Edges.append(SideColorPair(3, int(cube_data[19])))
        # edge 4
        self.Edges.append(SideColorPair(0, int(cube_data[9])))
        self.Edges.append(SideColorPair(1, int(cube_data[16])))
        # edge 5
        self.Edges.append(SideColorPair(2, int(cube_data[22])))
        self.Edges.append(SideColorPair(4, int(cube_data[58])))
        # edge 6
        self.Edges.append(SideColorPair(2, int(cube_data[24])))
        self.Edges.append(SideColorPair(1, int(cube_data[25])))
        # edge 7
        self.Edges.append(SideColorPair(1, int(cube_data[27])))
        self.Edges.append(SideColorPair(3, int(cube_data[28])))
        # edge 8
        self.Edges.append(SideColorPair(3, int(cube_data[30])))
        self.Edges.append(SideColorPair(4, int(cube_data[60])))
        # edge 9
        self.Edges.append(SideColorPair(2, int(cube_data[33])))
        self.Edges.append(SideColorPair(5, int(cube_data[46])))
        # edge 10
        self.Edges.append(SideColorPair(1, int(cube_data[36])))
        self.Edges.append(SideColorPair(5, int(cube_data[43])))
        # edge 11
        self.Edges.append(SideColorPair(3, int(cube_data[39])))
        self.Edges.append(SideColorPair(5, int(cube_data[48])))
        # edge 12
        self.Edges.append(SideColorPair(5, int(cube_data[51])))
        self.Edges.append(SideColorPair(4, int(cube_data[55])))
        
        # array for corners (24 same)
        # corner 1
        self.Corners.append(SideColorPair(0, int(cube_data[0])))
        self.Corners.append(SideColorPair(2, int(cube_data[12])))
        self.Corners.append(SideColorPair(4, int(cube_data[62])))
        # corner 2
        self.Corners.append(SideColorPair(0, int(cube_data[2])))
        self.Corners.append(SideColorPair(3, int(cube_data[20])))
        self.Corners.append(SideColorPair(4, int(cube_data[64])))
        # corner 3
        self.Corners.append(SideColorPair(0, int(cube_data[8])))
        self.Corners.append(SideColorPair(2, int(cube_data[14])))
        self.Corners.append(SideColorPair(1, int(cube_data[15])))
        # corner 4
        self.Corners.append(SideColorPair(0, int(cube_data[10])))
        self.Corners.append(SideColorPair(3, int(cube_data[18])))
        self.Corners.append(SideColorPair(1, int(cube_data[17])))
        # corner 5
        self.Corners.append(SideColorPair(5, int(cube_data[42])))
        self.Corners.append(SideColorPair(1, int(cube_data[35])))
        self.Corners.append(SideColorPair(2, int(cube_data[34])))
        # corner 6
        self.Corners.append(SideColorPair(5, int(cube_data[44])))
        self.Corners.append(SideColorPair(1, int(cube_data[37])))
        self.Corners.append(SideColorPair(3, int(cube_data[38])))
        # corner 7
        self.Corners.append(SideColorPair(5, int(cube_data[50])))
        self.Corners.append(SideColorPair(4, int(cube_data[54])))
        self.Corners.append(SideColorPair(2, int(cube_data[32])))
        # corner 8
        self.Corners.append(SideColorPair(5, int(cube_data[52])))
        self.Corners.append(SideColorPair(4, int(cube_data[56])))
        self.Corners.append(SideColorPair(3, int(cube_data[40])))
         
    def print_corner_color(self, cubeStateList, side, side_2, side_3):
        # Searches Corners array for correct corner, then prints 
        for i in range(0, 24, 3):
            corner = {}
            corner[self.Corners[i].side] = self.Corners[i].color
            corner[self.Corners[i+1].side] = self.Corners[i+1].color
            corner[self.Corners[i+2].side] = self.Corners[i+2].color
            if side in corner and side_2 in corner and side_3 in corner:
                cubeStateList.append(str(corner[side]))
                break
                
    def print_edge_color(self, cubeStateList, side, side_2):
        # Searches Corners array for correct corner, then prints 
        for i in range(0, 24, 2):
            edge = {}
            edge[self.Edges[i].side] = self.Edges[i].color
            edge[self.Edges[i+1].side] = self.Edges[i+1].color
            if side in edge and side_2 in edge:
                cubeStateList.append(str(edge[side]))
                break

    def print_State(self): #prints out state of cube like the input file
        cubeStateList = []
        self.print_corner_color(cubeStateList, 0, 4, 2)
        self.print_edge_color(cubeStateList, 0, 4)
        self.print_corner_color(cubeStateList, 0, 4, 3)
        cubeStateList.append("\n")
        self.print_edge_color(cubeStateList, 0, 2)
        cubeStateList.append('0')
        self.print_edge_color(cubeStateList, 0, 3)
        cubeStateList.append("\n")
        self.print_corner_color(cubeStateList, 0, 1, 2)
        self.print_edge_color(cubeStateList, 0, 1)
        self.print_corner_color(cubeStateList, 0, 1, 3)
        cubeStateList.append("\n")
        self.print_corner_color(cubeStateList, 2, 0, 4)
        self.print_edge_color(cubeStateList, 2, 0)
        self.print_corner_color(cubeStateList, 2, 0, 1)
        self.print_corner_color(cubeStateList, 1, 0, 2)
        self.print_edge_color(cubeStateList, 1, 0)
        self.print_corner_color(cubeStateList, 1, 0, 3)
        self.print_corner_color(cubeStateList, 3, 0, 1)
        self.print_edge_color(cubeStateList, 3, 0)
        self.print_corner_color(cubeStateList, 3, 0, 4)
        cubeStateList.append("\n")
        self.print_edge_color(cubeStateList, 2, 4)
        cubeStateList.append('2')
        self.print_edge_color(cubeStateList, 2, 1)
        self.print_edge_color(cubeStateList, 1, 2)
        cubeStateList.append('1')
        self.print_edge_color(cubeStateList, 1, 3)
        self.print_edge_color(cubeStateList, 3, 1)
        cubeStateList.append('3')
        self.print_edge_color(cubeStateList, 3, 4)
        cubeStateList.append("\n")
        self.print_corner_color(cubeStateList, 2, 5, 4)
        self.print_edge_color(cubeStateList, 2, 5)
        self.print_corner_color(cubeStateList, 2, 5, 1)
        self.print_corner_color(cubeStateList, 1, 5, 2)
        self.print_edge_color(cubeStateList, 1, 5)
        self.print_corner_color(cubeStateList, 1, 5, 3)
        self.print_corner_color(cubeStateList, 3, 5, 1)
        self.print_edge_color(cubeStateList, 3, 5)
        self.print_corner_color(cubeStateList, 3, 5, 4)
        cubeStateList.append("\n")
        self.print_corner_color(cubeStateList, 5, 1, 2)
        self.print_edge_color(cubeStateList, 5, 1)
        self.print_corner_color(cubeStateList, 5, 1, 3)
        cubeStateList.append("\n")
        self.print_edge_color(cubeStateList, 5, 2)
        cubeStateList.append('5')
        self.print_edge_color(cubeStateList, 5, 3)
        cubeStateList.append("\n")
        self.print_corner_color(cubeStateList, 5, 4, 2)
        self.print_edge_color(cubeStateList, 5, 4)
        self.print_corner_color(cubeStateList, 5, 4, 3)
        cubeStateList.append("\n")
        self.print_corner_color(cubeStateList, 4, 5, 2)
        self.print_edge_color(cubeStateList, 4, 5)
        self.print_corner_color(cubeStateList, 4, 5, 3)
        cubeStateList.append("\n")
        self.print_edge_color(cubeStateList, 4, 2)
        cubeStateList.append('4')
        self.print_edge_color(cubeStateList, 4, 3)
        cubeStateList.append("\n")
        self.print_corner_color(cubeStateList, 4, 0, 2)
        self.print_edge_color(cubeStateList, 4, 0)
        self.print_corner_color(cubeStateList, 4, 0, 3)
        
        cubeState = ''.join(cubeStateList)
        print (cubeState)
        
    # shifts in perspective
    def y(self): #rotates cube clockwise around y-axis
        print ("y")
        temp_front = self.front #temp variable to hold front value
        self.front = self.right
        self.right = self.back
        self.back = self.left
        self.left = temp_front
    def yc(self):
        print ("yc")
        temp_front = self.front
        self.front = self.left
        self.left = self.back
        self.back = self.right
        self.right = temp_front
    def x(self): #clockwise rotation if viewed from right side
        print ("x")
        temp_front = self.front
        self.front = self.bot
        self.bot = self.back
        self.back = self.top
        self.top = temp_front
    def xc(self):
        print ("xc")
        temp_front = self.front
        self.front = self.top
        self.top = self.back
        self.back = self.bot
        self.bot = temp_front
    def z(self):
        print ("z")
        temp_right = self.right
        self.right = self.top
        self.top = self.left
        self.left = self.bot
        self.bot = temp_right
    def zc(self):
        print ("zc")
        temp_right = self.right
        self.right = self.bot
        self.bot = self.left
        self.left = self.top
        self.top = temp_right
        
    def find_edges_on_side(self, inSide):
        edges = []
        i = 0
        while (len(edges) < 4):
            if (self.Edges[i].side == inSide):
                if (i % 2 == 0): # first in pair of edge edges
                    edges.append((i, i+1))
                else: # second one
                    edges.append((i-1, i))
            i += 1
        return edges
    
    def find_corners_on_side(self, inSide):
        corners = []
        i = 0
        while (len(corners) < 4):
            if (self.Corners[i].side == inSide):
                if (i % 3 == 0): #first of corner sides
                    corners.append((i, i+1, i+2))
                elif (i % 3 == 1): #second
                    corners.append((i-1, i, i+1))
                else: # last
                    corners.append((i-2, i-1, i))
            i += 1
        return corners
        
    def find_color_edges(self, inColor):
    # colors will always be in same positions in array if the cube 
    # starts solved
        edges = []
        i = 0
        while (len(edges) < 4):
            if (self.Edges[i].color == inColor):
                if (i % 2 == 0): # first in pair of edge edges
                    edges.append((i, i+1))
                else: # seconed one
                    edges.append((i-1, i))
            i += 1
        return edges
        
    # fundamental rotations
    def D(self):
        print ("D")
        # select 4 edges connected to self.bot
        bot_edges = self.find_edges_on_side(self.bot)
        # loop through edges and move to new sides
        for i in range(4):
            for ii in range(2):
                if self.Edges[bot_edges[i][ii]].side == self.bot:
                    continue # that side of edge doesn't move
                elif self.Edges[bot_edges[i][ii]].side == self.front:
                    self.Edges[bot_edges[i][ii]].side = self.right
                elif self.Edges[bot_edges[i][ii]].side == self.right:
                    self.Edges[bot_edges[i][ii]].side = self.back
                elif self.Edges[bot_edges[i][ii]].side == self.back:
                    self.Edges[bot_edges[i][ii]].side = self.left
                elif self.Edges[bot_edges[i][ii]].side == self.left:
                    self.Edges[bot_edges[i][ii]].side = self.front
        # select 4 corners connected to self.bot
        bot_corners = self.find_corners_on_side(self.bot)
        # loop through corners and move to new sides
        for i in range(4):
            for ii in range(3):
                if self.Corners[bot_corners[i][ii]].side == self.bot:
                    continue # that side of corner doesn't move
                elif self.Corners[bot_corners[i][ii]].side == self.front:
                    self.Corners[bot_corners[i][ii]].side = self.right
                elif self.Corners[bot_corners[i][ii]].side == self.right:
                    self.Corners[bot_corners[i][ii]].side = self.back
                elif self.Corners[bot_corners[i][ii]].side == self.back:
                    self.Corners[bot_corners[i][ii]].side = self.left
                elif self.Corners[bot_corners[i][ii]].side == self.left:
                    self.Corners[bot_corners[i][ii]].side = self.front

    def Dc(self):
        print ("Dc")
        bot_edges = self.find_edges_on_side(self.bot)
        # loop through edges and move to new sides
        for i in range(4):
            for ii in range(2):
                if self.Edges[bot_edges[i][ii]].side == self.bot:
                    continue # that side of edge doesn't move
                elif self.Edges[bot_edges[i][ii]].side == self.front:
                    self.Edges[bot_edges[i][ii]].side = self.left
                elif self.Edges[bot_edges[i][ii]].side == self.right:
                    self.Edges[bot_edges[i][ii]].side = self.front
                elif self.Edges[bot_edges[i][ii]].side == self.back:
                    self.Edges[bot_edges[i][ii]].side = self.right
                elif self.Edges[bot_edges[i][ii]].side == self.left:
                    self.Edges[bot_edges[i][ii]].side = self.back
        bot_corners = self.find_corners_on_side(self.bot)
        # loop through corners and move to new sides
        for i in range(4):
            for ii in range(3):
                if self.Corners[bot_corners[i][ii]].side == self.bot:
                    continue # that side of corner doesn't move
                elif self.Corners[bot_corners[i][ii]].side == self.front:
                    self.Corners[bot_corners[i][ii]].side = self.left
                elif self.Corners[bot_corners[i][ii]].side == self.right:
                    self.Corners[bot_corners[i][ii]].side = self.front
                elif self.Corners[bot_corners[i][ii]].side == self.back:
                    self.Corners[bot_corners[i][ii]].side = self.right
                elif self.Corners[bot_corners[i][ii]].side == self.left:
                    self.Corners[bot_corners[i][ii]].side = self.back
    def U(self):
        print ("U")
        top_edges = self.find_edges_on_side(self.top)
        # loop through edges and move to new sides
        for i in range(4):
            for ii in range(2):
                if self.Edges[top_edges[i][ii]].side == self.top:
                    continue # that side of edge doesn't move
                elif self.Edges[top_edges[i][ii]].side == self.front:
                    self.Edges[top_edges[i][ii]].side = self.left
                elif self.Edges[top_edges[i][ii]].side == self.right:
                    self.Edges[top_edges[i][ii]].side = self.front
                elif self.Edges[top_edges[i][ii]].side == self.back:
                    self.Edges[top_edges[i][ii]].side = self.right
                elif self.Edges[top_edges[i][ii]].side == self.left:
                    self.Edges[top_edges[i][ii]].side = self.back
        top_corners = self.find_corners_on_side(self.top)
        # loop through corners and move to new sides
        for i in range(4):
            for ii in range(3):
                if self.Corners[top_corners[i][ii]].side == self.top:
                    continue # that side of corner doesn't move
                elif self.Corners[top_corners[i][ii]].side == self.front:
                    self.Corners[top_corners[i][ii]].side = self.left
                elif self.Corners[top_corners[i][ii]].side == self.right:
                    self.Corners[top_corners[i][ii]].side = self.front
                elif self.Corners[top_corners[i][ii]].side == self.back:
                    self.Corners[top_corners[i][ii]].side = self.right
                elif self.Corners[top_corners[i][ii]].side == self.left:
                    self.Corners[top_corners[i][ii]].side = self.back
    def Uc(self):
        print ("Uc")
        top_edges = self.find_edges_on_side(self.top)
        # loop through edges and move to new sides
        for i in range(4):
            for ii in range(2):
                if self.Edges[top_edges[i][ii]].side == self.top:
                    continue # that side of edge doesn't move
                elif self.Edges[top_edges[i][ii]].side == self.front:
                    self.Edges[top_edges[i][ii]].side = self.right
                elif self.Edges[top_edges[i][ii]].side == self.right:
                    self.Edges[top_edges[i][ii]].side = self.back
                elif self.Edges[top_edges[i][ii]].side == self.back:
                    self.Edges[top_edges[i][ii]].side = self.left
                elif self.Edges[top_edges[i][ii]].side == self.left:
                    self.Edges[top_edges[i][ii]].side = self.front
        top_corners = self.find_corners_on_side(self.top)
        # loop through corners and move to new sides
        for i in range(4):
            for ii in range(3):
                if self.Corners[top_corners[i][ii]].side == self.top:
                    continue # that side of corner doesn't move
                elif self.Corners[top_corners[i][ii]].side == self.front:
                    self.Corners[top_corners[i][ii]].side = self.right
                elif self.Corners[top_corners[i][ii]].side == self.right:
                    self.Corners[top_corners[i][ii]].side = self.back
                elif self.Corners[top_corners[i][ii]].side == self.back:
                    self.Corners[top_corners[i][ii]].side = self.left
                elif self.Corners[top_corners[i][ii]].side == self.left:
                    self.Corners[top_corners[i][ii]].side = self.front
    def L(self):
        print ("L")
        left_edges = self.find_edges_on_side(self.left)
        # loop through edges and move to new sides
        for i in range(4):
            for ii in range(2):
                if self.Edges[left_edges[i][ii]].side == self.left:
                    continue # that side of edge doesn't move
                elif self.Edges[left_edges[i][ii]].side == self.front:
                    self.Edges[left_edges[i][ii]].side = self.bot
                elif self.Edges[left_edges[i][ii]].side == self.bot:
                    self.Edges[left_edges[i][ii]].side = self.back
                elif self.Edges[left_edges[i][ii]].side == self.back:
                    self.Edges[left_edges[i][ii]].side = self.top
                elif self.Edges[left_edges[i][ii]].side == self.top:
                    self.Edges[left_edges[i][ii]].side = self.front
        left_corners = self.find_corners_on_side(self.left)
        # loop through corners and move to new sides
        for i in range(4):
            for ii in range(3):
                if self.Corners[left_corners[i][ii]].side == self.left:
                    continue # that side of corner doesn't move
                elif self.Corners[left_corners[i][ii]].side == self.front:
                    self.Corners[left_corners[i][ii]].side = self.bot
                elif self.Corners[left_corners[i][ii]].side == self.bot:
                    self.Corners[left_corners[i][ii]].side = self.back
                elif self.Corners[left_corners[i][ii]].side == self.back:
                    self.Corners[left_corners[i][ii]].side = self.top
                elif self.Corners[left_corners[i][ii]].side == self.top:
                    self.Corners[left_corners[i][ii]].side = self.front
    def Lc(self):
        print ("Lc")
        left_edges = self.find_edges_on_side(self.left)
        # loop through edges and move to new sides
        for i in range(4):
            for ii in range(2):
                if self.Edges[left_edges[i][ii]].side == self.left:
                    continue # that side of edge doesn't move
                elif self.Edges[left_edges[i][ii]].side == self.front:
                    self.Edges[left_edges[i][ii]].side = self.top
                elif self.Edges[left_edges[i][ii]].side == self.bot:
                    self.Edges[left_edges[i][ii]].side = self.front
                elif self.Edges[left_edges[i][ii]].side == self.back:
                    self.Edges[left_edges[i][ii]].side = self.bot
                elif self.Edges[left_edges[i][ii]].side == self.top:
                    self.Edges[left_edges[i][ii]].side = self.back
        left_corners = self.find_corners_on_side(self.left)
        # loop through corners and move to new sides
        for i in range(4):
            for ii in range(3):
                if self.Corners[left_corners[i][ii]].side == self.left:
                    continue # that side of corner doesn't move
                elif self.Corners[left_corners[i][ii]].side == self.front:
                    self.Corners[left_corners[i][ii]].side = self.top
                elif self.Corners[left_corners[i][ii]].side == self.bot:
                    self.Corners[left_corners[i][ii]].side = self.front
                elif self.Corners[left_corners[i][ii]].side == self.back:
                    self.Corners[left_corners[i][ii]].side = self.bot
                elif self.Corners[left_corners[i][ii]].side == self.top:
                    self.Corners[left_corners[i][ii]].side = self.back
    def R(self):
        print ("R")
        right_edges = self.find_edges_on_side(self.right)
        # loop through edges and move to new sides
        for i in range(4):
            for ii in range(2):
                if self.Edges[right_edges[i][ii]].side == self.right:
                    continue # that side of edge doesn't move
                elif self.Edges[right_edges[i][ii]].side == self.front:
                    self.Edges[right_edges[i][ii]].side = self.top
                elif self.Edges[right_edges[i][ii]].side == self.bot:
                    self.Edges[right_edges[i][ii]].side = self.front
                elif self.Edges[right_edges[i][ii]].side == self.back:
                    self.Edges[right_edges[i][ii]].side = self.bot
                elif self.Edges[right_edges[i][ii]].side == self.top:
                    self.Edges[right_edges[i][ii]].side = self.back
        right_corners = self.find_corners_on_side(self.right)
        # loop through corners and move to new sides
        for i in range(4):
            for ii in range(3):
                if self.Corners[right_corners[i][ii]].side == self.right:
                    continue # that side of corner doesn't move
                elif self.Corners[right_corners[i][ii]].side == self.front:
                    self.Corners[right_corners[i][ii]].side = self.top
                elif self.Corners[right_corners[i][ii]].side == self.bot:
                    self.Corners[right_corners[i][ii]].side = self.front
                elif self.Corners[right_corners[i][ii]].side == self.back:
                    self.Corners[right_corners[i][ii]].side = self.bot
                elif self.Corners[right_corners[i][ii]].side == self.top:
                    self.Corners[right_corners[i][ii]].side = self.back
    def Rc(self):
        print ("Rc")
        right_edges = self.find_edges_on_side(self.right)
        # loop through edges and move to new sides
        for i in range(4):
            for ii in range(2):
                if self.Edges[right_edges[i][ii]].side == self.right:
                    continue # that side of edge doesn't move
                elif self.Edges[right_edges[i][ii]].side == self.front:
                    self.Edges[right_edges[i][ii]].side = self.bot
                elif self.Edges[right_edges[i][ii]].side == self.bot:
                    self.Edges[right_edges[i][ii]].side = self.back
                elif self.Edges[right_edges[i][ii]].side == self.back:
                    self.Edges[right_edges[i][ii]].side = self.top
                elif self.Edges[right_edges[i][ii]].side == self.top:
                    self.Edges[right_edges[i][ii]].side = self.front
        right_corners = self.find_corners_on_side(self.right)
        # loop through corners and move to new sides
        for i in range(4):
            for ii in range(3):
                if self.Corners[right_corners[i][ii]].side == self.right:
                    continue # that side of corner doesn't move
                elif self.Corners[right_corners[i][ii]].side == self.front:
                    self.Corners[right_corners[i][ii]].side = self.bot
                elif self.Corners[right_corners[i][ii]].side == self.bot:
                    self.Corners[right_corners[i][ii]].side = self.back
                elif self.Corners[right_corners[i][ii]].side == self.back:
                    self.Corners[right_corners[i][ii]].side = self.top
                elif self.Corners[right_corners[i][ii]].side == self.top:
                    self.Corners[right_corners[i][ii]].side = self.front
    def F(self):
        print ("F")
        front_edges = self.find_edges_on_side(self.front)
        # loop through edges and move to new sides
        for i in range(4):
            for ii in range(2):
                if self.Edges[front_edges[i][ii]].side == self.front:
                    continue # that side of edge doesn't move
                elif self.Edges[front_edges[i][ii]].side == self.top:
                    self.Edges[front_edges[i][ii]].side = self.right
                elif self.Edges[front_edges[i][ii]].side == self.right:
                    self.Edges[front_edges[i][ii]].side = self.bot
                elif self.Edges[front_edges[i][ii]].side == self.bot:
                    self.Edges[front_edges[i][ii]].side = self.left
                elif self.Edges[front_edges[i][ii]].side == self.left:
                    self.Edges[front_edges[i][ii]].side = self.top
        front_corners = self.find_corners_on_side(self.front)
        # loop through corners and move to new sides
        for i in range(4):
            for ii in range(3):
                if self.Corners[front_corners[i][ii]].side == self.front:
                    continue # that side of corner doesn't move
                elif self.Corners[front_corners[i][ii]].side == self.top:
                    self.Corners[front_corners[i][ii]].side = self.right
                elif self.Corners[front_corners[i][ii]].side == self.right:
                    self.Corners[front_corners[i][ii]].side = self.bot
                elif self.Corners[front_corners[i][ii]].side == self.bot:
                    self.Corners[front_corners[i][ii]].side = self.left
                elif self.Corners[front_corners[i][ii]].side == self.left:
                    self.Corners[front_corners[i][ii]].side = self.top
    def Fc(self):
        print ("Fc")
        front_edges = self.find_edges_on_side(self.front)
        # loop through edges and move to new sides
        for i in range(4):
            for ii in range(2):
                if self.Edges[front_edges[i][ii]].side == self.front:
                    continue # that side of edge doesn't move
                elif self.Edges[front_edges[i][ii]].side == self.top:
                    self.Edges[front_edges[i][ii]].side = self.left
                elif self.Edges[front_edges[i][ii]].side == self.right:
                    self.Edges[front_edges[i][ii]].side = self.top
                elif self.Edges[front_edges[i][ii]].side == self.bot:
                    self.Edges[front_edges[i][ii]].side = self.right
                elif self.Edges[front_edges[i][ii]].side == self.left:
                    self.Edges[front_edges[i][ii]].side = self.bot
        front_corners = self.find_corners_on_side(self.front)
        # loop through corners and move to new sides
        for i in range(4):
            for ii in range(3):
                if self.Corners[front_corners[i][ii]].side == self.front:
                    continue # that side of corner doesn't move
                elif self.Corners[front_corners[i][ii]].side == self.top:
                    self.Corners[front_corners[i][ii]].side = self.left
                elif self.Corners[front_corners[i][ii]].side == self.right:
                    self.Corners[front_corners[i][ii]].side = self.top
                elif self.Corners[front_corners[i][ii]].side == self.bot:
                    self.Corners[front_corners[i][ii]].side = self.right
                elif self.Corners[front_corners[i][ii]].side == self.left:
                    self.Corners[front_corners[i][ii]].side = self.bot
    def B(self):
        print ("B")
        back_edges = self.find_edges_on_side(self.back)
        # loop through edges and move to new sides
        for i in range(4):
            for ii in range(2):
                if self.Edges[back_edges[i][ii]].side == self.back:
                    continue # that side of edge doesn't move
                elif self.Edges[back_edges[i][ii]].side == self.top:
                    self.Edges[back_edges[i][ii]].side = self.left
                elif self.Edges[back_edges[i][ii]].side == self.right:
                    self.Edges[back_edges[i][ii]].side = self.top
                elif self.Edges[back_edges[i][ii]].side == self.bot:
                    self.Edges[back_edges[i][ii]].side = self.right
                elif self.Edges[back_edges[i][ii]].side == self.left:
                    self.Edges[back_edges[i][ii]].side = self.bot
        back_corners = self.find_corners_on_side(self.back)
        # loop through corners and move to new sides
        for i in range(4):
            for ii in range(3):
                if self.Corners[back_corners[i][ii]].side == self.back:
                    continue # that side of corner doesn't move
                elif self.Corners[back_corners[i][ii]].side == self.top:
                    self.Corners[back_corners[i][ii]].side = self.left
                elif self.Corners[back_corners[i][ii]].side == self.right:
                    self.Corners[back_corners[i][ii]].side = self.top
                elif self.Corners[back_corners[i][ii]].side == self.bot:
                    self.Corners[back_corners[i][ii]].side = self.right
                elif self.Corners[back_corners[i][ii]].side == self.left:
                    self.Corners[back_corners[i][ii]].side = self.bot
    def Bc(self): 
        print ("Bc")
        back_edges = self.find_edges_on_side(self.back)
        # loop through edges and move to new sides
        for i in range(4):
            for ii in range(2):
                if self.Edges[back_edges[i][ii]].side == self.back:
                    continue # that side of edge doesn't move
                elif self.Edges[back_edges[i][ii]].side == self.top:
                    self.Edges[back_edges[i][ii]].side = self.right
                elif self.Edges[back_edges[i][ii]].side == self.right:
                    self.Edges[back_edges[i][ii]].side = self.bot
                elif self.Edges[back_edges[i][ii]].side == self.bot:
                    self.Edges[back_edges[i][ii]].side = self.left
                elif self.Edges[back_edges[i][ii]].side == self.left:
                    self.Edges[back_edges[i][ii]].side = self.top
        back_corners = self.find_corners_on_side(self.back)
        # loop through corners and move to new sides
        for i in range(4):
            for ii in range(3):
                if self.Corners[back_corners[i][ii]].side == self.back:
                    continue # that side of corner doesn't move
                elif self.Corners[back_corners[i][ii]].side == self.top:
                    self.Corners[back_corners[i][ii]].side = self.right
                elif self.Corners[back_corners[i][ii]].side == self.right:
                    self.Corners[back_corners[i][ii]].side = self.bot
                elif self.Corners[back_corners[i][ii]].side == self.bot:
                    self.Corners[back_corners[i][ii]].side = self.left
                elif self.Corners[back_corners[i][ii]].side == self.left:
                    self.Corners[back_corners[i][ii]].side = self.top
    
    #derived rotations
    def d(self):  # Uc + yc
        print ("- d")
        self.Uc()
        self.yc()
    def dc(self): # U + y
        print ("- dc")
        self.U()
        self.y()
    def u(self):  # Dc + y
        print ("- u")
        self.Dc()
        self.y()
    def uc(self):  # D + yc
        print ("- uc")
        self.D()
        self.yc()
    def l(self):  # R + xc
        print ("- l")
        self.R()
        self.xc()
    def lc(self): # Rc + x
        print ("- lc")
        self.Rc()
        self.x()
    def r(self):  # L + x
        print ("- r")
        self.L()
        self.x()
    def rc(self): # Lc + xc
        print ("- rc")
        self.Lc()
        self.xc()
    def f(self):  # Bc + z
        print ("- f")
        self.Bc()
        self.z()
    def fc(self): # B + zc
        print ("- fc")
        self.B()
        self.zc()
    def b(self):  # Fc + z
        print ("- b")
        self.Fc()
        self.z()
    def bc(self): # F + zc
        print ("- bc")
        self.F()
        self.zc()
    def M(self):  # Rc + L + x
        print ("- M")
        self.Rc()
        self.L()
        self.x()
    def Mc(self): # R + Lc + xc
        print ("- Mc")
        self.R()
        self.Lc()
        self.xc()
    
    #rotations times 2
    def D2(self):
        print ("- D2")
        self.D()
        self.D()
    def d2(self):  
        print ("- d2")
        self.d()
        self.d()
    def U2(self):
        print ("- U2")
        self.U()
        self.U()
    def u2(self): 
        print ("- u2")
        self.u()
        self.u()
    def L2(self):
        print ("- L2")
        self.L()
        self.L()
    def l2(self):  
        print ("- l2")
        self.l()
        self.l()
    def R2(self):
        print ("- R2")
        self.R()
        self.R()
    def r2(self):  
        print ("- r2")
        self.r()
        self.r()
    def F2(self):
        print ("- F2")
        self.F()
        self.F()
    def f2(self):  
        print ("- f2")
        self.f()
        self.f()
    def B2(self):
        print ("- B2")
        self.B()
        self.B()
    def b2(self):  
        print ("- b2")
        self.b()
        self.b()
    def M2(self): 
        print ("- M2")
        self.M()
        self.M()
    
    def scramble(self):
        # execute 20 random rotations on cube
        print ("Scrambling")
        seedval = input("Enter seed value for scramble: ")
        random.seed(seedval)
        for i in range(20):
            number = random.randint(1, 18)
            if number == 1:
                self.D()
            elif number == 2:
                self.Dc()
            elif number == 3:
                self.U()
            elif number == 4:
                self.Uc()
            elif number == 5:
                self.L() 
            elif number == 6: 
                self.Lc()
            elif number == 7:
                self.R() 
            elif number == 8:
                self.Rc() 
            elif number == 9:
                self.F() 
            elif number == 10:
                self.Fc() 
            elif number == 11:
                self.B() 
            elif number == 12:
                self.Bc() 
            elif number == 13:
                self.D2() 
            elif number == 14:
                self.U2()
            elif number == 15:
                self.L2()
            elif number == 16:
                self.R2()
            elif number == 17:
                self.F2()
            elif number == 18:
                self.B2()