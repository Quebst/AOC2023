raw_data = """Time:      7  15   30
Distance:  9  40  200"""

read_data = """Time:        62     64     91     90
Distance:   553   1010   1473   1074
"""


def main():
    lines = read_data.splitlines()
    temp, times = lines[0].split(":")
    temp, distances = lines[1].split(":")
    times = list(map(int, times.split()))
    distances = list(map(int, distances.split()))
    
    answer = 1
    i = 0
    while i < len(times):
        time = times[i]
        distance = distances[i]
        speed = 1
        running = time - 1
        beats_record = 0
        
        while speed < time:
            result = running * speed
            if result > distance:
                beats_record += 1
            speed += 1
            running -= 1
        
        print(beats_record)
        answer =  answer * beats_record
        i += 1
            
        
    print(answer)
        



if __name__ == "__main__":
    main()