winning_moves = []

def _all_winning_moves():
    # Rows
    for z in range(3):
        for y in range(3):
            winning_moves.append([(0,y,z),(1,y,z),(2,y,z)])

    # Columns
    for z in range(3):
        for x in range(3):
            winning_moves.append([(x,0,z),(x,1,z),(x,2,z)])

    # Pillars
    for x in range(3):
        for y in range(3):
            winning_moves.append([(x,y,0),(x,y,1),(x,y,2)])

    # XY planes
    for z in range(3):
        winning_moves.append([(0,0,z),(1,1,z),(2,2,z)])
        winning_moves.append([(2,0,z),(1,1,z),(0,2,z)])

    # XZ planes
    for y in range(3):
        winning_moves.append([(0,y,0),(1,y,1),(2,y,2)])
        winning_moves.append([(2,y,0),(1,y,1),(0,y,2)])

    # YZ planes
    for x in range(3):
        winning_moves.append([(x,0,0),(x,1,1),(x,2,2)])
        winning_moves.append([(x,2,0),(x,1,1),(x,0,2)])

    # Space diagonals
    winning_moves.append([(0,0,0),(1,1,1),(2,2,2)])
    winning_moves.append([(2,0,0),(1,1,1),(0,2,2)])
    winning_moves.append([(0,2,0),(1,1,1),(2,0,2)])
    winning_moves.append([(2,2,0),(1,1,1),(0,0,2)])
