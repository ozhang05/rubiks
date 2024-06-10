color_key = ["w", "r", "b", "y", "o", "g"]

cube = [0] * 54

for i in range(6):
    for j in range(9):
        cube[(i * 9) + j] = i

def render(perspective = 0):
    print()

def print_cube():
    for i in range(3):
        print("     ", end = " ")
        for j in range(3):
            #print(8 - ((i * 3) + j), end = " ")
            print(color_key[cube[8 - ((i * 3) + j)]], end = " ")
        print()
    
    for i in range(3):
        #red
        for j in range(3):
            print(color_key[cube[9 + (i * 3) + j]], end = " ")
        #blue
        for j in range(3):
            print(color_key[cube[((2 + (j * 3) - i) % 9) + 18]], end = " ")
        #orange
        for j in range(3):
            print(color_key[cube[44 - ((i * 3) + j)]], end = " ")
        #green
        for j in range(3):
            print(color_key[cube[(47 + (j * 3) - i)]], end = " ")
        
        print()

    for i in range(3):
        print("     ", end = " ")
        #yellow
        for j in range(3):
            print(color_key[cube[35 - ((i * 3) + j)]], end = " ")
        print()

"""
L, R, F, B, U, D
"""
move_shift = {"l": 1, "r": 4, "f" : 2, "b": 5, "u": 0, "d": 3}
print(cube)

def do_move(move):
    temp = [0, 0, 0]
    previous_three = [0, 0, 0]
    if (len(move) == 2):
        move = move[:1:]
        do_move(move)
        do_move(move)

    move.lower

    center_side = move_shift[move]
    opposite_side = (center_side + 3) % 6

    backwards = False
    if (center_side > opposite_side):
        backwards = True

    if (not backwards):
        upper_side = (center_side + 2) % 3
    else:
        upper_side = (center_side - 1) % 3 + 3

    if (not backwards):
        right_side = ((center_side + 1) % 3)
    else:
        right_side = ((center_side - 2) % 3)
    
    bottom_side = (upper_side + 3) % 6
    left_side = (right_side + 3) % 6

    print ("Current move", move, center_side, upper_side, right_side, backwards)

    #new
    #store top layer values
    if (not backwards):
        for i in range((9 * upper_side) + 2, (9 * upper_side) + 11, 3):
            temp[int((i - ((9 * upper_side) + 2)) / 3)] = cube[i]
            previous_three[int((i - ((9 * upper_side) + 2)) / 3)] = i
    else:
        for i in range((9 * upper_side), (9 * upper_side) + 9, 3):
            temp[int((i - (9 * upper_side)) / 3)] = cube[i]
            previous_three[int((i - (9 * upper_side)) / 3)] = i

    #set right layer values
    if (not backwards):
        for i in range((9 * right_side), (9 * right_side) + 3, 1):
            cube[previous_three[i - (9 * right_side)]] = cube[i]
            previous_three[i - (9 * right_side)] = i
    else:
        for i in range((9 * right_side) + 6, (9 * right_side) + 9, 1):
            cube[previous_three[i - ((9 * right_side) + 6)]] = cube[i]
            previous_three[i - ((9 * right_side) + 6)] = i

    #set bottom layer values
    if (not backwards):
        for i in range((9 * bottom_side) + 2, (9 * bottom_side) + 11, 3):
            cube[previous_three[int((i - ((9 * bottom_side) + 2)) / 3)]] = cube[i]
            previous_three[int((i - ((9 * bottom_side) + 2)) / 3)] = i
    else:
        for i in range((9 * bottom_side), (9 * bottom_side) + 10, 3):
            temp[(i - (9 * bottom_side)) % 3] = cube[i]
            previous_three[(i - (9 * bottom_side)) % 3] = i

    #set left layer values
    #need to accound for doing reverse if (backwards)
    if (not backwards):
        for i in range((9 * left_side) + 6, (9 * left_side) + 9, 1):
            cube[previous_three[i - ((9 * left_side) + 6)]] = cube[i]
            previous_three[i - ((9 * left_side) + 6)] = i
    else:
        for i in range((9 * left_side), (9 * left_side) + 3, 1):
            cube[previous_three[i - (9 * left_side)]] = cube[i]
            previous_three[i - (9 * left_side)] = i

    #set top layer values
    #need to accound for doing reverse if (backwards)
    for i in range(0, 3, 1):
        #print ("Previous three is ", previous_three[i], "temp is ", temp[i])
        cube[previous_three[i]] = temp[i]

    """    
    #old
    #store first layer values
    for i in range(0,7,3):
        temp[i % 3] = cube[i]
    
    #changes one layer
    for i in range(0, 7, 3):
        cube[i] = cube[i + 45]

    #changes second layer
    for i in range(0, 7, 3):
        cube[i + 45] = cube[i + 27]

    #changes third layer
    for i in range(0, 7, 3):
        cube[i + 27] = cube[i + 18]

    #sets fourth layer to stored values
    for i in range(0, 7, 3):
        cube[i + 18] = temp[i % 3]
    """

    #rotate left side
    temp[0] = cube[(center_side * 9) + 1]
    temp[1] = cube[(center_side * 9) + 2]

    cube[(center_side * 9) + 1] = cube[(center_side * 9) + 3]
    cube[(center_side * 9) + 2] = cube[(center_side * 9)]

    cube[(center_side * 9) + 3] = cube[(center_side * 9) + 7]
    cube[(center_side * 9)] = cube[(center_side * 9) + 6]

    cube[(center_side * 9) + 7] = cube[(center_side * 9) + 5]
    cube[(center_side * 9) + 6] = cube[(center_side * 9) + 8]

    cube[(center_side * 9) + 5] = temp[0]
    cube[(center_side * 9) + 8] = temp[1]

    print_cube()



possible_moves = ["l", "r", "f", "b", "u", "d"]

"""for key in possible_moves:
    do_move(key)"""

"""
l works
r broke
f works
b broke
u works
d broke

this means that backwards = true -> code is broke
"""

do_move("r")

#print_cube
"""
while(True):
    move = input("")
    do_move(move)

    if ((cube)):
        print("You solved the cube!")
        break


"""

print_cube() 

"""




"""