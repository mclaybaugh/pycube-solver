#!/usr/bin/python3
# Developer: Michael Claybaugh
# Started: Thursday, February 2, 2017
# 5-27-17: -making script work again now that I have Python 3.6 installed. 
#           adding parenthesis to "print" calls
# 5-28-17: -corrected 'x' and 'xc' moves in derived rotations sections, they 
#           were in the opposite places
#          - changed "ColorSidePair" to "SideColorPair" to match constructor 
#            order of parameters
# Status: in progress
# Description: python program/script to solve a rubiks cube the way a human 
#              would (white cross, white corners, middle edges, 
from RubiksCube import RubiksCube, WHITE, GREEN, RED, ORANGE, BLUE, YELLOW

CubeStateFileName = r"cube-state.txt"

# Step 0 - initialize cube
cube = RubiksCube(CubeStateFileName)
cube.scramble()

# Step 1 - position and orient bottom/white cross
print ("Solving cube now")
print ("Initial state:")
cube.print_State()
white_edges = cube.find_color_edges(WHITE)
for edge in white_edges:
	# get color of non-white side, make that the front
	if cube.Edges[edge[0]].color == WHITE:
		color = cube.Edges[edge[1]].color
		color_side = cube.Edges[edge[1]].side
		white_side = cube.Edges[edge[0]].side
	else:
		color = cube.Edges[edge[0]].color
		color_side = cube.Edges[edge[0]].side
		white_side = cube.Edges[edge[1]].side

	if cube.left == color:
		cube.yc()
	elif cube.right == color:
		cube.y()
	elif cube.back == color: 
		cube.y()
		cube.y()
	
	# Position and orient each piece, 24 different possibilities
	print ("Placing edge: {0}-{1}".format(color, WHITE))
	if white_side == cube.front:
		if color_side == cube.bot: #piece needs re-oriented,(Fc,D,Rc,Dc)
			cube.Fc()
			cube.D()
			cube.Rc()
			cube.Dc()
		elif color_side == cube.left: #Dc, L, D
			cube.Dc()
			cube.L()
			cube.D()
		elif color_side == cube.top: #Fc, Dc, L, D
			cube.Fc()
			cube.Dc()
			cube.L()
			cube.D()
		else: #right, D, Rc, Dc
			cube.D()
			cube.Rc()
			cube.Dc()
	elif white_side == cube.left:
		if color_side == cube.front: #Fc
			cube.Fc()
		elif color_side == cube.top: #L, Fc, Lc
			cube.L()
			cube.Fc()
			cube.Lc()
		elif color_side == cube.back: #L2, Fc, L2
			cube.L2()
			cube.Fc()
			cube.L2()
		else: #bot: Lc, Fc	
			cube.Lc()
			cube.Fc()
	elif white_side == cube.right:
		if color_side == cube.front: #F
			cube.F()
		elif color_side == cube.top: #Rc, F, (R)
			cube.Rc()
			cube.F()
			cube.R()
		elif color_side == cube.back: #R2, F, (R2)
			cube.R2()
			cube.F()
			cube.R2()
		else: #bot: R, F (no need to protect)
			cube.R()
			cube.F()
	elif white_side == cube.back:
		if color_side == cube.bot: #B2, U, Rc, F, (R)
			cube.B2()
			cube.U()
			cube.Rc()
			cube.F()
			cube.R()
		elif color_side == cube.left: #L, Uc, F2, (Lc)
			cube.L()
			cube.Uc()
			cube.F2()
			cube.Lc()
		elif color_side == cube.top: # U, Rc, F, (R)
			cube.U()
			cube.Rc()
			cube.F()
			cube.R()
		else: #right: Rc, U, F2, (R)
			cube.Rc()
			cube.U()
			cube.F2()
			cube.R()
	elif white_side == cube.bot:
		if color_side == cube.front: #then already good
			continue
		elif color_side == cube.left: #L2, Uc, F2 (could be just D if first)
			cube.L2()
			cube.Uc()
			cube.F2()
		elif color_side == cube.right: #R2, U, F2 (or Dc if first)
			cube.R2()
			cube.U()
			cube.F2()
		else: #back: B2, U2, F2 (or D2 if first)
			cube.B2()
			cube.U2()
			cube.F2()
	elif white_side == cube.top:
		if color_side == cube.front: #F2
			cube.F2()
		elif color_side == cube.left: #Uc, F2
			cube.Uc()
			cube.F2()
		elif color_side == cube.right: #U, F2
			cube.U()
			cube.F2()
		else: #back: U2, F2
			cube.U2()
			cube.F2()
# check to make sure white cross successful
white_cross = True
for edge in white_edges:
	if cube.Edges[0].side == cube.Edges[0].color and cube.Edges[1].side == cube.Edges[1].color:
		continue
	else:
		white_cross = False
		break
if white_cross:
	print ("--- White cross positioned successfully")
else:
	print ("--- White cross not correct, error occurred.")

cube.print_State()
# Step 2 - position and orient white corners
#     1. place white on top - z2
#     2. any white corners on bottom? (max 4 times through loop)
#          a. if yes, then position with R' D' R D, go to step 2
#               in case corner at right bottom with white on front, do D' R' D R 
#          b. if no, then any corners on top need oriented or moved?
#               i. if need moved, then move to bottom
#               ii. if need oriented, do algo 


# Step 3 - position and orient middle edges
#     1. get edge to match either front or right side
#         a. if front, do U R U' R' U' F' U F 
#         b. if side, do U' F' U F U R U' R' 
# Step 4 - Orient top cross
#     1. if 2 adjacent yellows on top, do f R U R' U' f' 
#     2. if something else, do F R U R' U' F' 
#     3. if no yellow, 2nd then 1st
# Step 5 - Permute top cross
#     1. match color to front side, then do R U R' U R U2 R' 
#     2. If two match and two need flopped, do 1st then U to finish
# Step 6 - permute top corners
#     1. get correctly permuted corner at front top left of possible, then do  U R U' L' U R' U' L
# Step 7 - Orient top corners
#     1. for each corner needing permuted, put first at front top left, then do R' D' R D 
#     2. Do U or U' as necessary, then 1st until cube is solved 

# Edges can be in 8 spots in 2 different orientations, 16 total positions
	# narrow down edge spots by moving edges on middle layer, 8-3 = 5
		# 10 total edge positions
# corners can be in 8 spots in 3 different orientations, 24 total positions		
	# narrow down corners by only working corners from 2 positions	
		# 6 total positions

# Step 2 - solve bottom corner and middle edges 2 at a time
	# get a corner-edge pair (corners on top are easier, should be done first)
		# look on top side for white corner 
			#if edge is on top, position pair
			#if no corner/edge pair on top, then do corner top edge side	
		# if no corner on top, then do corner on bottom
			#if no corner edge on same side bot, then move corner to top
			
	
	# make left side color of edge front
	# position corner
		# if edge on another side than corner, position edge
	# match pattern, do respective algo

# Step 3 - Orient Last Layer (OLL algorithms)
	# match pattern, do respective algo
# Step 4 - Permute Last Layer (PLL algorithms)
	# match pattern, do respective algo