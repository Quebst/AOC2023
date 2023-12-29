import sys

raw_data =r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""

"""Directions are N E S W"""

def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    energy_field = [[0 for _ in range(len(lines) + 2)] for y in range(len(lines[0]) + 2)]
    board = [['x' for _ in range(len(lines) + 2)] for y in range(len(lines[0]) + 2)]
    visited = []
    total_energized = 0
    top_score = 0
    score = 0
    
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            board[i + 1][j + 1] = lines[i][j]
    sys.setrecursionlimit(3000)                
    # for row in board:
    #     for char in row:
    #         print(char, " ", end="")    
    #     print("")
    
    i_limit = len(board) - 2
    j_limit = len(board[0]) - 1
    
    # top row going south
    i = 1
    j = 1
    while j < j_limit:
        #print(board[i][j], " ", end="")
        ray(board, energy_field, [], [i, j], "S" )
        energy_field, top_score = ener_sum(energy_field, top_score)
        j += 1
        
    # bottom row going north
    j = 1
    i = 1
    while j < j_limit:
        ray(board, energy_field, [], [i_limit, j], "N" )
        energy_field, top_score = ener_sum(energy_field, top_score)
        j += 1
    
    # left edge going east    
    j = 1
    i = 1  
    while i <= i_limit:
        #print(board[i][j], " ", end="")
        ray(board, energy_field, [], [i, j], "E" )
        energy_field, top_score = ener_sum(energy_field, top_score)
        i += 1

    # right edge going west 
    j = 1
    i = 1  
    while i <= i_limit:
        #print(board[i][j_limit - 1], " ", end="")
        ray(board, energy_field, [], [i, j_limit - 1], "W" )
        energy_field, top_score = ener_sum(energy_field, top_score)
        i += 1
    
    
    #ray(board, energy_field, visited, [1, 1], "E" )
    
    # print("-------------------------------------")
    # for row in energy_field:
    #     for char in row:
    #         print(char, " ", end="")    
    #     print("")
    
    
    print("Energized tiles top score is: ", top_score)

# recursive function to follow each light path
def ray(board, energy, visited, loc, direction):
    i, j = loc
    
    while True:
        char = board[i][j]
        
        # End if char is an "x"
        if char == "x":
            return
        energy[i][j] = 1
        
        # If ray is on a previously visited cord and direction, terminate
        if [i, j, direction] in visited:
            return
        
        # Determine actions based on direction, then symbol
        if direction == "N":
            if char == "." or char == "|":
                i = i - 1
            elif char == "/":
                j = j + 1
                direction = "E"
            elif char == "\\":
                j = j - 1
                direction = "W"
            elif char == "-":
                visited.append([i, j, "N"])
                ray(board, energy, visited, [i, j - 1], "W")
                ray(board, energy, visited, [i, j + 1], "E")
                break
        elif direction == "S":
            if char == "." or char == "|":
                i = i + 1
            elif char == "/":
                j = j - 1
                direction = "W"
            elif char == "\\":
                j = j + 1
                direction = "E"
            elif char == "-":
                visited.append([i, j, "S"])
                ray(board, energy, visited, [i, j - 1], "W")
                ray(board, energy, visited, [i, j + 1], "E")
                break
        elif direction == "W":
            if char == "." or char == "-":
                j = j - 1
            elif char == "/":
                i = i + 1
                direction = "S"
            elif char == "\\":
                i = i - 1
                direction = "N"
            elif char == "|":
                visited.append([i, j, "W"])
                ray(board, energy, visited, [i - 1, j], "N")
                ray(board, energy, visited, [i + 1, j], "S")
                break
        elif direction == "E":
            if char == "." or char == "-":
                j = j + 1
            elif char == "/":
                i = i - 1
                direction = "N"
            elif char == "\\":
                i = i + 1
                direction = "S"
            elif char == "|":
                visited.append([i, j, "E"])
                ray(board, energy, visited, [i - 1, j], "N")
                ray(board, energy, visited, [i + 1, j], "S")
                break
                
        
    return    
        
def ener_sum(ener, top_score):
    score = 0
    for row in ener:
        score += sum(row)
    if score > top_score:
        top_score = score
        print("Score is: ", score)
    ener = [[0 for _ in range(len(ener))] for y in range(len(ener[0]))]
    return ener, top_score
            


if __name__ == "__main__":
    main()
