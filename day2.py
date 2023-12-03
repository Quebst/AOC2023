RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14

raw_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

test_data = """Game 8: 3 green, 10 red, 15 blue; 1 green, 9 red; 9 blue, 2 green, 12 red"""


def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    id_total = 0
    
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
                
        if red_total <= RED_LIMIT and blue_total <= BLUE_LIMIT and green_total <= GREEN_LIMIT:
            id_total += int(game_id)
            
    print(id_total)
                
        
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
