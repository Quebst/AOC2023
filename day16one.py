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
    lines = raw_data.splitlines()
    energy_field = [[0 for _ in range(len(lines) + 2)] for y in range(len(lines[0]) + 2)]
    board = [['x' for _ in range(len(lines) + 2)] for y in range(len(lines[0]) + 2)]
    visited = []
    total_energized = 0
    
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            board[i + 1][j + 1] = lines[i][j]
    sys.setrecursionlimit(2600)                
    # for row in board:
    #     for char in row:
    #         print(char, " ", end="")    
    #     print("")
    
    ray(board, energy_field, visited, [1, 1], "E" )
    
    # print("-------------------------------------")
    # for row in energy_field:
    #     for char in row:
    #         print(char, " ", end="")    
    #     print("")
    
    for row in energy_field:
        total_energized += sum(row)
    print("Energized tiles is: ", total_energized)

# recursive function to follow each light path
def ray(board, energy, visited, loc, direction):
    i, j = loc
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
            ray(board, energy, visited, [i - 1, j], "N")
        elif char == "/":
            ray(board, energy, visited, [i, j + 1], "E")
        elif char == "\\":
            ray(board, energy, visited, [i, j - 1], "W")
        elif char == "-":
            visited.append([i, j, "N"])
            ray(board, energy, visited, [i, j - 1], "W")
            ray(board, energy, visited, [i, j + 1], "E")
    elif direction == "S":
        if char == "." or char == "|":
            ray(board, energy, visited, [i + 1, j], "S")
        elif char == "/":
            ray(board, energy, visited, [i, j - 1], "W")
        elif char == "\\":
            ray(board, energy, visited, [i, j + 1], "E")
        elif char == "-":
            visited.append([i, j, "S"])
            ray(board, energy, visited, [i, j - 1], "W")
            ray(board, energy, visited, [i, j + 1], "E")
    elif direction == "W":
        if char == "." or char == "-":
            ray(board, energy, visited, [i, j - 1], "W")
        elif char == "/":
            ray(board, energy, visited, [i + 1, j], "S")
        elif char == "\\":
            ray(board, energy, visited, [i - 1, j], "N")
        elif char == "|":
            visited.append([i, j, "W"])
            ray(board, energy, visited, [i - 1, j], "N")
            ray(board, energy, visited, [i + 1, j], "S")
    elif direction == "E":
        if char == "." or char == "-":
            ray(board, energy, visited, [i, j + 1], "E")
        elif char == "/":
            ray(board, energy, visited, [i - 1, j], "N")
        elif char == "\\":
            ray(board, energy, visited, [i + 1, j], "S")
        elif char == "|":
            visited.append([i, j, "E"])
            ray(board, energy, visited, [i - 1, j], "N")
            ray(board, energy, visited, [i + 1, j], "S")
            
    return
        
        


if __name__ == "__main__":
    main()
