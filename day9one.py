
raw_data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""


def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    final_score = 0
    for line in lines:
        line = line.split()
        next_digit = int(line[-1]) + polate(line)
        print("The next digit is: ", next_digit)
        final_score += next_digit
        
    print(final_score)
            
# creates a new list/line based on supplied above line, passes recursively, returns final item in list    
def polate(line):
    old_digit = 0
    new_list = []
    currents = line
    
    if all(element == 0 for element in currents):
        return 0
        
    i = 1
    while i < len(currents):
        k = int(currents[i]) - int(currents[i - 1])
        
        new_list.append(k)
        i += 1
        
    print(new_list)
            
    
    return new_list[-1] + polate(new_list)
        



if __name__ == "__main__":
    main()
