raw_data = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""

raw_data2 = """0,0,1~1,0,1
0,1,1~0,1,2
0,0,5~0,0,5
0,0,4~0,1,4"""


def main():
    with open("input.txt", encoding="utf-8") as f:
        read_data = f.read()
    lines = read_data.splitlines()
    bricks = []
    settled = []
    keepers = set()
    
    # a's are always <= b's
    for line in lines:
        start, end = line.split("~")
        ax, ay, az = start.split(",")
        bx, by, bz = end.split(",")
        bricks.append(Brick(ax, ay, az, bx, by, bz))
        
    bricks = sorted(bricks, key=lambda x: x.az)
    #for brick in bricks:
        #print(brick)
    
    # Grid is x, y map of top of pile, first element is z level, second is brick attached
    grid = [[[0, None] for _ in range(10)] for _ in range(10)]
    
    
    while bricks:
        block = bricks.pop(0)
        xs, ys, zmag = block.btop()
        
        zztop = 0
        for x in xs:
            for y in ys:
                if grid[x][y][0] > zztop:
                    zztop = grid[x][y][0]
        
        for x in xs:
            for y in ys:
                #print(f"block {block.bnumber} x: {x} y: {y} zmag: {zmag}")
                if grid[x][y][1] and grid[x][y][0] == zztop:
                    block.supported.add(grid[x][y][1])
                grid[x][y][1] = block
                grid[x][y][0] = zztop + zmag
                
        settled.append(block)
        
    for s in settled:
        #print(f"Brick {s.bnumber} is supported by {s.supported}")
        if len(s.supported) == 1:
            keepers.update(s.supported)
        #print(f"{s} is supported by {s.supported}")
            
    destroy = len(settled) - len(keepers)
    
    print(f"{destroy} blocks can be safely removed")
    #print(f"Keepsers: {keepers}")
    #print(f"Settled: {settled}")
    
    #for g in grid:
        #print(g)
    


class Brick:
    count = 0
    
    def __init__(self, ax, ay, az, bx, by, bz):
        self.ax = int(ax)
        self.ay = int(ay)
        self.az = int(az)
        
        self.bx = int(bx)
        self.by = int(by)
        self.bz = int(bz)
        Brick.count += 1
        self.bnumber = Brick.count
        self.supported = set()
        
    def __repr__(self):
        return f"Brick {self.bnumber} is at {self.ax},{self.ay},{self.az} to {self.bx},{self.by},{self.bz}"

    # return list, list, int
    # list of x, list of y, zmag
    def btop(self):
        newx = self.ax
        newy = self.ay
        xs = []
        ys = []
        while newx <= self.bx:
            xs.append(newx)
            newx += 1
        while newy <= self.by:
            ys.append(newy)
            newy += 1
        magz = self.bz - self.az + 1
        
        return xs, ys, magz
            

if __name__ == "__main__":
    main()