test_data = """Game 8: 3 green, 10 red, 15 blue; 1 green, 9 red; 9 blue, 2 green, 12 red"""


def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    cube_total = 0
    
    for line in lines:
        red_total = 0
        green_total = 0
        blue_total = 0
        line = line.removeprefix("Game ")
        
        game_id, games = line.split(":")
        
        games = games.split(";")
        
        for game in games:
            red, blue, green = tally_game(game)
            
            if red > red_total:
                red_total = red
            if blue > blue_total:
                blue_total = blue
            if green > green_total:
                green_total = green
                
        cube_total += green_total * blue_total * red_total
            
    print(cube_total)
                
        
def tally_game(game):
    red = 0
    blue = 0
    green = 0
    
    stones = game.split(",")
    for stone in stones:
        stone = stone.strip()
        numb, color = stone.split(" ")
        numb = int(numb)
        
        match color:
            case "red" :
                red += numb
            case "blue" :
                blue += numb
            case "green" :
                green += numb
                
    return red, blue, green
    
    
if __name__ == "__main__":
    main()
