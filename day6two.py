raw_data = """Time:      7  15   30
Distance:  9  40  200"""

read_data = """Time:        62     64     91     90
Distance:   553   1010   1473   1074
"""

low = 1
def main():
    lines = read_data.splitlines()
    temp, times = lines[0].split(":")
    times = times.split()
    temp, distances = lines[1].split(":")
    distances = distances.split()
    time = ""
    distance = ""
    
    for i in times:
        time = time + i
    for j in distances:
        distance = distance + j
        
    time = int(time)
    distance = int(distance)
    total = time
    speed = time // 2
    time = total - speed
    old_time = 0
    possible = time
    
    print(time, " ")
    print(distance)

    while(True):
        possible = (possible / 2) 
        record = time * speed
        if record == distance:
            print("Result is: ", record)
            break
        elif record > distance:
            old_time = time
            time = time - possible
            speed = total - time
        elif record < distance:
            old_time = time
            time = time + possible
            speed = total - time
        if time == old_time:
            if record < distance:
                time += 1
                speed -= 1
                record = time * speed
            print("Answer is: ", time, " record is: ", record)
            break
        
        print(f"Record: {record} time: {time} speed: {speed}")
      
    ways = max(speed, time) - min(speed, time) + 1 
    print(f"There are {ways} ways to win this race")
    

if __name__ == "__main__":
    main()